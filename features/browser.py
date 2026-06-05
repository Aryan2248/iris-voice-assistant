import webbrowser

from utils.speech import speak

def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")


def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


def google_search(query):
    speak(f"Searching for {query}")

    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )