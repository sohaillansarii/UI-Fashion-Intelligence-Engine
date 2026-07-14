import streamlit as st
import requests

API_URL = "https://fashion-intelligence-engine.up.railway.app"

st.set_page_config(page_title="Fashion Search", layout="wide")
st.title(" Fashion Search Engine")
st.caption("Search by text, refine by image ")

st.markdown("""
<style>
/* Hide min/max labels */
[data-testid="stTickBarMin"],
[data-testid="stTickBarMax"] {
    display: none;
}

/* Hide current value above the thumb */
[data-testid="stSliderValue"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

<<<<<<< HEAD
=======



st.markdown("""
<style>
    /* Hide the tooltip that appears when hovering over sliders */
    .stSlider [data-baseweb="tooltip"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

>>>>>>> 61e8bcb (Initial Commit)
tab1, tab2 = st.tabs(["Text Search", "Refine by Image"])

with tab1:
    query = st.text_input("What are you looking for?", placeholder="e.g. blue shirt for men under 700")
    top_k = st.slider(
    label="",
    min_value=1,
    max_value=10,
    value=5,
    label_visibility="collapsed",
    key="search_k"
)

    if st.button("Search"):
        if query.strip():
            with st.spinner("Searching..."):
                response = requests.get(f"{API_URL}/search", params={"query": query, "top_k": top_k})

            if response.status_code == 200:
                data = response.json()
                st.write(f"**Detected filters:** {data['filters']}")

                if not data["results"]:
                    st.warning("No results found.")
                else:
                    cols = st.columns(len(data["results"]))
                    for col, item in zip(cols, data["results"]):
                        with col:
                            st.image(item["image_url"], width=150)
                            st.markdown(f"**{item['productDisplayName'][:30]}**")
                            st.write(f"₹{item['price']:.0f}")
                            st.write(f"Score: {item['score']:.3f}")
                            st.caption(f"{item['baseColour']} | {item['articleType']} | {item['gender']}")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        else:
            st.warning("Please enter a search query.")

with tab2:
    uploaded_file = st.file_uploader("Upload a product photo", type=["jpg", "jpeg", "png"])
    refine_text = st.text_input("Refine with text (optional)", placeholder="e.g. but in blue")
    image_weight = st.slider("Image weight", 0.0, 1.0, 0.5,
                              help="Higher = trust the photo more, lower = trust the text more")
    top_k_refine = st.slider("Number of results", 1, 10, 5, key="refine_k")

    if uploaded_file:
        st.image(uploaded_file, caption="Your upload", width=200)

    if st.button("Refine Search"):
        if uploaded_file is not None:
            with st.spinner("Refining..."):
                files = {"image": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                data_payload = {"text": refine_text, "image_weight": image_weight, "top_k": top_k_refine}
                response = requests.post(f"{API_URL}/refine", files=files, data=data_payload)

            if response.status_code == 200:
                data = response.json()

                if not data["results"]:
                    st.warning("No results found.")
                else:
                    cols = st.columns(len(data["results"]))
                    for col, item in zip(cols, data["results"]):
                        with col:
                            st.image(item["image_url"], width=150)
                            st.markdown(f"**{item['productDisplayName'][:30]}**")
                            st.write(f"₹{item['price']:.0f}")
                            st.write(f"Score: {item['score']:.3f}")
                            st.caption(f"{item['baseColour']} | {item['articleType']} | {item['gender']}")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        else:
            st.warning("Please upload an image first.")

<<<<<<< HEAD

=======
>>>>>>> 61e8bcb (Initial Commit)
st.markdown(
    """
    ---
    <div style="text-align:center;">
        Made by <b>SOHAIL ANSARI</b>
    </div>
    """,
    unsafe_allow_html=True
)