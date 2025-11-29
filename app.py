import streamlit as st

# Centralized navigation to control sidebar labels without renaming files
pages = st.navigation(
    [
        st.Page("cool-beetles.py", title="Cool Beetles", icon="🖼️", default=True),
        st.Page(
            "pages/bombardier-beetle.py",
            title="Bombardier Beetle",
            icon="💥",
        ),
        st.Page(
            "pages/diving-beetle.py",
            title="Diving Beetle",
            icon="🏊",
        ),
        st.Page(
            "pages/dung-beetle.py",
            title="Dung Beetle",
            icon="💩",
        ),
        st.Page(
            "pages/hercules-beetle.py",
            title="Hercules Beetle",
            icon="🪲",
        ),
        st.Page(
            "pages/tiger-beetle.py",
            title="Tiger Beetle",
            icon="🐅",
        ),
        st.Page(
            "pages/tortoise-beetle.py",
            title="Tortoise Beetle",
            icon="🐢",
        ),
    ]
)

pages.run()
