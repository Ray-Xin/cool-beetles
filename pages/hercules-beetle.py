import streamlit as st

st.set_page_config(
    page_title="Hercules Beetle",
    page_icon="🪲",
    layout="wide",
)

st.title("🪲 Hercules Beetle")
st.caption("Dynastes hercules • Giant rhinoceros beetle with impressive horns")

facts_col, image_col = st.columns([0.6, 0.4])
with facts_col:
    st.markdown(
        "The Hercules beetle is a species of beetle in the family Dynastidae. It is a herbivorous species of a ground beetle that feeds on roots, leaves, and other plant material. It is a stable species and is not currently threatened with extinction.")
    st.markdown("### 📌 Quick facts")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            - **Diet:** Roots, leaves, and other plant material
            - **Habitat:** Tropical forests in Central and South America
            - **Color:** Greenish, yellow, or olive elytra with black spots
            - **Conservation:** Not considered threatened
            """
        )
    with col2:
        st.markdown(
            """
            - **Size:** Up to ~17 cm including horns
            - **Weight:** Up to 100 g for the largest males
            - **Lifespan:** 1–2 years
            - **Life cycle:** Eggs → Larvae → Pupae → Adult
            """
        )

    st.markdown(
        """
### 😎 Cool facts

#### Awesome Adaptations

The Hercules Beetle is one of the largest beetles in the world. The males are super easy to identify because of their giant horns. They have one horn on top of the head and one below and they use these to wrestle other males. The horns look scary but they are not dangerous to humans. They are built for flipping rivals during beetle battles.

Another amazing thing is how strong they are. Hercules Beetles can carry things many times heavier than their own body. Their wings are hidden under their hard elytra and even though they look big and heavy they can actually fly. The larvae are huge white grubs that live in rotting wood and help break it down. Adults eat soft fruit sap and decaying plants.

#### Patterns/Behavior

A Hercules Beetle has a large rounded body with smooth hard elytra that can be green yellow olive or spotted with black. The color can change depending on humidity because the surface reacts to moisture. Females do not have large horns.

They are mostly active at night especially in tropical forests. Males spend a lot of time climbing tree trunks and wrestling other males. Even though they look huge they are not aggressive to people and they usually try to fly away if they feel bothered.
    """
    )

with image_col:
    st.image("static/beetles/hercules.jpg")

if st.button("← Back to Gallery", type="secondary"):
    st.switch_page("cool-beetles.py")
