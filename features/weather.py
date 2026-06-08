import os
import requests

from dotenv import load_dotenv
from utils.speech import speak

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        print(data)

        if str(data.get("cod")) != "200":
            speak(data.get("message", "Weather lookup failed"))
            return

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        speak(
            f"Current weather in {city}. "
            f"Temperature is {round(temp)} degrees Celsius. "
            f"Condition is {description}. "
            f"It feels like {round(feels_like)} degrees. "
            f"Humidity is {humidity} percent."
        )

    except Exception as e:
        print("Weather Error:", e)
        speak("Unable to fetch weather information")