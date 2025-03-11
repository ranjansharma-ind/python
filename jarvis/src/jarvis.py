import speech_recognition as sr
import pyttsx3
import datetime
import os
import sys
from typing import Optional, Dict, Callable
from pathlib import Path

class Jarvis:
    def __init__(self):
        """Initialize Jarvis with speech recognition and text-to-speech capabilities"""
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Command registry with command variations
        self.commands: Dict[str, Dict] = {
            "time": {
                "function": self.get_time,
                "variations": ["what time", "current time", "time now", "tell me the time"]
            },
            "date": {
                "function": self.get_date,
                "variations": ["what date", "current date", "date today", "tell me the date", "what day"]
            },
            "exit": {
                "function": self.exit_program,
                "variations": ["quit", "stop", "bye", "goodbye", "exit program", "close"]
            },
            "shutdown": {
                "function": self.shutdown_computer,
                "variations": ["turn off computer", "shutdown computer", "power off"]
            },
            "restart": {
                "function": self.restart_computer,
                "variations": ["reboot", "restart computer", "reboot computer"]
            },
            "open": {
                "function": self.open_application,
                "variations": ["launch", "start", "run"]
            },
            "search": {
                "function": self.web_search,
                "variations": ["look up", "google", "find", "search for"]
            },
            "volume": {
                "function": self.control_volume,
                "variations": ["sound", "volume control", "adjust volume"]
            },
            "screenshot": {
                "function": self.take_screenshot,
                "variations": ["take screenshot", "capture screen", "screen capture"]
            },
            "help": {
                "function": self.show_help,
                "variations": ["what can you do", "show commands", "available commands", "help me"]
            }
        }
        
        # Startup message
        self.speak("Jarvis initialized and ready to assist you.")
        
    def show_help(self, _: str) -> None:
        """Show available commands"""
        help_text = "Here are the commands I understand:\n"
        help_text += "1. Ask for time: 'what time is it?'\n"
        help_text += "2. Ask for date: 'what date is it?'\n"
        help_text += "3. Open applications: 'open chrome'\n"
        help_text += "4. Search the web: 'search for cats'\n"
        help_text += "5. Control volume: 'volume up/down/mute'\n"
        help_text += "6. Take screenshot: 'take screenshot'\n"
        help_text += "7. Exit: 'goodbye' or 'exit'\n"
        self.speak(help_text)
        
    def speak(self, text: str) -> None:
        """Convert text to speech"""
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self) -> Optional[str]:
        """Listen for voice input and convert to text"""
        try:
            with self.microphone as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                
            print("Processing...")
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
            
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
            
    def process_command(self, command: str) -> None:
        """Process the voice command with improved natural language understanding"""
        if not command:
            return
            
        command = command.lower().strip()
        
        # Check for help command first
        if any(var in command for var in self.commands["help"]["variations"]):
            self.show_help("")
            return
            
        # Process other commands
        for cmd_key, cmd_info in self.commands.items():
            # Check if any variation of the command is in the user's speech
            matched_variation = None
            for var in cmd_info["variations"]:
                if var in command:
                    matched_variation = var
                    break
                    
            if matched_variation or cmd_key in command:
                # Handle commands that need parameters
                if cmd_key in ["open", "search", "volume"]:
                    # Extract the parameter after the command word
                    param = ""
                    if matched_variation:
                        parts = command.split(matched_variation, 1)
                        if len(parts) > 1:
                            param = parts[1].strip()
                    else:
                        parts = command.split(cmd_key, 1)
                        if len(parts) > 1:
                            param = parts[1].strip()
                            
                    if param:
                        cmd_info["function"](param)
                        return
                    else:
                        self.speak(f"Please specify what you want me to {cmd_key}")
                        return
                else:
                    # Execute commands that don't need parameters
                    cmd_info["function"]("")
                    return
                    
        self.speak("I'm not sure what you want me to do. Say 'help' to see available commands.")
        
    def get_time(self, _: str) -> None:
        """Tell the current time"""
        time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {time}")
        
    def get_date(self, _: str) -> None:
        """Tell the current date"""
        date = datetime.datetime.now().strftime("%B %d, %Y")
        self.speak(f"Today is {date}")
        
    def exit_program(self, _: str) -> None:
        """Exit the program"""
        self.speak("Goodbye!")
        sys.exit()
        
    def shutdown_computer(self, _: str) -> None:
        """Shutdown the computer"""
        self.speak("Shutting down the computer")
        os.system("shutdown /s /t 30")
        
    def restart_computer(self, _: str) -> None:
        """Restart the computer"""
        self.speak("Restarting the computer")
        os.system("shutdown /r /t 30")
        
    def open_application(self, app_name: str) -> None:
        """Open a specified application"""
        try:
            os.startfile(app_name)
            self.speak(f"Opening {app_name}")
        except FileNotFoundError:
            self.speak(f"Sorry, I couldn't find {app_name}")
            
    def web_search(self, query: str) -> None:
        """Perform a web search"""
        import webbrowser
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        self.speak(f"Searching for {query}")
        
    def control_volume(self, command: str) -> None:
        """Control system volume"""
        import pyautogui
        if "up" in command:
            pyautogui.press("volumeup", 5)
            self.speak("Volume increased")
        elif "down" in command:
            pyautogui.press("volumedown", 5)
            self.speak("Volume decreased")
        elif "mute" in command:
            pyautogui.press("volumemute")
            self.speak("Volume muted")
            
    def take_screenshot(self, _: str) -> None:
        """Take a screenshot"""
        import pyautogui
        screenshot_dir = Path.home() / "Pictures" / "Screenshots"
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = screenshot_dir / f"screenshot_{timestamp}.png"
        
        pyautogui.screenshot(str(screenshot_path))
        self.speak("Screenshot taken and saved")
        
    def run(self) -> None:
        """Main loop to continuously listen for commands"""
        self.speak("How can I help you?")
        
        while True:
            command = self.listen()
            if command:
                self.process_command(command)

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run() 