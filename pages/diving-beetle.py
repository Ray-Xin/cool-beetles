import streamlit as st

st.set_page_config(
    page_title="Diving Beetle",
    page_icon="🏊",
    layout="wide",
)

st.title("🏊 Diving Beetle")
st.caption("Dytiscidae • Agile aquatic hunters with paddle-shaped legs")


facts_col, image_col = st.columns([0.6, 0.4])
with facts_col:
    st.markdown(
        "Diving beetles are predaceous beetles from family Dytiscidae. A majority of them are at least concern. However some species are threatened due to habitat loss and pollution. Diving beetles usually do not have fixed predators but are occassionally preyed upon by fish, birds, and other animals."
    )
    st.markdown("### 📌 Quick facts")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            - **Diet:** Other aquatic insects, tadpoles, and fish
            - **Habitat:** Ponds, lakes, streams,marshes and other freshwater habitats worldwide except for Antarctica
            - **Color:** Dark brown, black, or green
            - **Conservation:** Many species are stable, but some decline with water pollution and habitat loss
            """
        )
    with col2:
        st.markdown(
            """
            - **Size:** 1–4 cm
            - **Weight:** 0.5–5 g
            - **Lifespan:** 1–2 years
            - **Life cycle:** Eggs → Larvae → Pupae → Adult
            """
        )

    st.markdown(
        """
### 😎 Cool facts

#### Awesome Adaptations

The Diving Beetle is an excellent swimmer. It swims to catch food and escape from predators. It has an streamlit elongated body to reduce drag underwater. A visible adaptation to their underwater goings are their hind legs. The (sometimes yellow) hind legs are shaped like paddles and have bristles to powerfully push themselves across and under the water. These special legs are one of the reasons that these beetles can go so fast underwater. Other beetles have this such as whirligig beetles and other aquatic beetles. Another visible adaptation is its air pocket. THe diving beetle holds oxygen under its top wing or elytra. This helps it breathe unnderwater for a very long time (10 minutes).

The Diving beetles' defence mechanism is very unique. The diving beetle secretes a milky substance all over itself (like sunscreen). This substance is harmful to predators, making them spit it out ( even if it was killed the substance will take the predator down with it ( unlikely though)). For offence the diving beetle has sharp mandibles in larvae and adult forme. These sharp teeth are really helpful for catching prey, as this is a carnivorous bug throughout its entire life.

#### Patterns/Behavior

A diving beetle has many dinstinctive feature which sets them apart. A diving beetle has an olive green, brown, or black outer elytra. Its body is round and elongated with no hard edges. This reduces drag underwater (I think I said this already). A major feature are its hind legs. Its yellow, brown, or tan hind legs are shaped like paddles and usually 1/4 size relative to their body. Their head is usually tan, brown, and black, as well as the body. However, some exceptions such as the Sunburst Diving Beetle (Thermonnectus Marmoratus) are bright yellow. It's behavior is also sets them apart. Diving beetles are predaceous beetle from family Dytiscidae. are nocturnal, when searching for suitable habitats or hunting. They usually play dead, bite, or kick, in defence.
    """
    )

with image_col:
    st.image("static/beetles/diving.jpg")

if st.button("← Back to Gallery", type="secondary"):
    st.switch_page("cool-beetles.py")
