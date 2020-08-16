from gpiozero import LED, Button
from time import sleep

led = LED(17)
count = 0

while count < 5:
    print(count)
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    count += 1