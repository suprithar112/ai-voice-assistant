
import webbrowser
import subprocess
import datetime
import platform
import shutil
import random
from urllib.parse import quote_plus


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
        if platform.system() == "Windows":
            try:
                subprocess.Popen(["notepad.exe"])
                return "Opening Notepad."
            except OSError:
                return "Could not open Notepad."

        return (
            "Notepad is a desktop application. "
            "The cloud app cannot open it on your computer."
        )

    # Calculator
    elif intent == "open_calculator":
        if platform.system() == "Windows":
            try:
                subprocess.Popen(["calc.exe"])
                return "Opening Calculator."
            except OSError:
                return "Could not open Calculator."

        elif platform.system() == "Darwin":
            try:
                subprocess.Popen(["open", "-a", "Calculator"])
                return "Opening Calculator."
            except OSError:
                return "Could not open Calculator."

        else:
            calculator = shutil.which("gnome-calculator")

            if calculator:
                try:
                    subprocess.Popen([calculator])
                    return "Calculator command executed."
                except OSError:
                    pass

            return (
                "Calculator is unavailable on the cloud server. "
                "It cannot open Calculator on your personal computer."
            )

    # Chrome
    elif intent == "open_chrome":
        if platform.system() == "Windows":
            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            ]

            for chrome_path in chrome_paths:
                if shutil.which(chrome_path) or __import__("os").path.exists(chrome_path):
                    try:
                        subprocess.Popen([chrome_path])
                        return "Opening Chrome."
                    except OSError:
                        pass

        # On a hosted app, this opens a URL from the server,
        # not a browser window on the user's personal computer.
        webbrowser.open("https://www.google.com")
        return "Opening Google. The cloud app cannot launch Chrome on your computer."

    # YouTube
    elif intent == "open_youtube":
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    # Google
    elif intent == "open_google":
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    # Gmail
    elif intent == "open_gmail":
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail."

    # Spotify
    elif intent == "open_spotify":
        webbrowser.open("https://open.spotify.com")
        return "Opening Spotify."

    # Search
    elif intent == "search":
        query = text.lower().strip()

        for prefix in ("search for ", "search "):
            if query.startswith(prefix):
                query = query[len(prefix):].strip()
                break

        if not query:
            query = "Google"

        search_url = "https://www.google.com/search?q=" + quote_plus(query)
        webbrowser.open(search_url)

        return f"Searching for {query}."

    # Joke
    elif intent == "joke":
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "A SQL query walks into a bar and asks, Can I join you?",
            "There are 10 kinds of people. Those who understand binary and those who don't."
        ]
        return random.choice(jokes)

    # Help
    elif intent == "help":
        return (
            "I can respond to greetings, tell the time and date, "
            "search Google, open website links, tell jokes, and provide help. "
            "Desktop apps such as Notepad and Calculator require a local "
            "Windows environment."
        )

    # Status
    elif intent == "status":
        return "I am working and ready to assist you."

    # Thanks
    elif intent == "thanks":
        return "You are welcome. Happy to help."

    # Goodbye
    elif intent == "goodbye":
        return "Goodbye. Have a nice day."

    # Unknown
    else:
        return "Sorry, I did not understand that command."
