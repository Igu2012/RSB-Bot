import pyaudio
import wave
import sys
import config
import transcriber
import typeOut
from pynput.keyboard import Key, Listener

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = config.recordingTime
OUTPUT_FILENAME = config.OUTPUT_FILENAME

p = pyaudio.PyAudio()

device_index = config.device_index

def get_pynput_key(key_name_str):
    if key_name_str in dir(Key):
        return getattr(Key, key_name_str)
    # Para teclas normais (a, b, etc.), retorne a string
    return key_name_str

START_KEY = get_pynput_key(config.prefixKeyStart)
STOP_KEY = get_pynput_key(config.prefixKeyStop)

def show(key):
    if key == START_KEY:
            print(f"Recording from: {p.get_device_info_by_index(device_index)['name']}")
            
            stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=device_index)
            
            print('Recording...')
            frames = []
            
            for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
                    data = stream.read(CHUNK)
                    frames.append(data)
            print('Done')
            
            stream.stop_stream()
            stream.close()
            
            wf = wave.open(OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
                
            print(f'Saved to {OUTPUT_FILENAME}')
            
            try:
                    transcript = transcriber.transcriber()
                    print(transcript)
                    transcript = transcript.split()
                    typeOut.type(transcript[-1])
            except:
                    print('Transcription failed')
    if key == STOP_KEY:
            return False
    
with Listener(on_press=show) as listener:
        listener.join()



