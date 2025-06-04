# Exercise 99 : Drink Water Reminder
# Write a python program which reminds you of drinking water every hour
# or two. Your program can either beep or send desktop notifications for
# a specific operating system.

import pyttsx3
import ctypes
import time

REPEAT_INTERVAL = 10 # will notify after every 10 secs, make it 3600 for 1hr

engine = pyttsx3.init()

while True:
    engine.say("Hey Zahra, drink water")
    engine.runAndWait()
    ctypes.windll.user32.MessageBoxW(0, "Hey Zahra, Drink water", "Alert", 0x40 | 0x1)
    time.sleep(REPEAT_INTERVAL)

