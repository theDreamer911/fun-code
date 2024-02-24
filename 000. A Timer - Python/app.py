import time
import subprocess

def timer(seconds, sound_file):
    print(f"Timer set for {seconds} seconds.")
    time.sleep(seconds)
    
    subprocess.run(["start", "powershell", "(New-Object Media.SoundPlayer '{}').PlaySync()".format(sound_file)], shell=True)
    
    print("Timer complete!")

duration = int(input("Enter the duration of the timer in seconds: "))

sound_file = "alarm.wav"

timer(duration, sound_file)
