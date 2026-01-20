import streamlit as st

st.title("🌍 Language Dictionary")

languages = {
    "yoruba": {"Favour": "Ọ̀nugba", "God": "Olọ́run", "Time": "Àkókò", "Faith": "Ìgbàgbọ́", "Prosper": "Yọ̀",
               "Longevity": "Gbigbe laaye", "Family": "Ebi", "Love": "Ifẹ́", "King": "Ọba", "Queen": "Ọba ẹbi",
               "Prince": "Ọmọba", "Princess": "Ọmọbinrin", "Joy": "Ayọ̀", "Wisdom": "Ọgbọ́n", "Fortune": "Ọrẹ",
               "Happiness": "Alafia", "Beauty": "Ẹ̀wà", "Excellence": "Àṣe", "Strength": "Agbara", "Success": "Asese"},
    "igbo": {"dog": "nkita", "cat": "pusi", "goat": "ewu", "cow": "ehi", "horse": "hai", "sheep": "aturu", "pig": "ezi",
             "chicken": "okuko", "rat": "oke", "fish": "azu", "hawk": "ugo", "snail": "ejula", "rabbit": "onyeokuku",
             "bat": "anwanta", "turkey": "tooki", "tortoise": "mbe", "snake": "agwo", "elephant": "enyi",
             "monkey": "enwe", "grasshopper": "ukpana"},
    "hausa": {"hello": "sannu", "good afternoon": "ina wuni", "good evening": "ina yamma", "how are you": "lafiya lau",
              "welcome": "barka da zuwa", "please": "don allah", "thank you": "na gode", "you are welcome": "ba komai",
              "sorry": "yi hakuri", "good luck": "saa mai kyau", "take care": "allah ya kiyaye",
              "best wishes": "fatan alheri", "good night": "barka de dare", "congratulations": "taya murna",
              "see you tomorrow": "sai gobe", "all the best": "allah ya sa a dace", "goodbye": "sai mun hadu",
              "no problem": "ba matasala", "well done": "an yi kyau", "best of luck": "allah ya sa a"},
    "edo": {"plum": "plom", "garden egg": "egbon", "wild plum": "ukpon", "banana": "ogede", "coconut": "agbon",
            "kolanut": "ivbi", "orange": "osan", "bitter kola": "atigba", "african pear": "ugba", "local pear": "ukpe",
            "bitter fruit": "orogbo", "bush apple": "ukhi", "date palm fruit": "iyan", "lime": "laimu",
            "cashew": "kashu", "apple": "apulu", "peach": "pesh", "cherry": "cheri", "cranberry": "kranberi",
            "blackberry": "blackberi"}
}

option = st.selectbox(
    "What language dictionary would you like to use?",
    ("edo", "hausa", "idoma", "igbo", "yoruba")
)

word = st.text_input(f"Enter a word to translate in {option.capitalize()}:").strip()

if word:

    translation = languages.get(option, {}).get(word.lower()) or languages.get(option, {}).get(word.capitalize())

    if translation:
        st.success(f"**{word}** in {option.capitalize()} is: **{translation}**")
    else:
        st.error("Word not found in this dictionary.")
