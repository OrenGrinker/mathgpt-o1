import streamlit as st
from utils import (
    apply_custom_css,
    get_user_input,
    generate_response,
    display_answer,
)

def main():
    """
    Main function to run the MathGPT Streamlit app.
    """
    # Set page configuration for mathematical theme
    st.set_page_config(page_title="MathGPT-o1", page_icon="∑")

    # Apply custom CSS for mathematical design
    apply_custom_css()

    # Get user input
    api_key, query, selected_model = get_user_input()

    if st.button("Get Answer ➤"):
        if not api_key.strip():
            st.warning("Please enter your OpenAI API key.")
        elif not query.strip():
            st.warning("Please enter a math query.")
        else:
            with st.spinner('🧮 Calculating...'):
                answer = generate_response(api_key, query, selected_model)
                if answer:
                    display_answer(answer)

if __name__ == "__main__":
    main()
