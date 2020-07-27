#!/usr/bin/python2.7
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)

print("MCU Reset")
GPIO.output(12, GPIO.LOW)
sleep(1)

print("MCU Restarted")
GPIO.output(12, GPIO.HIGH)
sleep(1)


GPIO.cleanup()

