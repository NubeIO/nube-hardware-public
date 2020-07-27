#!/usr/bin/python2.7
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.OUT)

print("ETH0 OFF")
GPIO.output(26, GPIO.LOW)
sleep(1)

print("ETH0 ON")
GPIO.output(26, GPIO.HIGH)
sleep(1)


GPIO.cleanup()

