import requests
import json

import streamlit as st


def revise_homework(text):
    # Implement your revision logic here
    # This is just a placeholder implementation that adds " [Revised]" to the end of the text
    revised_text = text.strip() + " [Korrigiert]"
    return revised_text

def main():
    print("Willkommen zum Peer Review APP!")
    print("Schreib bitte deinen Text (500 Wörter oder weniger):")
    text = input()

    # Check if text exceeds the length limit
    if len(text) > 500:
        print("Dein Text enthält mehr als 500 Wörter! Versuch es noch einmal!")
        return

    revised_text = revise_homework(text)
    print("\nRevised Homework:")
    print(revised_text)

if __name__ == "__main__":
    main()
