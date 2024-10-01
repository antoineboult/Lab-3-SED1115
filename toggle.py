from machine import Pin
import time

led1 = Pin(18, Pin.OUT)
led2 = Pin(20, Pin.OUT)
led3 = Pin(16, Pin.OUT)
led4 = Pin(17, Pin.OUT)
led5 = Pin("LED", Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
sw4 = Pin(13, Pin.IN, Pin.PULL_DOWN)
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)
sw2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)


button1_old_value = False
button1_new_value = False


led2.off()
led3.off()
led4.off()
led5.off()
print("Starting...")

while True:

	button1_old_value = new_value
	button1_new_value = sw5.value()

	if new_value == 1 and old_value == 0:
		led1.toggle()
		print("Hello")
        time.sleep_ms(50)
