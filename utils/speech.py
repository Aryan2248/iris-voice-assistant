import os

def speak(text):
    print("IRIS:", text)
    os.system(f'say "{text}"')