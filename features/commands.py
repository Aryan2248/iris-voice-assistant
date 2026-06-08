import datetime

from config import USER_NAME
from utils.speech import speak

from features.weather import get_weather
from features.browser import (
    open_google,
    open_youtube,
    google_search
)
from features.wikipedia_search import (
    search_wikipedia
)


def extract_city(command):

    phrases = [
        "what's the weather in",
        "what is the weather in",
        "tell me the weather in",
        "weather in",
        "weather"
    ]

    command = command.lower()

    for phrase in phrases:
        if phrase in command:
            return command.replace(phrase, "").strip()

    return ""


def process_command(command):

    if any(word in command for word in ["hello", "hi", "hey"]):
        speak(f"Hello {USER_NAME}")

    elif "how" in command:
        speak("I am doing great. How can I help you?")

    elif "name" in command:
        speak("My name is IRIS")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command:
        today = datetime.date.today().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "weather" in command:

        city = extract_city(command)

        print(f"City extracted: {city}")

        if city:
            get_weather(city)
        else:
            speak("Please tell me the city name")

    elif "open google" in command:
        open_google()

    elif "open youtube" in command:
        open_youtube()

    elif "wikipedia" in command:

        query = command.replace(
            "wikipedia",
            ""
        ).strip()

        search_wikipedia(query)

    elif "search" in command:

        query = command.replace(
            "search",
            ""
        ).strip()

        if query:
            google_search(query)
        else:
            speak("Please tell me what to search")

    elif any(word in command for word in ["bye", "exit", "stop"]):
        speak(f"Goodbye {USER_NAME}")
        return False

    else:
        speak("Sorry, I don't know that command yet")

    return True