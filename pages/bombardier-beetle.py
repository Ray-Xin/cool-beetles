import streamlit as st

st.set_page_config(
    page_title="Bombardier Beetle",
    page_icon="💥",
    layout="wide",
)

st.title("💥 Bombardier Beetle")
st.caption("Brachinus • Tiny ground beetle with a mighty chemical defense")


facts_col, image_col = st.columns([0.6, 0.4])
with facts_col:
    st.markdown(
        "The Bombadier beetle is a species of beetle in the family Brachinidae. It is a carnivorous species of a ground beetle that feeds on small bugs and larvae. It is a stable species and is not currently threatened with extinction. It is also a prey for many other animals, such as birds and mammals.")

    st.markdown("### 📌 Quick facts")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            - **Diet:** Small insects and larvae
            - **Habitat:** Temperate forests, woodlands, and grasslands across North America, South America, Europe, Africa, and Australia
            - **Color:** Brown,black, and red
            - **Conservation:** Stable, not considered threatened
            """
        )
    with col2:
        st.markdown(
            """
            - **Size:** 1–2 cm
            - **Weight:** 1–2 g
            - **Lifespan:** 1–2 years
            - **Life cycle:** Eggs → Larvae → Pupae → Adult
            """
        )

    st.markdown(
        """
    ### 😎 Cool facts

    #### Awesome Adaptations

    The Bombardier Beetle is famous for having one of the craziest defenses of any insect. When something tries to eat it the 
    beetle blasts a boiling chemical spray from the tip of its abdomen. It sounds like a tiny pop and the spray is super hot. 
    The beetle mixes two chemicals inside its body and when they combine they explode outward which scares off frogs birds and 
    spiders almost instantly.

    Another cool thing is how the beetle can aim. It can twist its spray nozzle so it can fire in different directions even 
    backwards which makes it very hard to sneak up on. Bombardier beetles are also quick runners and have strong mandibles for 
    catching small insects because they are predators as well as defenders.

    #### Patterns/Behavior

    A bombardier beetle usually has a shiny dark body with reddish or brown legs. They are not very big but they act very bold. 
    If something surprises them they do not freeze or hide. They immediately prepare to spray and then run away fast once the 
    predator backs up.

    They are mostly active at night and hide under rocks leaves or logs during the day. They belong to the ground beetle family 
    and they move quickly when they hunt. Even though they look simple they have one of the most advanced defenses of any beetle.
    """
    )

with image_col:
    st.image("static/beetles/bombardier.jpg")

if st.button("← Back to Gallery", type="secondary"):
    st.switch_page("cool-beetles.py")
