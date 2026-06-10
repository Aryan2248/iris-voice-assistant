# IRIS - Intelligent Voice Assistant

IRIS is a Python-based voice assistant inspired by virtual AI assistants. It can understand voice commands, respond using speech synthesis, perform web searches, retrieve information from Wikipedia, and provide real-time weather updates for cities around the world.

## Features

* Voice recognition using SpeechRecognition
* Text-to-speech responses
* Personalized greetings based on time of day
* Open Google
* Open YouTube
* Google Search through voice commands
* Wikipedia search and summaries
* Real-time weather updates using OpenWeather API
* Current date and time announcements
* Personalized interaction
* Environment variable support using `.env`
* Modular and scalable project architecture

## Project Structure

```text
iris-voice-assistant/
│
├── main.py
├── config.py
├── .env
├── .gitignore
│
├── features/
│   ├── browser.py
│   ├── commands.py
│   ├── weather.py
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
* OpenWeather API
* Requests
* Python Dotenv
* WebBrowser Module
* Datetime Module

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Aryan2248/iris-voice-assistant.git
```

### 2. Navigate to the Project Directory

```bash
cd iris-voice-assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

## Run the Project

```bash
python main.py
```

## Example Commands

### General Commands

* "Hello"
* "What is your name?"
* "How are you?"
* "What is the time?"
* "What is today's date?"

### Browser Commands

* "Open Google"
* "Open YouTube"
* "Search Python programming"

### Knowledge Commands

* "Wikipedia Artificial Intelligence"
* "Wikipedia Alan Turing"

### Weather Commands

* "Weather in Dehradun"
* "What's the weather in Delhi"
* "Tell me the weather in London"
* "Weather in Tokyo"

### Exit Commands

* "Bye"
* "Exit"
* "Stop"

## Current Features

✅ Voice Recognition

✅ Text-to-Speech Responses

✅ Wikipedia Search

✅ Google Search

✅ Browser Automation

✅ Time and Date Information

✅ Real-Time Weather Updates

✅ Environment Variable Security

## Future Enhancements

* AI-powered conversations using Gemini/OpenAI
* Application launcher (VS Code, Chrome, Spotify)
* Reminder system
* News updates
* Email automation
* WhatsApp integration
* Battery and system monitoring
* Smart home integration
* GUI Dashboard
* Multi-language support

## Author

Aryan Yadav

## Current Status

### Version 1.1

IRIS currently supports voice commands, web search, Wikipedia integration, and real-time weather updates. The project is actively evolving toward a fully featured AI-powered virtual assistant.
