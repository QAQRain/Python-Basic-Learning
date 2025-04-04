"""
File: StepUp.py
Name: QAQrain
------------------------
This file shows Karel picking up
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def m():
    move()

def tl():
    turn_left()

def tr():
    for i in range(3):
        turn_left()

def pick():
    pick_beeper()

def put():
    put_beeper()

def put_99():
    for i in range(99):
        put_beeper()

def main():
    move()
    pick_beeper()
    move()
    tl()
    move()
    tr()
    move()
    put_99()
    move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
