import streamlit as st
import requests

st.title("🗣️ Générateur vocal avec gTTS (via FastAPI)")

# Zone de saisie
texte = st.text_area("✍️ Entrez un texte à lire à voix haute :", "")
langue = st.selectbox("🌍 Choisissez la langue :", ["fr", "en", "es", "de", "it"], index=0)

# Envoi du texte à l’API
if st.button("🎧 Générer la voix"):
    if texte.strip() == "":
        st.warning("Veuillez entrer un texte.")
    else:
        url = "http://127.0.0.1:8000/tts/"
        data = {
            "text": texte,
            "lang": langue
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            st.audio(response.content, format="audio/mp3")
            st.success("✅ Voix générée avec succès !")
        else:
            st.error("❌ Erreur lors de la génération.")
