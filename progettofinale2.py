import streamlit as st
import grammarbot

def revise_homework(text):
    # Use GrammarBot to correct orthography
    tool = grammarbot.LanguageTool('de-DE')
    matches = tool.check(text)
    revised_text = grammarbot.correct(text, matches)
    return revised_text

def main():
    st.title("Homework Revision Program (German)")
    st.write("Please enter your text (500 characters or less):")

    # Create a text input box for the user to enter the text
    text = st.text_area("Enter your text", height=200)

    # Check if text exceeds the length limit
    if len(text) > 500:
        st.error("Text exceeds the length limit of 500 characters. Please try again.")
        return

    if st.button("Revise Homework"):
        revised_text = revise_homework(text)
        st.write("\nRevised Homework:")
        st.write(revised_text)

if __name__ == "__main__":
    main()
