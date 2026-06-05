import speech_recognition as sr
import os
import datetime
import webbrowser
import wikipedia


def speak(text):
    print("Jarvis:", text)
    os.system(f'say "{text}"')


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source, duration=2)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            command = recognizer.recognize_google(audio)
            command = command.lower()

            print("You:", command)
            return command

        except sr.WaitTimeoutError:
            print("No speech detected")
            return ""

        except Exception:
            print("Could not understand")
            return ""


def process_command(command):

    # Greetings
    if any(word in command for word in ["hello", "hi", "hey"]):
        speak("Hello Aryan")

    # How are you
    elif "how" in command:
        speak("I am doing great. How can I help you?")

    # Name
    elif "name" in command:
        speak("My name is Jarvis")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # Date
    elif "date" in command:
        today = datetime.date.today().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    # Open Google
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Wikipedia Search
    elif "wikipedia" in command:

        query = command.replace("wikipedia", "").strip()

        if query:
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

        else:
            speak("Please tell me what to search on Wikipedia")

    # Search Google
    elif "search" in command:

        query = command.replace("search", "").strip()

        if query:
            speak(f"Searching for {query}")

            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

        else:
            speak("Please tell me what to search")

    # Exit
    elif any(word in command for word in ["bye", "exit", "stop"]):
        speak("Goodbye Aryan")
        return False

    else:
        speak("Sorry, I don't know that command yet")

    return True


# Startup Greeting
hour = datetime.datetime.now().hour

if hour < 12:
    speak("Good Morning Aryan")

elif hour < 18:
    speak("Good Afternoon Aryan")

else:
    speak("Good Evening Aryan")

speak("Jarvis is ready")


# Main Loop
running = True

while running:

    command = listen()

    if command:
        running = process_command(command)