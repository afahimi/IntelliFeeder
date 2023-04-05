from flask import Flask, request
import time
import requests
import RPi.GPIO as GPIO
from threading import Thread
GPIO.setmode(GPIO.BOARD)
import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
buzzer_pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer_pin, GPIO.OUT)
pwm = GPIO.PWM(buzzer_pin,50)
pwm.start(0)
pwm.ChangeDutyCycle(0)
# Define the melody as a list of notes and their durations
cat = [("C", 0.25), ("F", 0.25), ("A", 0.5)]
dog = [("C", 0.25), ("D", 0.25), ("E", 0.5),]

# Define the frequency of each note
note_freq = {"C": 600, "D": 294, "E": 329, "F": 670, "G": 392, "A": 800, "B": 493, "X": 600}

# Define the function to play a single note
def play_note(note, duration):
    freq = note_freq[note]
    if freq == 0:
        time.sleep(duration)
        return
    period = 1 / freq
    delay = period / 2
    cycles = int(duration * freq)
    for i in range(cycles):
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(delay)
    pwm.ChangeDutyCycle(0)

    
    

# Play the melody

# Clean up

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
dog_activated = dict()
cat_activated = dict()
dogtimer = []
cattimer = []
def Timer():
    while True:
        time.sleep(3)
        global dogtimer
        global cattimer
        for time1 in dogtimer:
            if time.time() > time1[0]:
                for note, duration in dog:
                    play_note(note, duration)
                print("served dog")
                set_angle(right_servo,10)
                time.sleep(time1[1])
                set_angle(right_servo,100)
                time.sleep(time1[1])
                dogtimer.remove(time1)
				
        for time1 in cattimer:
            if time.time() > time1[0]:
                for note, duration in cat:
                    play_note(note, duration)
                print("served cat")
                set_angle(left_servo,70)
                time.sleep(time1[1])
                set_angle(left_servo,10)
                time.sleep(time1[1])
                cattimer.remove(time1)
				

       
       

@app.route('/', methods=['POST'])

def handle_request():
    global dogtimer
    global cattimer
    print(time.time())
    data = request.json
    print(data)
    if data['request'] == 'dog' or data['request'] == 'cat':
        # Forward the request to the Pico W
        # response = requests.get('http://pico-w-address/' + data['request'])
        response = "nice"
        return "test"
    elif data['request'] == 'Left':
        for note, duration in dog:
            play_note(note, duration)
        set_angle(left_servo,70)
        time.sleep(1)
        set_angle(left_servo,10)
        time.sleep(1)
        return "Cat is fed"
    elif data['request'] == "Right":
        for note, duration in cat:
            play_note(note, duration)
        set_angle(right_servo,10)
        time.sleep(1)
        set_angle(right_servo,100)
        time.sleep(1)
        return "Dog is Fed "
    elif data['request'] == 'feed-data':
        for timer in data['Dog']['times']:
            if timer is not None:
                dogtimer.append([time.time() + timer, data['Dog']['portionSize']])
        for timer in data['Cat']['times']:
            if timer is not None:
               cattimer.append([time.time() + timer,  data['Cat']['portionSize']])
        return "dog is activated"

    elif data['request'] == "Cancel-Cat":
        cattimer = []
        return "Cat is cancelled"
    elif data['request'] == "Cancel-Dog":
       dogtimer = []
       return "Dog is cancelled"
        
    else:
        print("hello there")
        print(data['request'] == "Left")
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

    app.run(host="192.168.137.172", debug=True, port=5000)
