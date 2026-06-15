import whisper
import sounddevice as sd
from scipy.io.wavfile import write

print("Loading Whisper model...")
model = whisper.load_model("base")

fs = 16000

print("Speak for 5 seconds...")

recording = sd.rec(
    int(5 * fs),
    samplerate=fs,
    channels=1,
    dtype="int16"
)

sd.wait()

write("test.wav", fs, recording)

print("Audio saved as test.wav")
print("Transcribing...")

result = model.transcribe("test.wav")

print("\nYou said:")
print(result["text"])