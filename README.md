# Simple Music Player

A simple Python music player that can play audio files (MP3 and WAV formats).

## Requirements
- Python 3.x
- pygame library

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the player script:
```bash
python music_player/player.py
```

2. When prompted, enter the full path to your music file (MP3 or WAV format).

3. The music will start playing. Press Ctrl+C to stop the playback.

## Features
- Plays MP3 and WAV audio files
- Simple command-line interface
- Shows currently playing track
- Easy to stop playback with Ctrl+C

## Note
Make sure you have the audio file path ready before running the program. The file path can be absolute or relative to the current directory. 