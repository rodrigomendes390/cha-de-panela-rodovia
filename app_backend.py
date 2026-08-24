import os

import pandas as pd
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials


LOCAL = os.getenv("CHA_LOCAL", "").strip().lower() in {"1", "true", "yes"}
PREVIEW = os.getenv("CHA_PREVIEW", "").strip().lower() in {"1", "true", "yes"}
SHEET_ID = "1KBLAZ-NQRY4avsighgYBqBvAhebAsmWeDy3ccTib_hw"
WORKSHEET_NAME = "Cozinha"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def _credentials():
    if LOCAL:
        return Credentials.from_service_account_file(
            "credenciais.json",
            scopes=SCOPES,
        )

    return Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES,
    )


@st.cache_resource
def get_worksheet():
    client = gspread.authorize(_credentials())
    return client.open_by_key(SHEET_ID).worksheet(WORKSHEET_NAME)


@st.cache_data(ttl=300)
def load_products():
    records = get_worksheet().get_all_records()
    products = pd.DataFrame(records)
    products = products.rename(columns={"link": "Link"})

    # A reserva grava o nome na coluna D da planilha. Mantemos um nome de
    # coluna estável para que a interface consiga consultar a reserva mesmo se
    # o cabeçalho da planilha estiver escrito de outra forma.
    if "Nome" not in products.columns:
        products["Nome"] = products.iloc[:, 3] if products.shape[1] >= 4 else ""

    for column in ("Preco", "Imagem", "Link", "Reservado"):
        if column not in products.columns:
            products[column] = ""

    products["_sheet_row"] = range(2, len(products) + 2)
    return products


def reserve_product(sheet_row, name):
    if PREVIEW:
        return

    worksheet = get_worksheet()
    status = worksheet.acell(f"C{sheet_row}").value

    if str(status).strip().lower() == "sim":
        raise ValueError("Este presente acabou de ser reservado por outra pessoa.")

    worksheet.update(f"C{sheet_row}:D{sheet_row}", [["Sim", name]])
    load_products.clear()
