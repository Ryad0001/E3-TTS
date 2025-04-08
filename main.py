from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from gtts import gTTS
from tempfile import NamedTemporaryFile

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/tts/")
def generate_audio(request: TextRequest):
    if not request.text.strip():
        return {"error": "Texte vide"}

    tts = gTTS(text=request.text, lang='fr')
    temp_file = NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)

    return FileResponse(temp_file.name, media_type="audio/mpeg", filename="audio.mp3")
