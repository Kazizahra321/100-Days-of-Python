# Exercise 96: Write a program to give shoutouts to people.

import pyttsx3
import time

def give_voice_shoutout(people):
    engine = pyttsx3.init(driverName='sapi5')

    for person in people:
        shoutout = f"Shoutout to {person}!"
        print(shoutout)
        engine.say(shoutout)
        engine.runAndWait()  # Wait for the current shoutout to finish

# List of people to shout out
people_list = ["Sarah", "Zahra", "Zikra"]

# Run the shoutout
give_voice_shoutout(people_list)
