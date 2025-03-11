import pygame
import os
import time
from pytube import YouTube
from youtubesearchpython import VideosSearch
import tempfile
import shutil

def setup_youtube():
    """Configure YouTube with necessary headers"""
    import pytube.innertube
    pytube.innertube._headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

def search_youtube(query):
    """Search for a video on YouTube"""
    try:
        # Create VideosSearch instance
        videos_search = VideosSearch(query, limit=5)
        results = videos_search.result().get('result', [])
        
        if not results:
            print("No videos found!")
            return None
            
        # Display search results
        print("\nFound these videos:")
        for i, video in enumerate(results, 1):
            duration = video.get('duration', 'Unknown duration')
            title = video.get('title', 'Unknown title')
            print(f"{i}. {title} ({duration})")
            
        # Let user choose a video
        while True:
            try:
                choice = input("\nEnter the number of the video you want to play (1-5) or 'q' to quit: ")
                if choice.lower() == 'q':
                    return None
                    
                choice = int(choice)
                if 1 <= choice <= len(results):
                    return results[choice-1].get('link')
                else:
                    print("Please enter a valid number!")
            except ValueError:
                print("Please enter a valid number or 'q' to quit!")
                
    except Exception as e:
        print(f"Error searching YouTube: {str(e)}")
        return None

def download_youtube_audio(url, output_path):
    """Download audio from YouTube video"""
    try:
        # Create a YouTube object with custom parameters
        yt = YouTube(
            url,
            use_oauth=True,
            allow_oauth_cache=True
        )
        
        # Get the audio stream (trying different options)
        audio_stream = (
            yt.streams
            .filter(only_audio=True, file_extension='mp4')
            .order_by('abr')
            .desc()
            .first()
        )
        
        if not audio_stream:
            print("No suitable audio stream found")
            return None, None
            
        # Download the audio
        print(f"\nDownloading: {yt.title}")
        audio_file = audio_stream.download(output_path=output_path)
        
        # Rename the file to have .mp3 extension
        base, _ = os.path.splitext(audio_file)
        new_file = base + '.mp3'
        os.rename(audio_file, new_file)
        
        return new_file, yt.title
        
    except Exception as e:
        print(f"Error downloading YouTube video: {str(e)}")
        return None, None

def play_music(file_path, title):
    """Play the downloaded audio file"""
    # Initialize pygame mixer
    pygame.mixer.init()
    
    try:
        # Load and play the music file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        print(f"\nNow playing: {title}")
        print("Press Ctrl+C to stop the music")
        
        # Keep the program running while the music plays
        while pygame.mixer.music.get_busy():
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping music playback...")
    except Exception as e:
        print(f"Error playing music: {str(e)}")
    finally:
        # Clean up
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def main():
    print("YouTube Music Player")
    print("-------------------")
    print("You can enter either a YouTube URL or a search term")
    print("Press Ctrl+C to stop the current song")
    
    # Setup YouTube with proper headers
    setup_youtube()
    
    # Create a temporary directory for downloads
    temp_dir = tempfile.mkdtemp()
    
    try:
        while True:
            try:
                # Get input from user
                query = input("\nEnter YouTube URL or search term (or 'quit' to exit): ")
                
                if query.lower() == 'quit':
                    break
                
                # Check if input is a URL or search term
                if 'youtube.com' in query or 'youtu.be' in query:
                    url = query
                else:
                    url = search_youtube(query)
                
                if url:
                    # Download and play the audio
                    audio_file, title = download_youtube_audio(url, temp_dir)
                    if audio_file and title:
                        play_music(audio_file, title)
                
                # Ask if user wants to play another song
                choice = input("\nDo you want to play another song? (y/n): ")
                if choice.lower() != 'y':
                    break
                    
            except KeyboardInterrupt:
                print("\nStopping current song...")
                continue
                
    finally:
        # Clean up: remove temporary directory and its contents
        try:
            shutil.rmtree(temp_dir)
        except Exception as e:
            print(f"Error cleaning up temporary files: {str(e)}")

if __name__ == "__main__":
    main() 