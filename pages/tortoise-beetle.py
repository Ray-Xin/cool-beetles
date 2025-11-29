import streamlit as st

st.set_page_config(
    page_title="Tortoise Beetle",
    page_icon="🐢",
    layout="wide",
)

st.title("🐢 Tortoise Beetle")
st.caption("Cassidinae • Leaf-clinging beetles with a shield-like shell")

facts_col, image_col = st.columns([0.6, 0.4])
with facts_col:
    st.markdown(
        "The Tortoise beetle is a species of beetle in the family Cassididae. It is a herbivorous species of a leaf beetle that feeds on plant matter. It is a stable species and is not currently threatened with extinction. It is also a prey for many other animals, such as birds and mammals.")
    st.markdown("### 📌 Quick facts")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            - **Diet:** Plant material from the Morning Glory family (Convolvulaceae) or the Nightshade family (Solanaceae)
            - **Habitat:** Forests and grasslands in North America, Europe, and Asia
            - **Color:** Varies from metallic gold and green to mottled brown; clear shell edges add shine
            - **Conservation:** Generally common
            """
        )
    with col2:
        st.markdown(
            """
            - **Size:** 1 cm
            - **Weight:** 0.5–1 g
            - **Lifespan:** Up to 1 year
            - **Life cycle:** Egg → Larva → Pupa → Adult
            """
        )

    st.markdown(
        """
### 😎 Cool facts

#### Awesome Adaptations

The Tortoise Beetle is one of the most unique beetles you can find. Its entire body is covered by a smooth rounded shell that works almost like a turtle shell which is why it is called a tortoise beetle. Its domed shield protects it from predators like birds and spiders. A super cool adaptation is the see through edge of its shell. Some species look metallic gold or shiny green because of tiny layers that reflect light. When the beetle dies or gets scared that gold can fade which makes it even more mysterious.

Another major adaptation is the way these beetles cling tightly to leaves. Their shell can flatten down like a suction cup making it almost impossible for predators to pry them off. In larval form they have one of the strangest defenses ever. They hold a fecal shield over their backs which is a little umbrella made from poop and shed skins. This protects them from hungry insects and even ants. Adults are mostly leaf eaters and use their chewing mouthparts to scrape plant surfaces especially morning glory and sweet potato plants.

#### Patterns/Behavior

A tortoise beetle is easy to recognize if you look closely. It is usually small flat and rounded like a little bump combination. Their colors can be shiny gold green orange or dotted depending on the species. The clear edges of the shell let background colors show through which helps with camouflage.

Their behavior is pretty calm. When something scares them they do not run. They flatten down on the leaf like a suction cup and stay completely still. This makes them very hard for predators to pull off. They are daytime beetles and spend most of their lives eating leaves resting or laying eggs on their host plants.
    """
    )

with image_col:
    st.image("static/beetles/tortoise.jpg")

if st.button("← Back to Gallery", type="secondary"):
    st.switch_page("cool-beetles.py")
