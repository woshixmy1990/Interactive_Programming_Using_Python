import simplegui
import random

guess=0
count=0
max_count=0



def input_guess(message):
    global guess
    guess = int(message)
    global count
    print "Guess was "+str(guess)
    if guess > secret_number and count<max_count:
        print "Higher"
        count+=1
    elif guess == secret_number and count<max_count:
        print "Correct"
        count+=1
    elif guess < secret_number and count<max_count:
        print "Lower"
        count+=1
    elif count==max_count:
        print "Out of guess"
    print ""


secret_number=0

# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number=random.randint(0,100)
    return secret_number


# define event handlers for control panel
def range100():    
    global secret_number
    secret_number=random.randint(0,100)
    global max_count
    max_count=7
    print "Secret number is in the range 0 to 100"
    return secret_number

def range1000():
    global secret_number
    secret_number=random.randint(0,1000)
    global max_count
    max_count=10
    print "Secret number is in the range 0 to 1000"
    return secret_number


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Guessing Game", 300, 200)
frame.add_input("Put Your Guess", input_guess,100)
frame.add_button("Range is [0,100)", range100,100)
frame.add_button("Range is [0,1000)", range1000,100)