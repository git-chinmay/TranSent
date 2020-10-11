import streamlit as st
from googletrans import Translator
from textblob import TextBlob
import os


def Translate(text, code):
    if st.button("Translate"):
        translator = Translator()
        try:
            trans = translator.translate(text, dest=code).text
            st.success(trans)
        except Exception as e:
            if os.system("ping www.google.com") == 1:
                st.write("Google.com unrechable.")
            else:
                st.write("Invalid language code.")


def SentimentAnalyser(block):
    if st.button("Sentiment_Analysier"):
        # block = TextBlob(text)
        sentiment_score = block.sentiment.polarity
        if sentiment_score == 0:
            st.success("Neutral Message")
        elif sentiment_score > 0:
            st.success("Positive Message")
        else:
            st.success("Negative Message")


def main():
    st.title("Translator & Sentiment Analysier")
    st.write("(Powered by Googletranslator)")
    activities = ["Translator", "Sentiment_Analysier"]
    selection = ["Yes", "No"]
    displayCode = ["Yes", "No"]
    languageCode = [
        "Amharic:am",
        "Arabic:ar",
        "Basque:eu",
        "Bengali:bn",
        "English (UK):en-GB",
        "Portuguese (Brazil):pt-BR",
        "Bulgarian:bg",
        "Catalan:ca",
        "Cherokee:chr",
        "Croatian:hr",
        "Czech:cs",
        "Danish:da",
        "Dutch:nl",
        "English (US):en",
        "Estonian:et",
        "Filipino:fil",
        "Finnish:fi",
        "French:fr",
        "German:de",
        "Greek:el",
        "Gujarati:gu",
        "Hebrew:iw",
        "Hindi:hi",
        "Hungarian:hu",
        "Icelandic:is",
        "Indonesian:id",
        "Italian:it",
        "Japanese:ja",
        "Kannada:kn",
        "Korean:ko",
        "Latvian:lv",
        "Lithuanian:lt",
        "Malay:ms",
        "Malayalam:ml",
        "Marathi:mr",
        "Norwegian:no",
        "Polish:pl",
        "Portuguese (Portugal):pt-PT",
        "Romanian:ro",
        "Russian:ru",
        "Serbian:sr",
        "Chinese (PRC):zh-CN",
        "Slovak:sk",
        "Slovenian:sl",
        "Spanish:es",
        "Swahili:sw",
        "Swedish:sv",
        "Tamil:ta",
        "Telugu:te",
        "Thai:th",
        "Chinese (Taiwan):zh-TW",
        "Turkish:tr",
        "Urdu:ur",
        "Ukrainian:uk",
        "Vietnamese:vi",
        "Welsh:cy",
    ]
    choice = st.sidebar.selectbox("Select Actions", activities)
    choice2 = st.sidebar.selectbox("Spelling Correction", selection)
    choice3 = st.sidebar.selectbox("Display Language Code List", displayCode)

    # if choice3 == "Yes":
    #    choice4 = st.sidebar.selectbox("Language Code", languageCode)
    #    code = choice4.split(":")
    #    code = code[1]
    # else:
    #    # code = st.text_input("Enter language code")
    #    pass

    text = st.text_input("Text Input")
    block = TextBlob(text)
    if choice2 == "Yes":
        with st.spinner("Wait for it..."):

            corrected_text = block.correct()
            st.success(corrected_text)
            text = corrected_text
    else:
        text = text

    with st.spinner("Wait for it..."):

        if choice == "Translator":
            if choice3 == "Yes":
                choice4 = st.sidebar.selectbox("Language Code", languageCode)
                code = choice4.split(":")
                code = code[1]
            else:
                code = st.text_input("Enter language code")
            Translate(text, code)

        else:
            SentimentAnalyser(block)


if __name__ == "__main__":
    main()
