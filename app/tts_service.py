from gtts import gTTS
import io

def generar_audio(texto: str) -> io.BytesIO:
    tts = gTTS(text=texto, lang="es")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes