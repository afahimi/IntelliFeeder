import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

left_servo = GPIO.PWM(11, 50)
right_servo = GPIO.PWM(13, 50)
left_servo.start(0)
right_servo.start(0)
def set_angle(servo, angle):
	duty = angle / 18 + 2
	servo.ChangeDutyCycle(duty)
	time.sleep(0.5)
	servo.ChangeDutyCycle(0)                                   

while True:
	direction = input("Enter Left or Right: ")
	if direction == "Left":
		set_angle(left_servo,90)
		time.sleep(1)
		set_angle(left_servo,0)
		time.sleep(1)
	elif direction == "Right":
		set_angle(right_servo,90)
		time.sleep(1)
		set_angle(right_servo,0)
		time.sleep(1)
	else:
		print("Invlid Input: Enter Left or Right")

left_servo.stop()
right_servo.stop()
GPIO.cleanup()
