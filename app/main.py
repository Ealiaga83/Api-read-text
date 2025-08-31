from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from app.models import TextoRequest
from app.tts_service import generar_audio

app = FastAPI(title="Audio IA", description="Microservicio TTS con gTTS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/tts-json", summary="Generar audio desde JSON", tags=["Audio"])
async def tts_json(request: TextoRequest):
    if len(request.texto.strip()) < 3:
        return {"error": "Texto demasiado corto para generar audio"}

    audio = generar_audio(request.texto)
    headers = {"Content-Disposition": 'attachment; filename="audio.mp3"'}
    return StreamingResponse(audio, media_type="audio/mpeg", headers=headers)