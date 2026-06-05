import speech_recognition as sr

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