import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Inject custom CSS for blue theme
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f9ff;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, .stSubheader {
        color: #1e88e5;
    }
    .stButton>button {
        background: linear-gradient(135deg, #1e88e5, #1565c0);
        color: white;
        border-radius: 6px;
        padding: 0.6rem 1.2rem;
        font-weight: 500;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #1565c0;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Main app layout
def main():
    st.title("LinkedIn Post Generator")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.markdown(
            f"""
            <div style="background:#e3f2fd; padding:1rem; border-radius:8px; border:1px solid #1e88e5;">
                <p style="color:#1a1a1a; font-size:1.1rem;">{post}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Run the app
if __name__ == "__main__":
    main()