import base64
import html

import streamlit as st

from app_backend import load_products, reserve_product

st.set_page_config(
    page_title="Chá de Panela",
    page_icon="🎁",
    layout="wide",
)


def image_to_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


HERO_DESKTOP_IMAGE = image_to_base64("assets/hero-desktop.webp")
HERO_MOBILE_IMAGE = image_to_base64("assets/hero-mobile.webp")


def inject_style():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

        :root,
        html,
        body {
            color-scheme: light;
        }

        :root {
            --bg: #fbefe2;
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

        .hero picture {
            width: 100%;
            height: 100%;
            display: block;
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

        .reservation-reminder {
            max-width: 1088px;
            display: flex;
            gap: .75rem;
            align-items: flex-start;
            margin: 0 auto 1.4rem;
            padding: .9rem 1rem;
            border: 1px solid rgba(108, 29, 198, .18);
            border-radius: 16px;
            background: rgba(251, 239, 227, .82);
            color: var(--text);
            font-size: .9rem;
            line-height: 1.45;
        }

        .reservation-reminder strong {
            color: var(--purple-deep);
        }

        .intro-lead {
            margin: 0 0 .8rem;
            color: var(--text);
            font-size: .9rem;
            line-height: 1.45;
        }

        .intro-steps {
            display: flex;
            flex-direction: column;
            margin: 0 0 1rem;
        }

        .intro-step {
            position: relative;
            display: flex;
            gap: .8rem;
            align-items: flex-start;
            padding: 0 0 .72rem;
            color: var(--text);
            font-size: .9rem;
            line-height: 1.4;
        }

        .intro-step:last-child {
            padding-bottom: 0;
        }

        .intro-step:not(:last-child)::after {
            content: "";
            position: absolute;
            z-index: 0;
            left: .91rem;
            top: 1.85rem;
            bottom: 0;
            width: 2px;
            background: linear-gradient(var(--purple-2), var(--orange));
            opacity: .42;
        }

        .intro-number {
            position: relative;
            z-index: 1;
            width: 1.9rem;
            height: 1.9rem;
            display: grid;
            place-items: center;
            flex: 0 0 auto;
            border-radius: 999px;
            background: linear-gradient(135deg, var(--purple), var(--purple-2));
            border: 3px solid var(--surface);
            color: #fff;
            font-size: .78rem;
            font-weight: 800;
            box-sizing: border-box;
        }

        .intro-step-copy {
            padding-top: .08rem;
        }

        .intro-step-copy strong,
        .intro-step-copy span {
            display: block;
        }

        .intro-step-copy strong {
            margin-bottom: .12rem;
            color: var(--purple-deep);
            font-size: .91rem;
        }

        .intro-step-copy span {
            color: var(--muted);
            font-size: .85rem;
        }

        .intro-details {
            display: grid;
            gap: .38rem;
            margin: 0 0 .85rem;
            padding: .7rem .78rem;
            border-radius: 12px;
            background: var(--orange-soft);
            color: var(--text);
            font-size: .8rem;
            line-height: 1.38;
        }

        .confirmation-copy {
            color: var(--text);
            font-size: .98rem;
            line-height: 1.6;
            text-align: center;
        }

        .confirmation-heart {
            display: block;
            margin-bottom: .35rem;
            font-size: 2rem;
        }

        .filters {
            max-width: 1120px;
            margin: .4rem 0 1.3rem;
            padding: 0 1rem;
        }

        div[data-testid="stTextInput"] label,
        div[data-testid="stTextInput"] label p,
        div[data-testid="stTextInput"] [data-testid="stWidgetLabel"],
        div[data-testid="stTextInput"] [data-testid="stWidgetLabel"] *,
        div[data-testid="stSelectbox"] label,
        div[data-testid="stSelectbox"] label p {
            color: var(--text) !important;
            font-size: .86rem;
            font-weight: 750;
        }

        div[data-baseweb="input"] > div,
        div[data-baseweb="select"] > div {
            border-radius: 14px !important;
            border: 1.5px solid rgba(254, 129, 3, .42);
            background: rgba(251, 239, 226, .82);
            box-shadow: none;
            outline: none !important;
        }

        div[data-testid="stTextInputRootElement"],
        div[data-baseweb="input"] {
            border-radius: 14px !important;
            border: 1.5px solid rgba(254, 129, 3, .42) !important;
            background: rgba(251, 239, 226, .82) !important;
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

        .stApp div[data-testid="stTextInput"] input,
        div[data-baseweb="input"] input {
            color: var(--text) !important;
            -webkit-text-fill-color: var(--text) !important;
            caret-color: var(--purple) !important;
            opacity: 1 !important;
        }

        div[data-baseweb="select"] span,
        div[data-baseweb="select"] div {
            color: var(--orange) !important;
        }

        div[data-testid="stTextInput"] input::placeholder,
        div[data-baseweb="input"] input::placeholder {
            color: rgba(254, 129, 3, .62) !important;
            -webkit-text-fill-color: rgba(254, 129, 3, .62) !important;
            opacity: 1;
        }

        div[data-testid="stTextInput"] input:focus,
        div[data-baseweb="input"] > div:focus-within input {
            color: var(--purple) !important;
            -webkit-text-fill-color: var(--purple) !important;
        }

        div[data-testid="stTextInput"] input:focus::placeholder,
        div[data-baseweb="input"] > div:focus-within input::placeholder {
            color: var(--purple) !important;
            -webkit-text-fill-color: var(--purple) !important;
        }

        .stApp div[data-testid="stTextInput"] input:-webkit-autofill,
        .stApp div[data-testid="stTextInput"] input:-webkit-autofill:hover,
        .stApp div[data-testid="stTextInput"] input:-webkit-autofill:focus {
            -webkit-text-fill-color: var(--text) !important;
            caret-color: var(--purple) !important;
            box-shadow: 0 0 0 1000px #fbefe2 inset !important;
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
            object-fit: cover;
            object-position: center;
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
                min-height: 0;
                height: min(83.333vw, 390px);
            }

            .hero-img {
                height: min(83.333vw, 390px);
                min-height: 0;
                aspect-ratio: 6 / 5;
                object-position: center !important;
            }

            .product-name {
                min-height: auto;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_style()

if "dinamica_confirmada" not in st.session_state:
    st.session_state.dinamica_confirmada = False

if "reserva_confirmada" not in st.session_state:
    st.session_state.reserva_confirmada = None


@st.dialog("Oiie! Que bom ter você aqui 💜🧡", dismissible=False)
def explicar_dinamica():
    st.markdown(
        """
        <p class="intro-lead">
            Obrigada por fazer parte desse momento com a gente! Preparamos um
            resuminho para contar como tudo funciona ✨
        </p>
        <div class="intro-steps">
            <div class="intro-step">
                <span class="intro-number">1</span>
                <span class="intro-step-copy">
                    <strong>Escolha com carinho</strong>
                    <span>Reserve um presente disponível com o seu nome.</span>
                </span>
            </div>
            <div class="intro-step">
                <span class="intro-number">2</span>
                <span class="intro-step-copy">
                    <strong>Compre onde preferir</strong>
                    <span>A loja, a marca e o modelo ficam por sua conta.</span>
                </span>
            </div>
            <div class="intro-step">
                <span class="intro-number">3</span>
                <span class="intro-step-copy">
                    <strong>Leve no nosso grande dia</strong>
                    <span>Traga o presente embrulhado no dia 29/08.</span>
                </span>
            </div>
        </div>
        <div class="intro-details">
            <span>🖼️ Imagens ilustrativas; por isso não mostramos preços.</span>
            <span>🎨 Não temos regras de cor: escolha tons básicos, como branco,
            preto, madeira e metalizado, ou as cores do casamento — roxo, laranja,
            rosa e amarelo.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "Entendi 💜",
        key="confirmar_dinamica",
        use_container_width=True,
    ):
        st.session_state.dinamica_confirmada = True
        st.rerun()


@st.dialog("Presente reservado!", dismissible=False)
def agradecer_reserva(product_name):
    safe_product_name = html.escape(product_name)
    st.markdown(
        f"""
        <p class="confirmation-copy">
            <span class="confirmation-heart">💜</span>
            Obrigada por reservar <strong>{safe_product_name}</strong>!<br><br>
            Estamos contando com você e com esse presente no dia
            <strong>29/08</strong>, no nosso chá de panela.<br><br>
            Mal podemos esperar para celebrar esse momento juntinhos! ✨
        </p>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "Combinado!",
        key="fechar_confirmacao_reserva",
        use_container_width=True,
    ):
        st.session_state.reserva_confirmada = None
        st.rerun()


if not st.session_state.dinamica_confirmada:
    explicar_dinamica()
elif st.session_state.reserva_confirmada:
    agradecer_reserva(st.session_state.reserva_confirmada)

if "card_aberto" not in st.session_state:
    st.session_state.card_aberto = None

try:
    df = load_products()
except Exception:
    st.error("Não foi possível carregar a lista de presentes. Tente novamente em instantes.")
    st.stop()

if df.empty:
    st.warning("Nenhum presente encontrado.")
    st.stop()

reserved_mask = df["Reservado"].astype(str).str.strip().str.lower() == "sim"
available_count = int((~reserved_mask).sum())
reserved_count = int(reserved_mask.sum())

st.markdown(
    f"""
    <section class="hero">
        <picture>
            <source media="(max-width: 760px)" srcset="data:image/webp;base64,{HERO_MOBILE_IMAGE}">
            <img class="hero-img" src="data:image/webp;base64,{HERO_DESKTOP_IMAGE}"
                 alt="Chá de panela — dia 29 de agosto de 2026" fetchpriority="high">
        </picture>
    </section>
    <div class="stats">
            <span class="stat"><span class="emoji">🎁</span><strong>{len(df)}</strong> presentes</span>
            <span class="stat"><span class="emoji">✅</span><strong>{available_count}</strong> disponíveis</span>
            <span class="stat"><span class="emoji">🔒️</span><strong>{reserved_count}</strong> reservados</span>
    </div>
    <div class="reservation-reminder">
        <span>💜</span>
        <div>
            <strong>Escolheu um presente?</strong>
            Reserve por aqui, compre onde preferir e leve-o embrulhadinho no dia 29/08.
            As imagens são apenas para inspirar a sua escolha.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

filter_col = st.columns(1)[0]

with filter_col:
    busca = st.text_input("Procurar presente", placeholder="Digite o nome do produto")

if len(busca) >= 2:
    df = df[df["produtos"].astype(str).str.contains(busca, case=False, na=False)]

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
    reservado = str(row["Reservado"]).strip().lower() == "sim"
    product_name = html.escape(str(row.get("produtos", "Presente")))
    price = html.escape(str(row.get("Preco", "")))
    image_url = html.escape(str(row.get("Imagem", "")), quote=True)
    image_markup = (
        f'<img class="product-image" src="{image_url}" alt="{product_name}" '
        'loading="lazy" decoding="async">'
        if image_url
        else '<div class="product-image" aria-hidden="true"></div>'
    )

    with cards[position % 3]:
        with st.container(border=True):
            st.markdown(
                f"""<div class="product-card">
{image_markup}
<div class="card-body">
<p class="product-name">{product_name}</p>
{f'''<div class="meta-row">
<span class="pill price">R$ {price}</span>
</div>''' if price else ''}
</div>
</div>""",
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
                        try:
                            reserve_product(int(row["_sheet_row"]), nome.strip())
                        except ValueError as error:
                            st.warning(str(error))
                        except Exception:
                            st.error("Não foi possível concluir a reserva. Tente novamente.")
                        else:
                            st.session_state.card_aberto = None
                            st.session_state.reserva_confirmada = str(
                                row.get("produtos", "seu presente")
                            )
                            st.rerun()

                if cancelar:
                    st.session_state.card_aberto = None
                    st.rerun()
