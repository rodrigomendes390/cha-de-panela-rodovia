import base64

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Chá de Panela",
    page_icon="🎁",
    layout="wide",
)


PRODUCTS = pd.DataFrame(
    [
        {
            "produtos": "Panela roxa com tampa",
            "Categoria": "Cozinha",
            "Preco": "120 - 180",
            "Imagem": "https://images.unsplash.com/photo-1585515320310-259814833e62?auto=format&fit=crop&w=900&q=80",
        },
        {
            "produtos": "Jogo de panos coloridos",
            "Categoria": "Lavanderia",
            "Preco": "40 - 70",
            "Imagem": "https://images.unsplash.com/photo-1604335399105-a0c585fd81a1?auto=format&fit=crop&w=900&q=80",
        },
        {
            "produtos": "Tigela rosa para misturas",
            "Categoria": "Cozinha",
            "Preco": "35 - 60",
            "Imagem": "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?auto=format&fit=crop&w=900&q=80",
        },
        {
            "produtos": "Kit de espatulas",
            "Categoria": "Utensilios",
            "Preco": "25 - 50",
            "Imagem": "https://images.unsplash.com/photo-1590794056226-79ef3a8147e1?auto=format&fit=crop&w=900&q=80",
        },
        {
            "produtos": "Tabua de madeira",
            "Categoria": "Utensilios",
            "Preco": "45 - 90",
            "Imagem": "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?auto=format&fit=crop&w=900&q=80",
        },
        {
            "produtos": "Cesto organizador",
            "Categoria": "Organizacao",
            "Preco": "55 - 100",
            "Imagem": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=900&q=80",
        },
    ]
)


def image_to_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


HERO_IMAGE = image_to_base64("assets/hero.png")


