from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import speech_recognition as sr
import tempfile

app = FastAPI(
    title="Free Speech to Text API",
    description="Upload a .wav file and get transcription for free using Google SpeechRecognition.",
    version="1.0.0"
)

# ✅ Enable CORS (so frontend can call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to ["https://your-frontend-domain.com"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Accepts a .wav file and returns the text transcription.
    """
    if not file.filename.endswith(".wav"):
        return {"error": "Please upload a .wav audio file"}

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(await file.read())
        temp_audio_path = temp_audio.name

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(temp_audio_path) as source:
            audio_data = recognizer.record(source)

        # Use free Google Web Speech API
        text = recognizer.recognize_google(audio_data)

        return {"transcription": text}

    except sr.UnknownValueError:
        return {"error": "Audio could not be understood"}
    except sr.RequestError:
        return {"error": "Speech recognition service unavailable"}
    except Exception as e:
        return {"error": str(e)}
