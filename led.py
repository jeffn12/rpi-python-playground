from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(16)
count = 0

while True:
    print(count)
    button.when_pressed = led.on
    button.when_released = led.off
    count += 1