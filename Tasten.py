import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
def button_callback1(channel):
	global i
	i=1
	#time.sleep(20)
	print('inside')

def button_callback2(channel):
	global j
	if j==0:
		j=1
	else:
		j=0
	print("Button 2 was pushed!")
	
def button_callback3(channel):
	global k
	if k==0:
		k=1
	else:
		k=0
	print("Button 3 was pushed!")

i=0
j=0
k=0
	
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(8,GPIO.RISING,callback=button_callback1,bouncetime=200) # Setup event on pin 10 rising edge

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback2,bouncetime=200) # Setup event on pin 10 rising edge

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(12,GPIO.RISING,callback=button_callback3,bouncetime=200) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

while True:
  
  print(str(i))
  time.sleep(0.5)
