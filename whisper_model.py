import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io.wavfile import read
import numpy as np

def record_audio(filename="recording.wav", duration=10):
    print("Speak now... (Recording for", duration, "seconds)")
    audio = sd.rec(int(duration * 16000), samplerate=16000, channels=1, dtype="int16")
    sd.wait()
    write(filename, 16000, audio)
    print("Saved as", filename)
    return filename

def transcribe_audio(filename):
    model = whisper.load_model("base")
    
    sr, audio = read(filename)
    audio = audio.astype(np.float32) / 32768.0  
    
    result = model.transcribe(audio) 
    return result["text"]

if __name__ == "__main__":
    audio_file = record_audio()
    transcription = transcribe_audio(audio_file)
    print("\n-------- Transcription --------")
    print(transcription)