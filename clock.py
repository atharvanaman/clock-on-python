import time
import os
import sys

def clear_screen():
    # Clear the terminal screen for different platforms
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def get_current_time():
    return time.strftime("%H:%M:%S")

def animated_clock():
    # Simple ASCII art for animation
    frames = [
        "oOoOoOoOoOo",
        "OoOoOoOoOoO",
        "oOoOoOoOoOo",
        "OoOoOoOoOoO"
    ]
    
    frame_count = len(frames)
    frame_delay = 0.2  # Delay between frames in seconds
    
    try:
        while True:
            for i in range(frame_count):
                clear_screen()
                print(frames[i])  # Print the animated frame
                print("\n")
                print("     ", get_current_time())  # Print the current time
                time.sleep(frame_delay)
    except KeyboardInterrupt:
        clear_screen()
        print("Clock stopped.")

if __name__ == "__main__":
    animated_clock()
