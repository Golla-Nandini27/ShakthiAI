import streamlit as st
from utils import save_contribution, load_contributions
import random
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io


from datetime import datetime
from utils import get_safety_tip, get_emergency_contacts

st.set_page_config(page_title="ShaktiAI: Women's Safety Assistant", layout="centered")

st.title("🛡️ ShaktiAI: Women's Safety Assistant")

# Time-based tip
current_hour = datetime.now().hour
tip = get_safety_tip(current_hour)
st.subheader("📌 Safety Tip")
st.info(tip)

# Location input
st.subheader("📍 Your City / Area")
location = st.text_input("Enter your city or area (e.g., Hyderabad):")

if location:
    contacts = get_emergency_contacts(location)
    st.subheader("🚨 Emergency Contacts")
    st.write(contacts)

# Safety tips and quotes
safety_tips = [
    "Always share your live location with trusted contacts.",
    "Avoid isolated areas after dark.",
    "Carry a safety whistle or pepper spray.",
    "Inform someone before taking a cab.",
    "Trust your instincts. Leave if you feel unsafe."
]

motivational_quotes = [
    "You are strong, fearless, and capable.",
    "Courage is not the absence of fear, but action in its presence.",
    "You matter. You are powerful beyond measure.",
    "Your voice can change the world.",
    "Never underestimate your strength."
]

def record_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        audio = r.listen(source, timeout=5)
        try:
            text = r.recognize_google(audio)
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.warning("Sorry, could not understand.")
        except sr.RequestError:
            st.error("Could not request results.")
    return ""

# UI Setup

st.markdown("### 🙋‍♀️ Select Language")
lang = st.selectbox("Choose your language", ["English", "Telugu"])

# Voice Input
if st.button("🎤 Use Voice Input"):
    voice_text = record_voice()
else:
    voice_text = ""

# Manual Input
user_text = st.text_area("✍️ Type your safety tip, experience, or suggestion:", value=voice_text)

if st.button("Submit"):
    if user_text:
        save_contribution(user_text, lang)
        st.success("✅ Thanks for your contribution!")
    else:
        st.warning("Please enter some text.")

# Show contributions
if st.checkbox("📚 View Community Contributions"):
    df = load_contributions()
    st.dataframe(df)

# SOS Button (Simulated)
if st.button("🆘 SOS Alert"):
    st.error("🚨 SOS Triggered! Help is on the way!")
    st.balloons()

# Safety Tip
if st.button("🔐 Show Safety Tip"):
    st.info(random.choice(safety_tips))

# Motivation
if st.button("💪 Need Motivation?"):
    st.success(random.choice(motivational_quotes))






# Emergency Contacts
st.markdown("---")
st.subheader("📞 Emergency Contacts")
st.write("- Police: 100")
st.write("- Ambulance: 108")
st.write("- Women’s Helpline: 181")
st.caption("Made with ❤️ for women's safety.")