def inject_style():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

        :root {
            --bg: #f5e7d8;
            --surface: #fbefe3;
            --line: #d8bea5;
            --purple: #6c1dc6;
            --purple-2: #9b05db;
            --purple-deep: #6c1dc6;
            --purple-soft: #f0e7ff;
            --orange: #fe8103;
            --orange-soft: #fff0dc;
            --pink: #ff1d6b;
            --pink-2: #e200a2;
            --lilac: #9b05db;
            --yellow: #fbdd49;
            --green: #6f8b53;
            --text: #4b2774;
            --muted: #837081;
        }

        .stApp {
            background: var(--bg);
            color: var(--text);
            font-family: "Poppins", sans-serif;
        }

        [data-testid="stHeader"] {
            display: none;
        }

        [data-testid="stToolbar"],
        #MainMenu,
        footer {
            display: none;
        }

        .block-container {
            max-width: none;
            padding-top: 0;
            padding-left: 0;
            padding-right: 0;
            padding-bottom: 4rem;
        }

        .hero {
            min-height: 68vh;
            padding: 0;
            border-bottom: 1px solid var(--line);
            margin-top: -16px;
            margin-bottom: 1.4rem;
            border-radius: 0;
            background: var(--bg);
            border: 0;
            position: relative;
            overflow: hidden;
        }

        .hero-img {
            width: 100%;
            height: 68vh;
            min-height: 540px;
            display: block;
            object-fit: cover !important;
            object-position: center 28% !important;
        }

        .hero::before,
        .hero::after {
            content: "";
            position: absolute;
            width: 7rem;
            height: 7rem;
            border-radius: 999px;
            opacity: .16;
            pointer-events: none;
        }

        .hero::before {
            left: -2rem;
            top: -2rem;
            background: var(--purple);
        }

        .hero::after {
            right: -2rem;
            bottom: -2rem;
            background: var(--orange);
        }

        .kicker {
            width: fit-content;
            margin-bottom: .9rem;
            border: 1px solid rgba(223, 122, 34, .28);
            border-radius: 999px;
            padding: .36rem .72rem;
            background: rgba(254, 129, 3, .10);
            color: var(--orange);
            font-size: .78rem;
            font-weight: 800;
            letter-spacing: .02em;
            text-transform: uppercase;
        }

        .title {
            margin: 0;
            max-width: 760px;
            color: var(--purple-deep);
            font-size: clamp(2.2rem, 5vw, 4.25rem);
            line-height: .98;
            font-weight: 800;
            letter-spacing: 0;
        }

        .subtitle {
            margin: .85rem 0 0;
            max-width: 620px;
            color: var(--muted);
            font-size: clamp(1rem, 2vw, 1.2rem);
            line-height: 1.45;
            font-weight: 600;
        }

        .flower-line {
            display: flex;
            flex-wrap: wrap;
            gap: .45rem;
            align-items: center;
            margin-top: 1.25rem;
            color: var(--muted);
            font-size: .86rem;
            font-weight: 700;
        }

        .mini-flower {
            width: 1.05rem;
            height: 1.05rem;
            position: relative;
            display: inline-block;
            flex: 0 0 auto;
        }

        .mini-flower::before {
            content: "";
            position: absolute;
            inset: .36rem;
            border-radius: 999px;
            background: var(--orange);
            box-shadow:
                0 -.36rem 0 var(--pink),
                .36rem 0 0 var(--lilac),
                0 .36rem 0 var(--yellow),
                -.36rem 0 0 var(--purple);
        }

        .stats {
            max-width: 1120px;
            display: flex;
            flex-wrap: wrap;
            gap: .6rem;
            margin: 1.25rem auto 1.3rem;
            padding: 0 1rem;
        }

        .stat {
            display: inline-flex;
            gap: .45rem;
            align-items: baseline;
            border: 1px solid var(--line);
            border-radius: 999px;
            padding: .5rem .78rem;
            background: rgba(255, 253, 248, .74);
            color: var(--muted);
            font-size: .9rem;
            font-weight: 650;
        }

        .stat .emoji {
            font-size: 1rem;
            line-height: 1;
            font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
        }

        .stat strong {
            color: var(--purple-deep);
            font-size: 1rem;
        }

        .filters {
            max-width: 1120px;
            margin: .4rem 0 1.3rem;
            padding: 0 1rem;
        }

        div[data-testid="stTextInput"] label,
        div[data-testid="stSelectbox"] label {
            color: var(--text);
            font-size: .86rem;
            font-weight: 750;
        }

        div[data-baseweb="input"] > div,
        div[data-baseweb="select"] > div {
            border-radius: 14px !important;
            border: 1.5px solid rgba(254, 129, 3, .42);
            background: rgba(245, 231, 216, .82);
            box-shadow: none;
            outline: none !important;
        }

        div[data-testid="stTextInputRootElement"],
        div[data-baseweb="input"] {
            border-radius: 14px !important;
            border: 1.5px solid rgba(254, 129, 3, .42) !important;
            background: rgba(245, 231, 216, .82) !important;
            box-shadow: none !important;
        }

        div[data-baseweb="input"] > div:hover,
        div[data-baseweb="select"] > div:hover,
        div[data-testid="stTextInputRootElement"]:hover {
            border-color: rgba(108, 29, 198, .58) !important;
        }

        div[data-baseweb="input"] > div:focus-within,
        div[data-baseweb="select"] > div:focus-within,
        div[data-testid="stTextInputRootElement"]:focus-within {
            border-color: var(--purple) !important;
            box-shadow: 0 0 0 3px rgba(108, 29, 198, .10) !important;
        }

        div[data-baseweb="input"] input,
        div[data-baseweb="select"] span,
        div[data-baseweb="select"] div {
            color: var(--orange) !important;
        }

        div[data-baseweb="input"] input::placeholder {
            color: rgba(254, 129, 3, .62) !important;
            opacity: 1;
        }

        div[data-baseweb="input"] > div:focus-within input,
        div[data-baseweb="input"] > div:focus-within input::placeholder {
            color: var(--purple) !important;
        }

        div[data-baseweb="popover"],
        div[data-baseweb="popover"] > div,
        ul[role="listbox"],
        div[role="listbox"] {
            background: #fbefe3 !important;
            border: 1px solid rgba(108, 29, 198, .22) !important;
            border-radius: 14px !important;
            box-shadow: 0 14px 30px rgba(108, 29, 198, .16) !important;
            overflow: hidden !important;
        }

        li[role="option"],
        div[role="option"] {
            background: #fbefe3 !important;
            color: var(--orange) !important;
            font-weight: 650 !important;
        }

        li[role="option"] *,
        div[role="option"] * {
            background: transparent !important;
            color: var(--orange) !important;
        }

        li[role="option"]:hover,
        div[role="option"]:hover {
            background: #fbefe3 !important;
            color: var(--purple) !important;
        }

        li[role="option"]:hover *,
        div[role="option"]:hover * {
            background: transparent !important;
            color: var(--purple) !important;
        }

        li[role="option"][aria-selected="true"],
        div[role="option"][aria-selected="true"] {
            background: #fbefe3 !important;
            color: var(--purple) !important;
        }

        li[role="option"][aria-selected="true"] *,
        div[role="option"][aria-selected="true"] * {
            background: transparent !important;
            color: var(--purple) !important;
        }

        .section-heading {
            max-width: 1120px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin: 1.1rem auto .9rem;
            padding: 0 1rem;
        }

        .section-heading h2 {
            margin: 0;
            color: var(--text);
            font-size: 1rem;
            font-weight: 800;
            letter-spacing: .02em;
            text-transform: uppercase;
        }

        [data-testid="stHorizontalBlock"] {
            max-width: 1120px;
            margin-left: auto;
            margin-right: auto;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .tiny-flower {
            display: flex;
            gap: .35rem;
            align-items: center;
        }

        .dot {
            width: .48rem;
            height: .48rem;
            border-radius: 999px;
            display: block;
        }

        .dot.purple { background: var(--purple); }
        .dot.orange { background: var(--orange); }
        .dot.pink { background: var(--pink); }
        .dot.lilac { background: var(--lilac); }
        .dot.yellow { background: var(--yellow); }

        .card-body {
            padding: 1rem 0 0;
        }

        div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlock"]:has(> div[data-testid="stElementContainer"] .product-card) {
            padding: .75rem;
            border: 1.5px solid rgba(108, 29, 198, .16);
            border-radius: 20px;
            background: var(--surface);
            box-shadow: 0 10px 22px rgba(108, 29, 198, .055);
            overflow: hidden;
        }

        .product-card {
            padding: 0;
            background: transparent;
            border: 0;
        }

        .product-image {
            width: 100%;
            aspect-ratio: 1 / 1;
            display: block;
            background: #f4eadf;
            background-size: cover;
            background-position: center;
            border-radius: 14px;
            margin: 0;
        }

        .product-name {
            margin: 0 0 .7rem;
            min-height: 2.6rem;
            color: var(--text);
            font-size: 1rem;
            line-height: 1.3;
            font-weight: 800;
        }

        .meta-row {
            display: flex;
            flex-wrap: wrap;
            gap: .4rem;
            margin-bottom: .7rem;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: .3rem .54rem;
            font-size: .76rem;
            line-height: 1;
            font-weight: 750;
            color: var(--purple-deep);
            background: var(--purple-soft);
        }

        .pill.price {
            color: var(--orange);
            background: rgba(254, 129, 3, .10);
        }

        .status {
            margin: .2rem 0 .85rem;
            color: var(--muted);
            font-size: .86rem;
            font-weight: 700;
        }

        .status .emoji,
        .stButton .emoji {
            font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
        }

        .reserve-note {
            border-radius: 12px;
            margin: .2rem 0 .7rem;
            padding: .75rem;
            background: #fff8ea;
            border: 1px solid rgba(242, 200, 102, .45);
            color: var(--text);
            font-size: .88rem;
            font-weight: 650;
        }

        .stButton > button,
        button[data-testid="stBaseButton-secondary"] {
            border: 0;
            border-radius: 12px;
            min-height: 2.75rem;
            background: linear-gradient(135deg, var(--purple), var(--purple-2)) !important;
            color: #ffffff !important;
            font-weight: 800;
            box-shadow: none;
            transition: background .15s ease, transform .15s ease;
        }

        .stButton > button:hover,
        button[data-testid="stBaseButton-secondary"]:hover {
            border: 0;
            color: #ffffff !important;
            background: linear-gradient(135deg, var(--orange), var(--pink)) !important;
            transform: none;
        }

        .stButton > button:disabled,
        button[data-testid="stBaseButton-secondary"]:disabled {
            border: 1px solid rgba(108, 29, 198, .18);
            background: rgba(108, 29, 198, .07) !important;
            color: var(--purple) !important;
            opacity: 1;
            cursor: not-allowed;
            transform: none;
        }

        .stButton > button:disabled:hover,
        button[data-testid="stBaseButton-secondary"]:disabled:hover {
            border: 1px solid rgba(108, 29, 198, .18);
            background: rgba(108, 29, 198, .07) !important;
            color: var(--purple) !important;
            transform: none;
        }

        @media (max-width: 760px) {
            .block-container {
                padding-left: 0;
                padding-right: 0;
                padding-top: 0;
            }

            .hero {
                min-height: 58vh;
            }

            .hero-img {
                height: 58vh;
                min-height: 420px;
            }

            .product-name {
                min-height: auto;
            }
        }
        </style>
        """.replace("__HERO_IMAGE__", HERO_IMAGE),
        unsafe_allow_html=True,
    )


def reserve_item(index, name):
    st.session_state.reservas[index] = name
    st.session_state.card_aberto = None
    st.toast("Reserva feita no prototipo.")


inject_style()

if "reservas" not in st.session_state:
    st.session_state.reservas = {1: "Exemplo"}

if "card_aberto" not in st.session_state:
    st.session_state.card_aberto = None

df = PRODUCTS.copy()
df["Reservado"] = ["Sim" if i in st.session_state.reservas else "Nao" for i in df.index]

available_count = int((df["Reservado"] != "Sim").sum())
reserved_count = int((df["Reservado"] == "Sim").sum())

st.markdown(
    f"""
    <section class="hero">
        <img class="hero-img" src="data:image/png;base64,{HERO_IMAGE}" alt="">
    </section>
    <div class="stats">
            <span class="stat"><span class="emoji">🎁</span><strong>{len(df)}</strong> presentes</span>
            <span class="stat"><span class="emoji">✅</span><strong>{available_count}</strong> disponíveis</span>
            <span class="stat"><span class="emoji">🔒️</span><strong>{reserved_count}</strong> reservados</span>
        </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="filters">', unsafe_allow_html=True)
