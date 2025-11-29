import streamlit as st

st.set_page_config(
    page_title="Dung Beetle",
    page_icon="💩",
    layout="wide",
)

st.title("💩 Dung Beetle")
st.caption("Scarabaeidae • Nature's recyclers that turn waste into nutrients")


facts_col, image_col = st.columns([0.6, 0.4])
with facts_col:
    st.markdown(
        "Dung beetles play a crucial role in ecosystems by cleaning up animal waste and returning nutrients to the soil. They roll, bury, or live directly inside dung piles, which helps control parasites and fertilize the ground.")
    st.markdown("### 📌 Quick facts")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            - **Diet:** Decomposing matter, or ... POOP
            - **Habitat:** Prairies, grasslands, and savannas worldwide
            - **Color:** Black or brown
            - **Conservation:** Generally stable with localized threats from habitat loss
            """
        )
    with col2:
        st.markdown(
            """
            - **Size:** 2–5 cm
            - **Weight:** 0.5–10 g
            - **Lifespan:** 0.5-2 years
            - **Life cycle:** Egg → Larva → Pupa → Adult
            """
        )

    st.markdown(
        """
### 😎 Cool facts

#### Awesome Adaptations

The dung beetle is primarily known for one thing. As its name suggests the dung beetle spends most of its time in... you guessed it dung. They have a quite unusual way of living like some of the others such as the diving beetle. They have specialized parts to roll or burrow into dung. Let me rephrase can you imagine living and burrowing in your food. Beetles as strong as these are quite rare because a dung beetle can lift 1141 times its own weight. To put that into scale a human could carry an M1 Abrams tank with 10 artillery shells inside.

A dung beetle is a huge part in some cultures not cheese especially in Egyptian ones. Scarab beetles are considered sacred in Egyptian culture. They believed the rolling dung ball looked like the sun moving across the sky which made the beetle a symbol of the sun and rebirth. Dung beetles are also super important for the environment because they clean up waste and recycle nutrients back into the soil.

#### Patterns/Behavior

A dung beetle has many distinctive features. Most have round tough shiny bodies that can be black brown or metallic green. Their legs are strong and spiky which helps them grip and roll dung balls across the ground. Some species even have small horns on their heads for fighting over dung piles.

Their behavior depends on their type. Rollers shape dung into balls and push them away using their back legs. Tunnelers dig underneath dung piles and drag pieces underground. Dwellers live directly inside the dung itself. They are mostly active at night or early morning and they can dig into soil extremely fast when threatened. They are one of the most helpful beetles in the ecosystem.
    """
    )

with image_col:
    st.image("static/beetles/dung.jpg")

if st.button("← Back to Gallery", type="secondary"):
    st.switch_page("cool-beetles.py")
