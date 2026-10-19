
import webbrowser
import subprocess
import datetime
import platform
import random
import os
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
            "Notepad cannot open on your computer from the online cloud app. "
            "Run the assistant locally on Windows to use this feature."
        )

    # Calculator
    elif intent == "open_calculator":
        if platform.system() == "Windows":
            try:
                subprocess.Popen(["calc.exe"])
                return "Opening Calculator."
            except OSError:
                return "Could not open Calculator."
        return (
            "Calculator cannot open on your computer from the online cloud app. "
            "Run the assistant locally on Windows to use this feature."
        )

    # Chrome
    elif intent == "open_chrome":
        if platform.system() == "Windows":
            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            ]

            for chrome_path in chrome_paths:
                if os.path.exists(chrome_path):
                    try:
                        subprocess.Popen([chrome_path])
                        return "Opening Chrome."
                    except OSError:
                        pass

        return "Chrome cannot be launched on your computer from the online cloud app."

    # YouTube
    elif intent == "open_youtube":
        return "YouTube: https://www.youtube.com"

    # Google
    elif intent == "open_google":
        return "Google: https://www.google.com"

    # Gmail
    elif intent == "open_gmail":
        return "Gmail: https://mail.google.com"

    # Spotify
    elif intent == "open_spotify":
        return "Spotify: https://open.spotify.com"

    # Search
    elif intent == "search":
        query = text.lower().strip()

        for prefix in ("search for ", "search "):
            if query.startswith(prefix):
                query = query[len(prefix):].strip()
                break

        if not query:
            query = "Google"

        search_url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )

        return f"Search Google for {query}: {search_url}"

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
            "provide website links, search Google, tell jokes, "
            "and answer simple questions. Desktop applications require "
            "the assistant to run locally on your computer."
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
