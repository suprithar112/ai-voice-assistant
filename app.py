from assistant.speech import speak, listen
from assistant.predict import predict_intent
from assistant.actions import perform_action

speak("AI Voice Assistant Started")

while True:

    text = listen()

    if text == "":
        continue

    intent = predict_intent(text)

    response = perform_action(
        intent,
        text
    )

    speak(response)

    if intent == "goodbye":
        break