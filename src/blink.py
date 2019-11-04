#! /usr/bin/python3
from gpiozero import LED
from time import sleep
import psutil

def blink(pin, interval):
    led = LED(pin)
    counters = psutil.net_io_counters()
    bytes = counters.bytes_sent + counters.bytes_recv
    while True:
        counters = psutil.net_io_counters()
        newbytes = counters.bytes_sent + counters.bytes_recv
        if (newbytes - bytes > 20000000):
          led.on()
        else:
          led.off()
        bytes = newbytes
        sleep(1)

blink(26, 1)