filter_col, category_col = st.columns([3, 1])

with filter_col:
    busca = st.text_input("Procurar presente", placeholder="Digite o nome do produto")

with category_col:
    categorias = ["Todas"] + sorted(df["Categoria"].unique().tolist())
    categoria = st.selectbox("Categoria", categorias)

st.markdown("</div>", unsafe_allow_html=True)

if len(busca) >= 2:
    df = df[df["produtos"].astype(str).str.contains(busca, case=False, na=False)]

if categoria != "Todas":
    df = df[df["Categoria"] == categoria]

st.markdown(
    """
    <div class="section-heading">
        <h2>Escolha seu presente</h2>
        <div class="tiny-flower">
            <span class="dot purple"></span>
            <span class="dot orange"></span>
            <span class="dot pink"></span>
            <span class="dot lilac"></span>
            <span class="dot yellow"></span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

cards = st.columns(3, gap="medium")

for position, (idx, row) in enumerate(df.iterrows()):
    reservado = row["Reservado"] == "Sim"

    with cards[position % 3]:
        with st.container(border=True):
            st.markdown(
                f"""
                <div class="product-card">
                <div class="product-image" style="background-image: url('{row["Imagem"]}');"></div>
                <div class="card-body">
                    <p class="product-name">{row["produtos"]}</p>
                    <div class="meta-row">
                        <span class="pill">{row["Categoria"]}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if reservado:
                st.markdown('<div class="status reserved"><span class="emoji">🔒️</span> Já escolhido</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="status available"><span class="emoji">✅</span> Disponível</div>', unsafe_allow_html=True)

            if st.session_state.card_aberto != idx:
                if st.button(
                    "🔒️ Reservado" if reservado else "🎁 Reservar",
                    disabled=reservado,
                    key=f"reservar_{idx}",
                    use_container_width=True,
                ):
                    st.session_state.card_aberto = idx
                    st.rerun()
            else:
                st.markdown(
                    '<div class="reserve-note">Deixe seu nome para reservar este presente.</div>',
                    unsafe_allow_html=True,
                )
                nome = st.text_input("Seu nome", key=f"nome_{idx}")

                confirm_col, cancel_col = st.columns(2)
                with confirm_col:
                    confirmar = st.button("Confirmar", key=f"confirmar_{idx}", use_container_width=True)
                with cancel_col:
                    cancelar = st.button("Cancelar", key=f"cancelar_{idx}", use_container_width=True)

                if confirmar:
                    if not nome.strip():
                        st.error("Informe seu nome.")
                    else:
                        reserve_item(idx, nome.strip())
                        st.rerun()

                if cancelar:
                    st.session_state.card_aberto = None
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)
