# Exercise 100 : Drink water notifier Second method

import pyttsx3
import time
from win10toast import ToastNotifier

REPEAT_INTERVAL = 10

engine = pyttsx3.init()
toast = ToastNotifier()

while True:
    engine.say("Hey Zahra, drink water")
    engine.runAndWait()
    toast.show_toast(
        "Drink Waterrr!",
        "It's time to drink water",
        duration=10,
        icon_path=None,  # You can specify an icon path here
        threaded=True
    )
    time.sleep(REPEAT_INTERVAL)
