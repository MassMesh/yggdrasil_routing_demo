#! /usr/bin/python3
from gpiozero import LED
from time import sleep
import psutil

def flash_short(led):
    led.on()
    led.off()

def flash_long(led):
    led.on()
    sleep(5)
    led.off()
    sleep(1)

def ident(pin):
    led = LED(pin)
    sleep(3)
    flash_long(led)
    i=0
    while i < 5:
        flash_short(led)
        i+=1

ident(21)
