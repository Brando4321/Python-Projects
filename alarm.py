from pydub import AudioSegment
from pydub.playback import play
import time

# ANSI Characters/ Escape Sequences
# Clears the entire terminal screen
CLEAR= "\033[2J"
# Return the cursor to the home position
CLEAR_AND_RETURN= "\033[H"
# 


def alarm(seconds):
    time_elapsed= 0

    print(CLEAR)
    while time_elapsed <seconds:
        time.sleep(1)
        time_elapsed+=1

        time_left= seconds-time_elapsed
        minutes_left= time_left //60     # Actual division
        seconds_left= time_left % 60     #% Gives remainder after division

        print(f"{CLEAR_AND_RETURN}Alarm wil sound in: {minutes_left:02}:{seconds_left:02}")
    
minutes= int(input("How many minutes to wait: "))
seconds= int(input("How many seconds to wait: "))
total_seconds= minutes * 60 + seconds


alarm(total_seconds)

