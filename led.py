from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(16)

button.wait_for_press()
print("pressed")


