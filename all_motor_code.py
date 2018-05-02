import RPi.GPIO as GPIO
from time import sleep

# setting it as board mode
GPIO.setmode(GPIO.BOARD)

# to suppress the warnings
GPIO.setwarnings(False)

# setting pin 7 as output pin
GPIO.setup(12, GPIO.OUT)


# intializing pwm on pin 7 with 50 Hz
pwm = GPIO.PWM(12, 50)

# Reading the input from the_data file inside /home/pi

with  open('/home/pi/the_data','r') as f:
        value = f.readline()
        value = value.split('(')[0].strip()

if not value is None:

	# The values that it accepts are between 3-11
	pwm.start(5)

	try:
		if value == 'apple':
			pwm.ChangeDutyCycle(3)

		elif value == 'book':
			pwm.ChangeDutyCycle(5)
		
		elif value == 'smartphone':
			pwm.ChangeDutyCycle(7)
		
		elif value == 'pen':
			pwm.ChangeDutyCycle(9)
			
		else:
			# Else statement can be fixed onto the water bottle
			pwm.ChangeDutyCycle(11)			
	
			# For first motor
		GPIO.setup(03, GPIO.OUT)
		GPIO.setup(05, GPIO.OUT)
		GPIO.setup(07, GPIO.OUT)
		
		# For second motor
		GPIO.setup(11, GPIO.OUT)
		GPIO.setup(13, GPIO.OUT)
		GPIO.setup(15, GPIO.OUT)

		pwm1 = GPIO.PWM(07, 100)
		pwm2 = GPIO.PWM(15, 100)

		pwm1.start(0)
		pwm2.start(0)

		GPIO.output(03, True)
		GPIO.output(05, False)

		GPIO.output(11, False)
		GPIO.output(13, True)


		pwm1.ChangeDutyCycle(50)
		pwm2.ChangeDutyCycle(50)


		GPIO.output(07, True)
		GPIO.output(15, True)

		sleep(2)

		# GPIO.output(07,False)

		# GPIO.output(03, False)
		# GPIO.output(05, True)

		# sleep(3)

		# GPIO.output(07, True)

		pwm1.stop()
		pwm2.stop()

	except KeyboardInterrupt:
			GPIO.cleanup()








