from flask import Flask, request
import time
import requests
import RPi.GPIO as GPIO
from threading import Thread
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
app = Flask(__name__)
dog_activated = False
cat_activated = False
dogtimer = 0
cattimer = 0
def Timer():
    while True:
        global dog_activated
        global dogtimer
        global cat_activated
        global cattimer
        time.sleep(5)
        if dog_activated and time.time() > dogtimer:
            set_angle(left_servo,90)
            time.sleep(1)
            set_angle(left_servo,0)
            time.sleep(1)
            dog_activated = False
        
        if cat_activated and time.time() > cattimer:
            set_angle(right_servo,90)
            time.sleep(1)
            set_angle(right_servo,0)
            time.sleep(1)
            cat_activated = False
       
       

@app.route('/', methods=['POST'])

def handle_request():
    global dog_activated
    global dogtimer
    global cat_activated
    global cattimer
        
    data = request.json
    print(data)
    print(data['request'])
    if data['request'] == 'dog' or data['request'] == 'cat':
        # Forward the request to the Pico W
        # response = requests.get('http://pico-w-address/' + data['request'])
        response = "nice"
        return "test"
    elif data['request'] == 'Left':
        set_angle(left_servo,90)
        time.sleep(1)
        set_angle(left_servo,0)
        time.sleep(1)
        return "Cat is fed"
    elif data['request'] == "Right":
        set_angle(right_servo,90)
        time.sleep(1)
        set_angle(right_servo,0)
        time.sleep(1)
        return "Dog is Fed "
    elif len(data['request']) >= 10 and data['request'][:10] == "Dog-Timer:":
        dogtimer = int(data['request'][10:]) + time.time()
        dog_activated = True
        return "dog is activated"
    elif len(data['request']) >= 10 and data['request'][:10] == "Cat-Timer:":
        cattimer = int(data['request'][10:]) + time.time()
        cat_activated = True
        return "cat is activated"
    elif data['request'] == "Cancel-Cat":
        cat_activated = False
        return "Cat is cancelled"
    elif data['request'] == "Cancel-Dog":
       dog_activated = False
       return "Dog is cancelled"
        
    else:
        print("hello there")
        print(data['request'] == "Left")
        print(f"{len(data['request'])} {data['request']}")
        print(data['request'][0])
        return 'Invalid request'


    """
    if data['request'] == 'dog' or data['request'] == 'cat':
        # Forward the request to the Pico W
        response = requests.get('http://pico-w-address/' + data['request'])
        return response.text
    
    """
    # elif data['request'] == 'timer':
    #     # Countdown for the timer length and then send a dog or cat request
    #     timer_length = data['length']
    #     time.sleep(timer_length)
    #     response = requests.get('http://pico-w-address/' + ['dog', 'cat'][int(time.time() % 2 == 0)])
    #     return response.text
    

if __name__ == '__main__':
    background_thread = Thread(target = Timer)
    background_thread.start()

    app.run(host="192.168.137.10", debug=True, port=5000)
