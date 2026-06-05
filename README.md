# IRIS - Intelligent Voice Assistant

IRIS is a Python-based voice assistant that listens to voice commands and performs various tasks such as web searches, opening websites, providing time and date information, and retrieving information from Wikipedia.

## Features

* Voice recognition using SpeechRecognition
* Text-to-speech responses
* Greeting system based on time of day
* Open Google
* Open YouTube
* Google Search through voice commands
* Wikipedia search and summaries
* Current date and time announcements
* Personalized interaction
* Modular project structure for easy scalability

## Project Structure

```text
iris-voice-assistant/
│
├── main.py
├── config.py
│
├── features/
│   ├── browser.py
│   ├── commands.py
│   └── wikipedia_search.py
│
├── utils/
│   ├── listener.py
│   └── speech.py
│
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* SpeechRecognition
* Wikipedia API
* WebBrowser Module
* Datetime Module

## Installation

1. Clone the repository

```bash
git clone https://github.com/Aryan2248/iris-voice-assistant.git
```

2. Navigate to the project directory

```bash
cd iris-voice-assistant
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Example Commands

* "Hello"
* "What is your name?"
* "What is the time?"
* "What is today's date?"
* "Open Google"
* "Open YouTube"
* "Search Python programming"
* "Wikipedia Artificial Intelligence"
* "Bye"

## Future Enhancements

* Weather updates
* AI-powered conversations
* Email sending
* Reminder system
* News updates
* WhatsApp integration
* Application launcher
* Smart home integration
* GUI Dashboard
* OpenAI/Gemini integration

## Author

Aryan Yadav

### Current Status

Version 1.0

IRIS currently supports voice recognition, web search, Wikipedia integration, and basic assistant functionalities. The project is being actively developed with plans to evolve into a full-featured AI voice assistant.
