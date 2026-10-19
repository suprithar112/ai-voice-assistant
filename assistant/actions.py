
import datetime
import random
from urllib.parse import quote_plus


def perform_action(intent, text=""):
    """Handle assistant commands safely on Streamlit Cloud and Windows."""

    # Greetings
    if intent == "greeting":
        return "Hello! How can I help you today?"

    # Assistant name
    elif intent == "name":
        return "I am your AI Voice Assistant."

    # Current time
    elif intent == "time":
        current = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current}."

    # Current date
    elif intent == "date":
        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today is {today}."

    # Notepad
    elif intent == "open_notepad":
        return (
            "Notepad cannot be launched directly from Streamlit Cloud. "
            "Please open Notepad manually on your computer."
        )

    # Calculator
    elif intent == "open_calculator":
        return (
            "Calculator cannot be launched directly from Streamlit Cloud. "
            "Please open Calculator manually on your computer."
        )

    # Chrome / browser
    elif intent == "open_chrome":
        return "Open your browser and visit https://www.google.com"

    # Websites
    elif intent == "open_youtube":
        return "Open YouTube: https://www.youtube.com"

    elif intent == "open_google":
        return "Open Google: https://www.google.com"

    elif intent == "open_gmail":
        return "Open Gmail: https://mail.google.com"

    elif intent == "open_spotify":
        return "Open Spotify: https://open.spotify.com"

    # Google search
    elif intent == "search":
        query = (text or "").strip()

        for prefix in ("search for ", "search ", "find "):
            if query.lower().startswith(prefix):
                query = query[len(prefix):].strip()
                break

        if not query:
            return "Please enter something to search for."

        search_url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )
        return f"Search Google for '{query}': {search_url}"

    # Joke
    elif intent == "joke":
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "A SQL query walks into a bar and asks, Can I join you?",
            "There are 10 kinds of people: those who understand binary and those who don't."
        ]
        return random.choice(jokes)

    # Help
    elif intent == "help":
        return (
            "I can greet you, tell you the time and date, tell jokes, "
            "search Google, and provide links to YouTube, Gmail, "
            "Spotify, and Google. Desktop applications must be opened "
            "manually when using the cloud version."
        )

    # Status
    elif intent == "status":
        return "I am running and ready to assist you."

    # Thanks
    elif intent == "thanks":
        return "You are welcome! Happy to help."

    # Goodbye
    elif intent == "goodbye":
        return "Goodbye! Have a nice day."

    # Unknown command
    else:
        return "Sorry, I did not understand that command."
