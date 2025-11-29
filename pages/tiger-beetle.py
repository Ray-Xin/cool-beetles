import streamlit as st

st.set_page_config(
    page_title="Tiger Beetle",
    page_icon="🐅",
    layout="wide",
)

st.title("🐅 Tiger Beetle")
st.caption("Cicindelinae • Lightning-fast hunters with sharp mandibles")

facts_col, image_col = st.columns([0.6, 0.4])
with facts_col:
    st.markdown(
        "The Tiger beetle is a species of beetle in the family Cicindelidae. It is a carnivorous species of a ground beetle that feeds on small insects and larvae. It is a stable species and is not currently threatened with extinction. It is also a prey for many other animals, such as birds and mammals.")
    st.markdown("### 📌 Quick facts")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            - **Diet:** Small insects and larvae, though occassionally prey on small animals
            - **Habitat:** Sunny forests, grasslands, dunes, and riverbanks
            - **Color:** Black, white, green, and yellow
            - **Conservation:** Many species are stable, some are local conservation concerns
            """
        )
    with col2:
        st.markdown(
            """
            - **Size:** 2–4 cm
            - **Weight:** 0.5–2 g
            - **Lifespan:** 1–2 years
            - **Life cycle:** Eggs → Larvae → Pupae → Adult
            """
        )

    st.markdown(
        """
### 😎 Cool facts

#### Awesome Adaptations

Tiger Beetles are some of the fastest running insects in the world. They sprint so quickly that they sometimes cannot see while they run and they have to stop for a split second to refocus. Their long legs help them race across sand or dirt to chase their prey like ants spiders and other insects. Their giant mandibles are sharp and curved which makes them perfect for grabbing and holding prey.

Tiger Beetles also have incredible eyesight with big bulging eyes that help them spot movement from far away. Many species have shiny metallic colors like green blue or orange with spots or stripes that make them look like tiny jewels. The bright colors can confuse predators when the beetle is moving fast.

#### Patterns/Behavior

A tiger beetle usually has a slender body long legs and shiny colorful elytra. Their patterns let them blend into sand or dirt while still looking bright up close. They are very active beetles that run stop run again then pounce on prey with lightning speed.

They prefer sunny open habitats like sand dunes paths or riverbanks. When they get scared they either run super fast or fly forward a short distance before landing to look back. Both larvae and adults are predators so they stay carnivorous their whole life.
    """
    )

with image_col:
    st.image("static/beetles/tiger.jpg")

if st.button("← Back to Gallery", type="secondary"):
    st.switch_page("cool-beetles.py")
