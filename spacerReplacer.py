import streamlit as st

st.title("🛠️ Space Replacer Tool")
st.write("Replace all spaces in your text with a special character!")

# User input
paragraph = st.text_area("✍️ Enter your paragraph:")
character = st.text_input("🔁 Enter the character to replace spaces:")

if st.button("Replace Now"):
    if character.strip() == "":
        st.warning("⚠️ Please enter a character to replace.")
    else:
        result = paragraph.replace(" ", character)
        st.success("✅ Here is your modified text:")
        st.code(result, language='text')
