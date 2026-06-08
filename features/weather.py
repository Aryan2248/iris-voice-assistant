import requests
from utils.speech import speak

API_KEY = "bc3516a21be947b42607eac36212b100"


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        if str[data.get("cod")] != 200:
            print(data)
            speak(data.get("message", "Weather lookup failed"))
            return

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]

        speak(
            f"In {city}, it is {temp} degrees Celsius "
            f"with {description}. "
            f"It feels like {feels_like} degrees."
        )

    except Exception:
        speak("Unable to fetch weather information")