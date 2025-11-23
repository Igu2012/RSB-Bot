import config
import speech_recognition as sr

def transcriber():
    AUDIO_FILE = config.OUTPUT_FILENAME

    r = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
        try:
            return (r.recognize_google(audio))
        except:
            print('transcription failed')