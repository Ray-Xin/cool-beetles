from typing import List, Dict

import streamlit as st

# ---------- Page setup ----------
st.set_page_config(
    page_title="Cool Beetles",
    page_icon="🖼️",
    layout="wide",
)

# ---------- Demo data (replace with your own) ----------
GALLERY: List[Dict[str, str]] = [
    {
        "title": "Bombardier Beetle",
        "emoji": "💥",
        "url": "static/beetles/bombardier.jpg",
        "page": "pages/bombardier-beetle.py",
    },
    {
        "title": "Diving Beetle",
        "emoji": "🏊",
        "url": "static/beetles/diving.jpg",
        "page": "pages/diving-beetle.py",
    },
    {
        "title": "Dung Beetle",
        "emoji": "💩",
        "url": "static/beetles/dung.jpg",
        "page": "pages/dung-beetle.py",
    },
    {
        "title": "Hercules Beetle",
        "emoji": "🪲",
        "url": "static/beetles/hercules.jpg",
        "page": "pages/hercules-beetle.py",
    },
    {
        "title": "Tiger Beetle",
        "emoji": "🐅",
        "url": "static/beetles/tiger.jpg",
        "page": "pages/tiger-beetle.py",
    },
    {
        "title": "Tortoise Beetle",
        "emoji": "🐢",
        "url": "static/beetles/tortoise.jpg",
        "page": "pages/tortoise-beetle.py",
    },
]


# ---------- UI ----------
st.title("🖼️ Cool Beetles")

cols_per_row = 3
rows = (len(GALLERY) + cols_per_row - 1) // cols_per_row

idx = 0
for _ in range(rows):
    image_cols = st.columns(cols_per_row, gap="large")
    button_cols = st.columns(cols_per_row, gap="large")

    for image_col, button_col in zip(image_cols, button_cols):
        if idx >= len(GALLERY):
            break

        item = GALLERY[idx]

        with image_col:
            st.image(item["url"], use_container_width=True)

        with button_col:
            if st.button(
                f"{item['emoji']} {item['title']}",
                key=f"open_{idx}",
                use_container_width=True,
            ):
                st.switch_page(item["page"])

            st.link_button(
                "🎮 Play a game",
                "https://example.com",
                use_container_width=True,
            )

        idx += 1
