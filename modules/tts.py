from re import T
from gtts import gTTS
from io import BytesIO

def create(text, lang):
    mp3 = BytesIO()
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.write_to_fp(mp3)
    return mp3.getvalue()