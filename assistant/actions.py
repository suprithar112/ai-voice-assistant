
import os
import webbrowser
import subprocess
import datetime
from urllib.parse import quote_plus


def perform_action(intent, text=""):
    """
    Execute an action based on the predicted intent
    and return a response string.
    """

    text = (text or "").strip().lower()

    # 1. Greeting
    if intent == "greeting":
        return "Hello! How can I help you today?"

    # 2. Assistant name
    elif intent == "name":
        return "I am your AI Voice Assistant."

    # 3. Current time
    elif intent == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # 4. Current date
    elif intent == "date":
        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today}."

    # 5. Open Notepad
    elif intent == "open_notepad":
        return open_windows_app("notepad.exe", "Notepad")

    # 6. Open Calculator
    elif intent == "open_calculator":
        return open_windows_app("calc.exe", "Calculator")

    # 7. Open Chrome
    elif intent == "open_chrome":
        return open_website(
            "https://www.google.com",
            "Google Chrome / Google"
        )

    # 8. Open websites and platforms
    elif intent in ("open_youtube", "youtube"):
        return open_website("https://www.youtube.com", "YouTube")

    elif intent in ("open_gmail", "gmail"):
        return open_website("https://mail.google.com", "Gmail")

    elif intent in ("open_whatsapp", "whatsapp"):
        return open_website("https://web.whatsapp.com", "WhatsApp Web")

    elif intent in ("open_google", "google"):
        return open_website("https://www.google.com", "Google")

    elif intent in ("open_maps", "google_maps"):
        return open_website("https://maps.google.com", "Google Maps")

    elif intent in ("open_github", "github"):
        return open_website("https://github.com", "GitHub")

    elif intent in ("open_chatgpt", "chatgpt"):
        return open_website("https://chatgpt.com", "ChatGPT")

    elif intent in ("open_instagram", "instagram"):
        return open_website("https://www.instagram.com", "Instagram")

    elif intent in ("open_facebook", "facebook"):
        return open_website("https://www.facebook.com", "Facebook")

    elif intent in ("open_linkedin", "linkedin"):
        return open_website("https://www.linkedin.com", "LinkedIn")

    elif intent in ("open_spotify", "spotify"):
        return open_website("https://open.spotify.com", "Spotify")

    elif intent in ("open_stackoverflow", "stackoverflow"):
        return open_website(
            "https://stackoverflow.com",
            "Stack Overflow"
        )

    elif intent in ("open_amazon", "amazon"):
        return open_website("https://www.amazon.in", "Amazon India")

    # 9. Search Google
    elif intent == "search":
        query = text

        prefixes = (
            "search for ",
            "search ",
            "google ",
            "look up ",
        )

        for prefix in prefixes:
            if query.startswith(prefix):
                query = query[len(prefix):].strip()
                break

        if not query:
            return "Please tell me what you want to search for."

        search_url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )

        return open_website(search_url, f"Google search for {query}")

    # 10. Goodbye
    elif intent == "goodbye":
        return "Goodbye! Have a great day."

    # 11. Unknown command
    return (
        "Sorry, I did not understand that command. "
        "Please try again."
    )


def open_website(url, name):
    """Open a website in the default browser on the local computer."""
    try:
        opened = webbrowser.open(url, new=2)

        if opened:
            return f"Opening {name} in your default browser."

        return f"Please open this link in your browser: {url}"

    except Exception:
        return f"Could not open {name}. You can visit: {url}"


def open_windows_app(command, app_name):
    """Open a Windows desktop application."""
    if os.name != "nt":
        return f"{app_name} can only be launched directly on Windows."

    try:
        subprocess.Popen([command])
        return f"Opening {app_name}."
    except OSError:
        return f"Sorry, I could not open {app_name}."
