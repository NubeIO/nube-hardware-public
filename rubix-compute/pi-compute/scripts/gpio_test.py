#!/usr/bin/python2.7
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.HIGH)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.HIGH)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.HIGH)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.HIGH)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.HIGH)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, GPIO.HIGH)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.HIGH)

print("USB_ON OFF")
GPIO.output(17, GPIO.LOW)
sleep(1)

print("MCU_ON OFF")
GPIO.output(12, GPIO.LOW)
sleep(1)

print("X1_ON OFF")
GPIO.output(13, GPIO.LOW)
sleep(1)

print("X2_ON OFF")
GPIO.output(16, GPIO.LOW)
sleep(1)

print("SER1_ON OFF")
GPIO.output(24, GPIO.LOW)
sleep(1)

print("SER2_ON OFF")
GPIO.output(22, GPIO.LOW)
sleep(1)

print("SER3_ON OFF")
GPIO.output(20, GPIO.LOW)
sleep(1)

print("SER4_ON OFF")
GPIO.output(18, GPIO.LOW)
sleep(1)

print("SER5_ON OFF")
GPIO.output(19, GPIO.LOW)
sleep(1)

print("SER6_ON OFF")
GPIO.output(21, GPIO.LOW)
sleep(1)

print("SER7_ON OFF")
GPIO.output(23, GPIO.LOW)
sleep(1)

print("SER8_ON OFF")
GPIO.output(25, GPIO.LOW)
sleep(1)

print("SER9_ON OFF")
GPIO.output(27, GPIO.LOW)
sleep(1)


print("USB_ON ON")
GPIO.output(17, GPIO.HIGH)
sleep(1)

print("MCU_ON ON")
GPIO.output(12, GPIO.HIGH)
sleep(1)

print("X1_ON ON")
GPIO.output(13, GPIO.HIGH)
sleep(1)

print("X2_ON ON")
GPIO.output(16, GPIO.HIGH)
sleep(1)

print("SER1_ON ON")
GPIO.output(24, GPIO.HIGH)
sleep(1)

print("SER2_ON ON")
GPIO.output(22, GPIO.HIGH)
sleep(1)

print("SER3_ON ON")
GPIO.output(20, GPIO.HIGH)
sleep(1)

print("SER4_ON ON")
GPIO.output(18, GPIO.HIGH)
sleep(1)

print("SER5_ON ON")
GPIO.output(19, GPIO.HIGH)
sleep(1)

print("SER6_ON ON")
GPIO.output(21, GPIO.HIGH)


print("SER7_ON ON")
GPIO.output(23, GPIO.HIGH)
sleep(1)

print("SER8_ON ON")
GPIO.output(25, GPIO.HIGH)
sleep(1)

print("SER9_ON ON")
GPIO.output(27, GPIO.HIGH)
sleep(1)


GPIO.cleanup()

