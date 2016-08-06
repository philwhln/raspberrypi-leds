import RPi.GPIO as GPIO
import time
from sys import stdout

ON = 'on'
OFF = 'off'
RED = 'red'
GREEN = 'green'
YELLOW = 'yellow'

ports = {
  RED: 33,
  YELLOW: 37,
  GREEN: 36
}

colors = {
  RED: 'red',
  YELLOW: 'yellow',
  GREEN: 'green'
}

states = {
  OFF: GPIO.LOW,
  ON: GPIO.HIGH
}

GPIO.setmode(GPIO.BOARD)
for color in [RED, YELLOW, GREEN]:
    GPIO.setup(ports[color], GPIO.OUT)

def color_state(color, state):
    print('{} {}'.format(color, state))
    GPIO.output(ports[color], states[state])

try:
    while True:
        for color in [RED, YELLOW, GREEN, YELLOW]:
            color_state(color, ON)
            time.sleep(0.5)
            color_state(color, OFF)
            time.sleep(0.1)

except KeyboardInterrupt:
    print('Abort requested')

for color in [RED, YELLOW, GREEN]:
    color_state(color, OFF)
