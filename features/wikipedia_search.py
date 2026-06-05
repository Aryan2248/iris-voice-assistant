import wikipedia

from utils.speech import speak

def search_wikipedia(query):

    if not query:
        speak("Please tell me what to search on Wikipedia")
        return

    try:
        speak(f"Searching Wikipedia for {query}")

        result = wikipedia.summary(
            query,
            sentences=2
        )

        print(result)
        speak(result)

    except Exception:
        speak("I could not find information")