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
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Rua+Silva+Rabelo%2C+91"


def inject_style():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,400,0,0');

        .material-symbols-outlined {
            font-family: "Material Symbols Outlined";
            font-weight: normal;
            font-style: normal;
            font-size: 1.25rem;
            line-height: 1;
            letter-spacing: normal;
            text-transform: none;
            display: inline-block;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
            -webkit-font-feature-settings: "liga";
            -webkit-font-smoothing: antialiased;
        }

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
            --purple-2: #6c1dc6;
            --purple-deep: #6c1dc6;
            --purple-soft: #f0e7ff;
            --orange: #fe8103;
            --orange-soft: #fff0dc;
            --pink: #ff1d6b;
            --pink-2: #e200a2;
            --lilac: #6c1dc6;
            --yellow: #fbdd49;
            --green: #595e28;
            --text: #595e28;
            --muted: #7b7768;
        }

        .stApp {
            background: var(--bg);
            color: var(--text);
            font-family: "Poppins", sans-serif;
        }

        div[data-baseweb="modal"],
        div[data-testid="stDialog"] {
            background-color: transparent !important;
            z-index: 1000060 !important;
        }

        div[data-baseweb="modal"] > div:not([role="dialog"]),
        div[data-testid="stDialog"] > div:not([role="dialog"]) {
            background-color: transparent !important;
        }

        body:has([role="dialog"])::before {
            content: "";
            position: fixed;
            inset: 0;
            z-index: 1000050;
            background: rgba(0, 0, 0, .72);
            pointer-events: none;
        }

        [role="dialog"] {
            background-color: var(--surface) !important;
            opacity: 1 !important;
            box-shadow: 0 18px 50px rgba(0, 0, 0, .32) !important;
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

        .event-invite {
            width: calc(100% - 2rem);
            max-width: 1088px;
            display: grid;
            grid-template-columns: minmax(0, 1.25fr) minmax(320px, .75fr);
            gap: clamp(2rem, 6vw, 5rem);
            align-items: center;
            box-sizing: border-box;
            margin: .5rem auto 1.3rem;
            padding: 1.25rem 0 1rem;
            color: var(--text);
        }

        .event-eyebrow {
            display: block;
            margin-bottom: .55rem;
            color: var(--muted);
            font-size: .78rem;
            font-weight: 800;
            letter-spacing: .04em;
        }

        .event-invite-title {
            margin: 0;
            max-width: 680px;
            color: var(--text);
            font-size: clamp(1.9rem, 3.6vw, 3rem);
            line-height: 1.08;
            font-weight: 800;
            letter-spacing: -.025em;
        }

        .event-invite-copy p {
            max-width: 600px;
            margin: .8rem 0 0;
            color: var(--muted);
            font-size: .98rem;
            line-height: 1.55;
        }

        .event-highlight {
            position: relative;
            min-height: 190px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .event-date-lockup {
            position: relative;
            z-index: 1;
            display: flex;
            gap: .65rem;
            align-items: center;
        }

        .event-day {
            color: var(--purple-deep);
            font-size: clamp(4.5rem, 8vw, 6.5rem);
            line-height: .82;
            font-weight: 800;
            letter-spacing: -.07em;
        }

        .event-date-meta {
            color: var(--orange);
            font-size: 1.12rem;
            line-height: 1.15;
            font-weight: 800;
            letter-spacing: 0;
        }

        .event-date-meta strong {
            display: block;
            margin-top: .35rem;
            color: var(--purple-deep);
            font-size: 1.35rem;
            font-weight: 800;
            letter-spacing: 0;
        }

        .event-location-lockup {
            position: relative;
            z-index: 1;
            display: flex;
            gap: .55rem;
            align-items: flex-start;
            margin-top: 1rem;
        }

        .event-location-lockup > .material-symbols-outlined {
            margin-top: .08rem;
            color: var(--orange);
            font-size: 1.25rem;
        }

        .event-location-lockup strong,
        .event-location-lockup span {
            display: block;
        }

        .event-location-lockup strong {
            color: var(--text);
            font-size: .92rem;
        }

        .event-location-lockup span {
            color: var(--muted);
            font-size: .84rem;
        }

        .event-address-link {
            color: inherit !important;
            font-weight: inherit;
            text-decoration-line: underline;
            text-decoration-color: rgba(254, 129, 3, .55);
            text-decoration-thickness: 1px;
            text-underline-offset: 3px;
        }

        .event-address-link:hover {
            color: var(--purple) !important;
            text-decoration-color: var(--purple);
        }

        .event-map-link {
            display: inline-block;
            margin-top: .28rem;
            color: var(--orange) !important;
            font-size: .78rem;
            font-weight: 750;
            text-decoration: none;
        }

        .event-map-link:hover {
            color: var(--purple) !important;
        }

        .event-steps {
            width: calc(100% - 2rem);
            max-width: 1088px;
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: clamp(1rem, 3vw, 2.5rem);
            box-sizing: border-box;
            margin: 0 auto 1rem;
        }

        .event-step {
            position: relative;
            display: block;
        }

        .event-step:not(:last-child)::after {
            content: "";
            position: absolute;
            z-index: 0;
            top: 1.02rem;
            left: 2.15rem;
            right: -3rem;
            height: 2px;
            background: linear-gradient(90deg, var(--purple), var(--orange));
            opacity: .30;
        }

        .event-step-number {
            position: relative;
            z-index: 1;
            grid-row: 1 / span 2;
            width: 2.15rem;
            height: 2.15rem;
            display: grid;
            place-items: center;
            border-radius: 999px;
            background: linear-gradient(135deg, var(--purple), var(--purple-2));
            color: #fff;
            font-size: .78rem;
            line-height: 1;
            font-weight: 800;
            margin-bottom: .55rem;
        }

        .event-step strong {
            display: block;
            color: var(--text);
            font-size: .88rem;
            font-weight: 800;
        }

        .event-step span:last-child {
            display: block;
            margin-top: .12rem;
            color: var(--muted);
            font-size: .78rem;
            line-height: 1.4;
        }

        .event-contact-inline {
            display: flex !important;
            gap: .35rem;
            align-items: center;
            margin-top: 1rem !important;
            color: var(--text) !important;
            font-size: .84rem !important;
        }

        .event-contact-inline .material-symbols-outlined {
            color: var(--purple);
            font-size: 1.05rem;
        }

        .event-contact-inline strong {
            color: var(--text);
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

        .confirmation-details {
            display: grid;
            gap: .55rem;
            margin: .9rem 0;
            padding: .8rem .9rem;
            border-radius: 12px;
            background: var(--orange-soft);
            color: var(--text);
            font-size: .82rem;
            line-height: 1.45;
        }

        .confirmation-details span {
            display: block;
        }

        .event-footer {
            width: calc(100% - 2rem);
            max-width: 1088px;
            box-sizing: border-box;
            margin: 2.2rem auto 0;
            padding: 1.25rem 1rem;
            border: 1px solid rgba(108, 29, 198, .18);
            border-radius: 20px;
            background: rgba(251, 239, 227, .88);
            color: var(--text);
            text-align: center;
        }

        .event-footer strong {
            display: block;
            margin-bottom: .65rem;
            color: var(--purple-deep);
            font-size: 1rem;
        }

        .event-footer-details {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: .45rem 1.2rem;
            font-size: .9rem;
            line-height: 1.45;
        }

        .filters {
            max-width: 1120px;
            margin: .4rem 0 1.3rem;
            padding: 0 1rem;
        }

        .product-start {
            width: calc(100% - 2rem);
            max-width: 1120px;
            box-sizing: border-box;
            margin: 4.2rem auto .9rem;
        }

        .product-start-title {
            margin: 0;
            color: var(--text);
            font-size: clamp(1.35rem, 2.4vw, 1.75rem);
            line-height: 1.2;
            font-weight: 800;
        }

        .product-start p {
            margin: .35rem 0 0;
            color: var(--muted);
            font-size: .88rem;
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
            box-shadow: 0 0 0 1000px var(--bg) inset !important;
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

        [data-testid="stHorizontalBlock"] {
            max-width: 1120px;
            margin-left: auto;
            margin-right: auto;
            padding-left: 1rem;
            padding-right: 1rem;
        }

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

        @media (max-width: 1000px) {
            .event-invite {
                grid-template-columns: minmax(0, 1fr) minmax(280px, .8fr);
                gap: 2rem;
            }
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

            .event-invite,
            .event-steps {
                grid-template-columns: 1fr;
            }

            .event-invite {
                gap: 1.25rem;
                padding-top: .75rem;
                text-align: center;
            }

            .event-invite-copy p {
                margin-right: auto;
                margin-left: auto;
            }

            .event-contact-inline {
                justify-content: center;
            }

            .event-highlight {
                min-height: 190px;
                align-items: center;
            }

            .event-location-lockup {
                text-align: left;
            }

            .event-steps {
                gap: 1rem;
            }

            .product-start {
                margin-top: 3rem;
            }

            .event-step {
                display: grid;
                grid-template-columns: 2.15rem 1fr;
                column-gap: .65rem;
                align-items: start;
            }

            .event-step-number {
                margin-bottom: 0;
            }

            .event-step:not(:last-child)::after {
                top: 2.15rem;
                right: auto;
                bottom: -1rem;
                left: 1.02rem;
                width: 2px;
                height: auto;
                background: linear-gradient(180deg, var(--purple), var(--orange));
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
        f"""
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
                    <span>
                        Traga o presente embrulhado no dia 29/08, às 16h, na
                        <a class="event-address-link" href="{MAPS_URL}" target="_blank"
                           rel="noopener noreferrer">Rua Silva Rabelo, 91 — Salão de Festas</a>.
                    </span>
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
            Estamos contando com você e com esse presente no nosso chá de panela.
        </p>
        <div class="confirmation-details">
            <span>🕓 <strong>29/08, às 16h</strong></span>
            <span>📍 <a class="event-address-link" href="{MAPS_URL}" target="_blank"
                rel="noopener noreferrer">Rua Silva Rabelo, 91 — Salão de Festas</a></span>
            <span>🎨 Escolha tons básicos, como branco, preto, madeira e metalizado,
                ou as cores do casamento — roxo, laranja, rosa e amarelo.</span>
        </div>
        <p class="confirmation-copy">
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
    <section class="event-invite">
        <div class="event-invite-copy">
            <span class="event-eyebrow">Chá de panela Lívia e Rodrigo 💜🧡</span>
            <div class="event-invite-title">Obrigada por fazer parte desse momento tão especial!</div>
            <p>
                Preparamos tudo com muito carinho e estamos contando os dias
                para celebrar com você.
            </p>
            <p class="event-contact-inline">
                <span class="material-symbols-outlined" aria-hidden="true">chat_bubble</span>
                <span><strong>Ainda ficou com dúvidas?</strong> Fale com um dos noivos!</span>
            </p>
        </div>
        <div class="event-highlight">
            <div class="event-date-lockup">
                <span class="event-day">29</span>
                <span class="event-date-meta">de agosto<strong>às 16h</strong></span>
            </div>
            <div class="event-location-lockup">
                <span class="material-symbols-outlined" aria-hidden="true">location_on</span>
                <div>
                    <strong>Rua Silva Rabelo, 91</strong>
                    <span>Salão de Festas</span>
                    <a class="event-map-link" href="{MAPS_URL}" target="_blank"
                       rel="noopener noreferrer">Ver no Google Maps ↗</a>
                </div>
            </div>
        </div>
    </section>
    <div class="event-steps">
        <div class="event-step">
            <span class="event-step-number">1</span>
            <strong>Escolha e reserve</strong>
            <span>Selecione um presente disponível e deixe o seu nome.</span>
        </div>
        <div class="event-step">
            <span class="event-step-number">2</span>
            <strong>Compre onde preferir</strong>
            <span>A loja, a marca e o modelo ficam por sua conta.</span>
        </div>
        <div class="event-step">
            <span class="event-step-number">3</span>
            <strong>Leve no grande dia</strong>
            <span>Traga o presente embrulhado no dia 29/08.</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="product-start">
        <div class="product-start-title">Escolha seu presente:</div>
        <p>Pesquise pelo nome ou navegue pela lista abaixo.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

filter_col = st.columns(1)[0]

with filter_col:
    busca = st.text_input(
        "Procurar presente",
        placeholder="Digite o nome do produto",
        label_visibility="collapsed",
    )

st.markdown(
    f"""
    <div class="stats">
        <span class="stat"><span class="emoji">🎁</span><strong>{len(df)}</strong> presentes</span>
        <span class="stat"><span class="emoji">✅</span><strong>{available_count}</strong> disponíveis</span>
        <span class="stat"><span class="emoji">🔒️</span><strong>{reserved_count}</strong> reservados</span>
    </div>
    """,
    unsafe_allow_html=True,
)

if len(busca) >= 2:
    df = df[df["produtos"].astype(str).str.contains(busca, case=False, na=False)]

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

st.markdown(
    """
    <footer class="event-footer">
        <strong>Nos vemos no dia 29/08! 💜🧡</strong>
        <div class="event-footer-details">
            <span>📍 <a class="event-address-link" href="{MAPS_URL}" target="_blank"
               rel="noopener noreferrer">Rua Silva Rabelo, 91 — Salão de Festas</a></span>
            <span>🕓 16h</span>
        </div>
    </footer>
    """,
    unsafe_allow_html=True,
)
