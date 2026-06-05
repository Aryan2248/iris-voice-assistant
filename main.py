import datetime

from config import USER_NAME
from utils.speech import speak
from utils.listener import listen
from features.commands import process_command


def greet_user():
    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 12:
        speak(f"Good Morning {USER_NAME}")

    elif 12 <= current_hour < 17:
        speak(f"Good Afternoon {USER_NAME}")

    elif 17 <= current_hour < 21:
        speak(f"Good Evening {USER_NAME}")

    else:
        speak(f"Good Night {USER_NAME}")

    speak("IRIS is ready")


def main():

    greet_user()

    running = True

    while running:

        command = listen()

        if command:
            running = process_command(command)


if __name__ == "__main__":
    main()