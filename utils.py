import streamlit as st
from openai import OpenAI

def apply_custom_css():
    """
    Applies custom CSS styles to the Streamlit app for a mathematical theme.
    """
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Georgia', serif;
        }
        .stTextInput > div > input {
            font-family: 'Courier New', monospace;
            background-color: #eef;
        }
        .stTextArea > div > textarea {
            font-family: 'Courier New', monospace;
            background-color: #eef;
        }
        .stButton > button {
            background-color: #004080;
            color: white;
        }
        .stMarkdown {
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def get_user_input():
    """
    Renders input fields for the API key, model selection, and math query, and returns their values.
    """
    st.title("∑ MathGPT")
    st.write("Welcome to **MathGPT**! Enter your OpenAI API key, select a model, and input your math query below.")

    # Input field for OpenAI API key
    api_key = st.text_input("🔑 OpenAI API Key", type="password")

    # Dropdown for model selection
    model_options = ["o1-mini", "o1-preview"]
    selected_model = st.selectbox("🧠 Select Model", model_options)

    # Input field for the math query
    query = st.text_area("✍️ Math Query", height=150)

    return api_key, query, selected_model

def generate_response(api_key, query, selected_model):
    """
    Sends the user's query to the OpenAI API and returns the response.
    """
    # Set the OpenAI API key
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=selected_model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": query
                        },
                    ],
                }
            ]
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def display_answer(answer):
    """
    Displays the answer returned from the OpenAI API.
    """
    st.markdown("### 📚 Answer:")
    # Display the answer with syntax highlighting if it's code
    if "```" in answer:
        st.markdown(answer)
    else:
        st.write(answer)
