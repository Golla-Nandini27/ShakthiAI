
## **ShaktiAI – Women’s Safety Assistant**
ShaktiAI is an AI-powered assistant built using **Streamlit** to support **women’s safety** by delivering quick access to emergency contacts, safety tips, and motivational support.
* It also supports voice input and language-based customization.
---

**Summer AI Internship 2025 – Project**  
Developed as part of the Sweecha Summer AI Internship 2025
---
It is a team based project
## 1. Team Information

- **Team Name**: ShaktiAI
- **Team Members**:
  -  Nandini Golla(TeamLeader) – Frontend Developer & Coordinator
  -  Madhuri Jakkampudi – AI Model Integration
  -  Udayasri Paravatha – Backend & Database
  -  Matham Saideepthi – UI/UX and Design
  -  Amulya Naalla – Testing & User Growth
---
#Gitlab
## Git Repository link:
Git Repositorylink:  https://code.swecha.org/Nandinigolla/shaktiai.git

## User Feedback
We collected user feedback using this form:  
🔗 [Google Feedback Form](https://forms.gle/WhRxs9wZhJwSkNuj9)

user aquisition 
https://docs.google.com/document/d/1pbRLSyErC-RKE2dsNtWzqOhRlBXZ5plDNQ9clTFiUSM/edit?usp=sharing

---

## 2. Application Overview

- **App Name**: ShaktiAI
- **Purpose**: To help women easily access:
  -  Emergency contact information
  -  Safety tips
  -  Motivational stories/quotes
  -  Regional language support
- **Core MVP Features**:
  - Language and location-based content
  - Top 5 emergency numbers (static or dynamic)
  - Time/day-based safety tip suggestion
  - Optional voice input for convenience

---

##3.Features

-**Language Selection** – Select your preferred regional language  
- **Location Input** – View emergency contacts based on your location  
- **AI-Generated Safety Tips** – Based on current time/day context  
- **Voice Input Support** – Speak instead of typing (basic version)  
- **Motivational Quote/Story** – Daily positive message  
- **Offline-First Design** – Lightweight and fast loading  
- **Simple, Mobile-Responsive UI** – Streamlit-powered frontend  
---

## 4. Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Voice Input**: `SpeechRecognition` + `PyAudio`
- **Data Storage**: SQLite (optional for offline tip caching)
- **Deployment**: Hugging Face Spaces(not used) or local deployment

---

##  5. Offline-First Strategy

- Preloaded emergency tips and motivation quotes
- Lightweight, fast-loading interface
- Minimal image usage, mostly text-based UI
- Optimized for low internet areas


## 6. User Testing & Feedback *(Planned)*

> ✅ Will be filled after Week 2:
- Feedback forms via Google Forms
- WhatsApp/Instagram collection from real users
- Bugs and improvement logs


##7. Project Lifecycle & Roadmap

### Week 1: Development Sprint
- ✅ Finalize Streamlit UI
- ✅ Display safety tips and motivation
- ✅ Language selector & location input
- ✅ Integrate AI-based time/day safety tips
- ✅ Deploy to Hugging Face (basic version)

### 📍 Week 2: Beta Testing
-  Get feedback from friends/family
-  Log bugs and resolve UI issues
-  features based on usage

### 📍 Weeks 3–4: Outreach & Growth
-  Target Audience: Women in rural & urban areas, students, NGOs
-  Promotion:
  - Instagram reels on safety awareness
  - QR codes on posters shared via WhatsApp
  - Collaborate with Sweecha communities
- 📊 Data Metrics:
  - Total visits
  - Language/area breakdown
  - User feedback

## 8. Post-Internship Vision

-  GPS-based safety alerts
-  Voice-enabled AI chatbot
-  Partner with NGOs for real-world deployment
-  Use collected data to improve rural and urban programs

---

##  Technologies Used

Technology         | Use                          

Python                Core development              
Streamlit             Frontend interface            
SpeechRecognition    Voice input functionality     
PyAudio              Microphone access             
 SQLite (optional)   Local storage/cache           


## 📂 Project Structure
shaktiai/
├── app.py # Main Streamlit App
├── emergency_data.db # SQLite Database for contact info
├── utils/ # Helper functions and logic
│ └── tips.py # AI-based safety tips logic
│ └── motivation.py # Motivational content
├── assets/ # Images used in app
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## ▶️ Run the App Locally

### Prerequisites
- Python 3.10 or higher
- pip

### 📥 Installation
git clone https://code.swecha.org/Nandinigolla/shaktiai.git
cd shaktiai
pip install -r requirements.txt

##🚀 Run the App
Copy code
streamlit run app.py

## 📜 License

MIT License — free to use and modify for educational/non-commercial purposes.
---

###Known Issues
-Voice input may require PyAudio installation
-Multilingual translation still in progress
-Hugging Face hosting not yet integrated


##Credits
Team ShaktiAI – Summer AI Internship 2025
 -Nandinigolla – Frontend Developer & Coordinator
  -  Madhuri Jakkampudi – AI Model Integration
  -  Udayasri Paravatha – Backend & Database
  -  Matham Saideepthi – UI/UX and Design
  -  Amulya Naalla – Testing & User Growth

**Empowering women with the power of AI 🌐**

##  Acknowledgments

Thanks to **Sweecha Foundation** for providing the internship opportunity.  
Special appreciation to mentors and peers for support.


# 🚀 ShaktiAI

ShaktiAI is a community-driven Streamlit app that collects culturally rich data from people across India. The data includes folk tales, recipes, memes, and more — all in local languages — to build a public dataset that preserves our diverse linguistic and cultural heritage.

## 🔥 Features
- Submit text (folk stories, proverbs, etc.)
- Upload image memes or landmarks with captions
- AI-powered language detection
- Offline-first & low-bandwidth friendly

## 🛠️ Tech Stack
- Streamlit
- Python
- LangDetect
- JSON-based corpus

# ShaktiAI

🪔 ShaktiAI is a Streamlit app to crowdsource Indian linguistic and cultural knowledge – folk tales, proverbs, and landmark descriptions – to build a rich AI dataset.

## Features

- Multilingual contribution
- Optional image uploads
- Offline-first saving
- Simple interface

