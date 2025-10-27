# 🎙️ Speech-to-Text API (FastAPI + Google SpeechRecognition)

A free, deployable speech-to-text API built with FastAPI.  
Upload `.wav` audio files and get transcribed text using Google's free Web Speech API.

## 🚀 Features
- 100% free (no API key or paid services)
- Works perfectly on Render Free Tier
- FastAPI backend with CORS enabled for frontend apps
- `.wav` file support

## 🧩 Tech Stack
- **Backend:** FastAPI
- **Speech Recognition:** Google Web Speech API (via `SpeechRecognition` library)
- **Deployment:** Render (Free Plan)

## 🧰 Local Setup
```bash
# Create Python 3.11 environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app:app --reload
