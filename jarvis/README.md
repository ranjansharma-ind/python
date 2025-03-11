# Jarvis - Personal AI Assistant

A Python-based AI assistant that can perform various computer tasks through voice commands, inspired by Iron Man's JARVIS.

## Features

- **Voice Recognition**: Understands and processes voice commands
- **Text-to-Speech**: Responds with natural voice output
- **System Control**: Can control computer functions (shutdown, restart, volume)
- **Time Management**: Provides time and date information
- **Application Control**: Can open applications
- **Web Integration**: Performs web searches
- **Screenshot Capability**: Takes and saves screenshots
- **Modern Architecture**: Uses type hints and clean code practices

## Available Commands

1. **"time"** - Get current time
2. **"date"** - Get current date
3. **"exit"** - Exit the program
4. **"shutdown"** - Shutdown the computer
5. **"restart"** - Restart the computer
6. **"open [app_name]"** - Open specified application
7. **"search [query]"** - Perform web search
8. **"volume [up/down/mute]"** - Control system volume
9. **"screenshot"** - Take a screenshot

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix/MacOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run Jarvis:
```bash
python src/jarvis.py
```

## Technical Details

- Uses SpeechRecognition for voice input
- pyttsx3 for text-to-speech output
- PyAudio for audio processing
- pyautogui for system control
- Modern Python features (type hints, pathlib)
- Clean architecture with modular design

## Project Structure

```
jarvis/
├── src/
│   └── jarvis.py       # Main implementation
├── utils/              # Utility functions
├── commands/           # Command implementations
├── requirements.txt    # Project dependencies
└── README.md          # Documentation
```

## Resume-Worthy Elements

- Voice Recognition Implementation
- System Automation
- Clean Code Architecture
- Type Annotations
- Error Handling
- Modern Python Practices
- Cross-platform Compatibility
- Modular Design 