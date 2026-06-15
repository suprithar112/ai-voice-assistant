import pyttsx3
import threading

def speak(text):

    def run_speech():

        try:
            engine = pyttsx3.init()

            engine.setProperty(
                "rate",
                170
            )

            engine.say(text)

            engine.runAndWait()

        except Exception as e:
            print("Speech Error:", e)

    threading.Thread(
        target=run_speech,
        daemon=True
    ).start()