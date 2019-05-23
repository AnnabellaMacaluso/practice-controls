
from random import Random

from RPi._GPIO import *

IN = "Input"
OUT = "Output"

HIGH = 1
LOW = 0

BOARD = "Board Layout"
BCM = "BCM Layout"
mode = "UNDECLARED"

RISING = "Rising"
FALLING = "falling"

PUD_DOWN = "down"
PUD_UP = "up"

VERSION = '0.6.3'
RPI_INFO = "You silly billy, this isn't a raspberrypi"


def setmode(pinLayout):
    mode = pinLayout
    print("mode set")


def setup(channel, gpio_mode):
    print("Set up pin" + channel + " as an " + gpio_mode)


def setup(channel, gpio_mode, pull_up_down):
    print("Set up pin" + channel + " as an " + gpio_mode)


def setup(channel, gpio_mode, initial):
    print("Set up pin" + channel + " as an " + gpio_mode + " with initial value of " + initial)


def input(channel) -> bool:
    return bool(channel % 2)


def output(channel, high_or_low):
    print("set pin " + channel + " to " + high_or_low)


def cleanup():
    print("All clean!")


def cleanup(channel):
    print("cleaned " + channel)


def setwarnings(boolean):
    print("warnings are " + boolean)


def getmode():
    return mode


def add_event_detect(channel, rising_or_falling, callback, bouncetime):
    print("still gotta figure this one out")
