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
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(buzzer_pin, GPIO.OUT) # Set buzzer_pin's mode to output
pwm = GPIO.PWM(buzzer_pin,50) # Set buzzer_pin's frequency to 50Hz
pwm.start(0) # Start PWM with 0% duty cycle
pwm.ChangeDutyCycle(0) # Change the duty cycle to 0%
# Define the melody as a list of notes and their durations
cat = [("C", 0.25), ("F", 0.25), ("A", 0.5)] # C, F, A
dog = [("C", 0.25), ("D", 0.25), ("E", 0.5),] # C, D, E

# Define the frequency of each note
note_freq = {"C": 600, "D": 294, "E": 329, "F": 670, "G": 392, "A": 800, "B": 493, "X": 600}

# Define the function to play a single note
def play_note(note, duration): # note is a string, duration is a float
    freq = note_freq[note] # Get the frequency of the note
    if freq == 0: # If the note is a rest
        time.sleep(duration) # Wait for the duration of the rest
        return # And stop playing the note
    period = 1 / freq # Calculate the time for one wave
    delay = period / 2 # Calculate the time for half of the wave
    cycles = int(duration * freq) # Calculate the number of waves to produce the duration of the note
    for i in range(cycles): # Produce the waves
        GPIO.output(buzzer_pin, GPIO.HIGH) # Set buzzer_pin to high
        time.sleep(delay) # Wait for half of the wave
        GPIO.output(buzzer_pin, GPIO.LOW) # Set buzzer_pin to low
        time.sleep(delay) # Wait for half of the wave
    pwm.ChangeDutyCycle(0) # Change the duty cycle to 0%

    
    

# Play the melody

# Clean up

GPIO.setup(11, GPIO.OUT) # Set buzzer_pin's mode to output
GPIO.setup(13, GPIO.OUT) # Set buzzer_pin's mode to output

left_servo = GPIO.PWM(11, 50) # Set buzzer_pin's frequency to 50Hz
right_servo = GPIO.PWM(13, 50) # Set buzzer_pin's frequency to 50Hz
left_servo.start(0) # Start PWM with 0% duty cycle
right_servo.start(0) # Start PWM with 0% duty cycle

def set_angle(servo, angle): # note is a string, duration is a float
	duty = angle / 18 + 2 # Get the frequency of the note
	servo.ChangeDutyCycle(duty) # If the note is a rest
	time.sleep(0.5) # Wait for the duration of the rest
	servo.ChangeDutyCycle(0) # And stop playing the note                                
app = Flask(__name__) # Create a new Flask app instance
dog_activated = dict() # Create a dictionary to store the activated dogs
cat_activated = dict() # Create a dictionary to store the activated cats
dogtimer = [] # Create a list to store the activated dogs
cattimer = [] # Create a list to store the activated cats
def Timer(): # Define the function to play a single note
    while True: # note is a string, duration is a float
        time.sleep(3) # Get the frequency of the note
        global dogtimer # If the note is a rest
        global cattimer # Wait for the duration of the rest
        for time1 in dogtimer: # And stop playing the note
            if time.time() > time1[0]: # note is a string, duration is a float
                for note, duration in dog: # Get the frequency of the note
                    play_note(note, duration) # If the note is a rest
                print("served dog") # Wait for the duration of the rest
                set_angle(right_servo,100) # And stop playing the note
                time.sleep(time1[1]) # note is a string, duration is a float
                set_angle(right_servo,10) # Get the frequency of the note
                time.sleep(time1[1]) # If the note is a rest
                dogtimer.remove(time1) # Wait for the duration of the rest
				
        for time1 in cattimer: # And stop playing the note
            if time.time() > time1[0]:  # note is a string, duration is a float
                for note, duration in cat: # Get the frequency of the note
                    play_note(note, duration) # If the note is a rest
                print("served cat") # Wait for the duration of the rest
                set_angle(left_servo,70) # And stop playing the note
                time.sleep(time1[1]) # note is a string, duration is a float
                set_angle(left_servo,10) # Get the frequency of the note
                time.sleep(time1[1]) # If the note is a rest
                cattimer.remove(time1) # Wait for the duration of the rest
				

       
       

@app.route('/', methods=['POST'])
 # Create a route for the default URL, which is going to be handled by a function
def handle_request():
    global dogtimer
    global cattimer
    print(time.time())
    data = request.json
    print(data)
    if data['request'] == 'dog' or data['request'] == 'cat': # If the request is 'dog' or 'cat'
        # Forward the request to the Pico W
        # response = requests.get('http://pico-w-address/' + data['request'])
        response = "nice"
        return "test"
    elif data['request'] == 'Left': # If the request is 'left' or 'right'
        for note, duration in dog: # Play the melody
            play_note(note, duration)
        set_angle(left_servo,70)
        time.sleep(2)
        set_angle(left_servo,10)
        time.sleep(2)
        return "Cat is fed"
    elif data['request'] == "Right": # If the request is 'left' or 'right'
        for note, duration in cat:
            play_note(note, duration) # Play the melody
        set_angle(right_servo,100)
        time.sleep(2)
        set_angle(right_servo,10)
        time.sleep(2)
        return "Dog is Fed "
    elif data['request'] == 'feed-data': # If the request is 'left' or 'right'
        for timer in data['Dog']['times']:
            if timer is not None and timer > 0:
                dogtimer.append([time.time() + timer, data['Dog']['portionSize']]) #configure the timer
        for timer in data['Cat']['times']:
            if timer is not None and timer > 0:
               cattimer.append([time.time() + timer,  data['Cat']['portionSize']]) #configure the timer
        return "dog is activated"

    elif data['request'] == "Cancel-Cat": # If the request is to cancel the timer
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
