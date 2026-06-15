import webbrowser
import subprocess
import datetime


def perform_action(intent, text):

    # Greetings
    if intent == "greeting":
        return "Hello. How can I help you today?"

    # Name
    elif intent == "name":
        return "I am your AI Voice Assistant."

    # Time
    elif intent == "time":
        current = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current}"

    # Date
    elif intent == "date":
        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today is {today}"

    # Notepad
    elif intent == "open_notepad":
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"

    # Calculator
    elif intent == "open_calculator":
        subprocess.Popen("calc.exe")
        return "Opening Calculator"

    # Chrome
    elif intent == "open_chrome":
        try:
            subprocess.Popen(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            )
        except:
            webbrowser.open("https://www.google.com")

        return "Opening Chrome"

    # YouTube
    elif intent == "open_youtube":
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    # Google
    elif intent == "open_google":
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    # Gmail
    elif intent == "open_gmail":
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    # Spotify
    elif intent == "open_spotify":
        webbrowser.open("https://open.spotify.com")
        return "Opening Spotify"

    # Search
    elif intent == "search":

        query = text.lower()

        query = query.replace("search", "")
        query = query.replace("for", "")

        query = query.strip()

        if query == "":
            query = "google"

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searching for {query}"

    # Joke
    elif intent == "joke":

        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "A SQL query walks into a bar and asks, Can I join you?",
            "There are 10 kinds of people. Those who understand binary and those who don't."
        ]

        import random
        return random.choice(jokes)

    # Help
    elif intent == "help":
        return (
            "I can open Chrome, YouTube, Gmail, Spotify, "
            "Notepad, Calculator, search Google, tell time and date, "
            "and answer simple questions."
        )

    # Status
    elif intent == "status":
        return "I am working perfectly and ready to assist you."

    # Thanks
    elif intent == "thanks":
        return "You are welcome. Happy to help."

    # Goodbye
    elif intent == "goodbye":
        return "Goodbye. Have a nice day."

    # Unknown
    else:
        return "Sorry, I did not understand that command."