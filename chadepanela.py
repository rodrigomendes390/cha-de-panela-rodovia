import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials


# ARQUIVO = "C:\\Users\\digo8\\OneDrive\\Documentos\\coisas\\Cha_de_Panela_v1.xlsx"



# url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit?usp=sharing"

# ==================================================
# CONFIGURAÇÃO
# ==================================================

st.set_page_config(
    page_title="Chá de Panela",
    page_icon="🎁",
    layout="wide"
)

# ID DA PLANILHA GOOGLE SHEETS
SHEET_ID = "1KBLAZ-NQRY4avsighgYBqBvAhebAsmWeDy3ccTib_hw"

# Nome da aba
WORKSHEET_NAME = "Cozinha"

# ==================================================
# AUTENTICAÇÃO GOOGLE
# ==================================================

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

### credenciais antigas

# credentials = Credentials.from_service_account_file(
#     "credenciais.json",
#     scopes=SCOPES
# )

credentials = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPES
)

client = gspread.authorize(credentials)

spreadsheet = client.open_by_key(SHEET_ID)

worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

# ==================================================
# FUNÇÕES
# ==================================================

@st.cache_data(ttl=60)
def carregar_presentes():
    registros = worksheet.get_all_records()
    return pd.DataFrame(registros)

def reservar_item(row_number, nome):

    status = worksheet.acell(
        f"C{row_number}"
    ).value

    if str(status).lower() == "sim":
        raise Exception(
            "Item já reservado"
        )
    
    worksheet.update(
        f"C{row_number}:D{row_number}",
        [["Sim", nome]]
    )

# ==================================================
# CABEÇALHO
# ==================================================

st.markdown("""
<h1 style="
    text-align:center;
    color:white;
    margin-bottom:0px;
">
💜🧡 Chá de Panela da Lívia & Rodrigo 🧡💜
</h1>

<p style="
    text-align:center;
    color:#FFB74D;
    font-size:20px;
">
Escolha um presente especial para celebrar conosco
</p>
""", unsafe_allow_html=True)

# ==================================================
# LEITURA DOS DADOS
# ==================================================

df = carregar_presentes()

if df.empty:
    st.warning("Nenhum presente encontrado.")
    st.stop()

# ==================================================
# FILTROS
# ==================================================

col1, col2 = st.columns([3, 1])

with col1:
    busca = st.text_input(
        "🔎 Procurar presente"
    )

with col2:

    categorias = ["Todas"]

    if "Categoria" in df.columns:
        categorias += sorted(
            df["Categoria"]
            .dropna()
            .unique()
            .tolist()
        )

    categoria = st.selectbox(
        "Categoria",
        categorias
    )

# ==================================================
# FILTRAGEM
# ==================================================

if len(busca) >= 2:
    df = df[
        df["produtos"]
        .astype(str)
        .str.contains(
            busca,
            case=False,
            na=False
        )
    ]

if categoria != "Todas":
    df = df[
        df["Categoria"] == categoria
    ]

# mostra apenas disponíveis
# df = df[
#     df["Reservado"]
#     .astype(str)
#     .str.lower()
#     != "sim"
# ]

st.info(
    f"{len(df[df["Reservado"].astype(str).str.strip().str.lower() != "sim"])} presentes disponíveis"
)

# ==================================================
# CARDS DOS PRESENTES
# ==================================================

st.markdown("""
<style>
div[data-testid="stVerticalBlockBorderWrapper"]{
    padding:0.7rem;
}
</style>
""", unsafe_allow_html=True)

if "card_aberto" not in st.session_state:
    st.session_state.card_aberto = None

st.markdown(
    """
    <style>
    div[data-testid="stVerticalBlockBorderWrapper"]{
        min-height:350px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

cards = st.columns(
    3,
    gap="large"
)

for idx, row in df.iterrows():

    with cards[idx % 3]:

        with st.container(border=True):

            st.markdown(f"#### {row["produtos"]}")

            if row.get("Imagem"):

                st.markdown(
                    f"""
                    <div style="
                        height:230px;
                        width:230px;
                        margin:auto;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        background-color:white;
                        border-radius:10px;
                        overflow:hidden;
                        padding:10px;
                    ">
                        <img src="{row['Imagem']}"
                            style="
                                max-width:100%;
                                max-height:100%;
                                object-fit:contain;
                            ">
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # st.markdown(
                #     "</div>",
                #     unsafe_allow_html=True
                # )

            if row.get("Categoria"):
                st.caption(
                    f"Categoria: {row['Categoria']}"
                )

            if row.get("Preco"):
                st.write(
                    f"💰 Faixa de preço: R$ {row['Preco']}"
                )

            if row.get("Link"):
                st.link_button(
                    "🔗 Ver produto",
                    row["Link"]
                )

            reservado = (
                    str(row["Reservado"]).strip().lower()
                    == "sim"
                )

            if st.session_state.card_aberto != idx:

                
                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown(
                    "<div style='height:33px'></div>",
                    unsafe_allow_html=True
                )

                # if reservado:

                #     st.warning(
                #         "🎁 Este presente já foi reservado"
                #     )

                if reservado:
                    st.markdown(
                        "<span style='color:#FF9800;'>🟠 Já reservado</span>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        "<span style='color:#4CAF50;'>🟢 Disponível</span>",
                        unsafe_allow_html=True
                    )

                if st.button(
                    "🎁 Reservar",
                    disabled = reservado,
                    key=f"reservar_{idx}",
                    use_container_width=True
                ):

                    st.session_state.card_aberto = idx

                    st.rerun()

                

            else:

                st.markdown(
                    "<div style='height:5px'></div>",
                    unsafe_allow_html=True
                )

                nome = st.text_input(
                    "Seu nome",
                    key=f"nome_{idx}"
                )

                ### selecionador do email (DESATIVADO)

                # email = st.text_input(
                #     "Seu e-mail",
                #     key=f"email_{idx}"
                # )

                col_confirmar, col_cancelar = st.columns(2)

                with col_confirmar:

                    confirmar = st.button(
                        "✅ Confirmar",
                        key=f"confirmar_{idx}",
                        use_container_width=True
                    )
                
                with col_cancelar:

                    cancelar = st.button(
                        "❌ Cancelar",
                        key=f"cancelar_{idx}",
                        use_container_width=True
                    )

                if confirmar:

                    if not nome.strip():
                        st.error("Informe seu nome.")

                    ### DESATIVADO do email

                    # elif not email.strip():
                    #     st.error("Informe seu e-mail.")

                    else:

                        row_number = idx + 2

                        reservar_item(
                            row_number,
                            nome
                            # email
                        )

                        st.toast(
                            "🎁 Presente reservado!"
                        )

                        st.cache_data.clear()

                        st.session_state.card_aberto = None

                        st.rerun()

                if cancelar:

                    st.session_state.card_aberto = None

                    st.rerun()