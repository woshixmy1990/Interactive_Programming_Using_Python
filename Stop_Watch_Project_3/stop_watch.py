# template for "Stopwatch: The Game"
import simplegui
# define global variables
message="0:00.0"
started=False
game_count=0
time=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global message
    hour=t/600
    min=(t-600*hour)/10
    sec=t-600*hour-min*10
    if min<10:
        message=str(hour)+":"+"0"+str(min)+"."+str(sec)
    elif min>=10:
        message=str(hour)+":"+str(min)+"."+str(sec)
    return message
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def check_start():
    global started    
    started = True
    timer.start()

    
def stop_button():
    global started
    global game_count
    timer.stop()
    started = False
    game_count+=1

def reset():
    global started
    global time
    global message
    message="0:00.0"
    started = True
    game_count=0
    timer.stop()
    time=0
 


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    format(time)

# define draw handler
def draw(canvas):
    canvas.draw_text(message, (100,100), 36, "Red")
    canvas.draw_text("0" + " / " + str(game_count),(250,20), 24, "Green")
# create frame
frame = simplegui.create_frame("stop watch", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
current_timer = simplegui.create_timer(1, check_start)
frame.add_button("Start", check_start, 75)
frame.add_button("Stop", stop_button, 75)
frame.add_button("Reset", reset, 75)

# start frame
frame.start()


# Please remember to review the grading rubric
