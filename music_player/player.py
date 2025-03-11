import pygame
import os
import time

def play_music(file_path):
    # Initialize pygame mixer
    pygame.mixer.init()
    
    try:
        # Load and play the music file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        # Get the length of the audio file (in seconds)
        audio = pygame.mixer.Sound(file_path)
        duration = audio.get_length()
        
        print(f"Now playing: {os.path.basename(file_path)}")
        print("Press Ctrl+C to stop the music")
        
        # Keep the program running while the music plays
        while pygame.mixer.music.get_busy():
            time.sleep(1)
            
    except KeyboardInterrupt:
        # Handle the Ctrl+C interrupt
        print("\nStopping music playback...")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Clean up
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def main():
    print("Simple Music Player")
    print("-----------------")
    
    # Get the music file path from user
    file_path = input("Enter the path to your music file (mp3/wav): ")
    
    # Check if file exists
    if os.path.exists(file_path):
        play_music(file_path)
    else:
        print("Error: File not found!")

if __name__ == "__main__":
    main() 