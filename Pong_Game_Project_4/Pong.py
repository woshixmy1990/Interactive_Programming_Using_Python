# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH/2, HEIGHT/2] 
ball_vel = [0,1] 
# initialize paddle_pos and paddle_vel for paddles
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2
paddle1_vel=1
paddle2_vel=1
score1=0
score2=0


# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_vel[0] = -random.randrange(120,240)/100   
    if direction == True: 
        ball_vel[0] *= -1 
    ball_vel[1] = -random.randrange(60, 180)/100
    ball_pos = [WIDTH/2, HEIGHT/2]
 

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2
    paddle1_vel=0
    paddle2_vel=0
    score1=0
    score2=0
    spawn_ball(0)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, score1, score2
    global paddle1_vel,paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    
    #check the ball hit the gutter or bottom and upper and rebounce
    if ball_pos[0] <= (BALL_RADIUS  + PAD_WIDTH) or ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):        
        ball_vel[0] *= -1
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos >= HALF_PAD_HEIGHT and paddle1_vel < 0) or (paddle1_pos <= HEIGHT-HALF_PAD_HEIGHT and paddle1_vel > 0) :
        paddle1_pos += paddle1_vel    
    elif (paddle2_pos >= HALF_PAD_HEIGHT and paddle2_vel < 0) or (paddle2_pos <= HEIGHT-HALF_PAD_HEIGHT and paddle2_vel > 0) :
        paddle2_pos += paddle2_vel  

     
    
    # draw paddles
    canvas.draw_polygon([[0, (paddle1_pos-HALF_PAD_HEIGHT)], [PAD_WIDTH, (paddle1_pos-HALF_PAD_HEIGHT)],
                         [PAD_WIDTH, (paddle1_pos + HALF_PAD_HEIGHT) ],[0, (paddle1_pos + HALF_PAD_HEIGHT)]],1,"white","white")
    canvas.draw_polygon([[(WIDTH-PAD_WIDTH), (paddle2_pos-HALF_PAD_HEIGHT)], [WIDTH, (paddle2_pos-HALF_PAD_HEIGHT)],
                         [WIDTH, (paddle2_pos + HALF_PAD_HEIGHT) ],[(WIDTH-PAD_WIDTH), (paddle2_pos + HALF_PAD_HEIGHT)]],1,"white","white")
    # determine whether paddle and ball collide   
    if (ball_pos[0] <= PAD_WIDTH+BALL_RADIUS):             
        if (ball_pos[1] < (paddle1_pos-HALF_PAD_HEIGHT)) or (ball_pos[1] > (paddle1_pos + HALF_PAD_HEIGHT)):
            score2 += 1
            spawn_ball(RIGHT)
        else: 
            ball_vel[0] += 0.1*ball_vel[0]
           
            
    elif (ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS):
        if (ball_pos[1] < (paddle2_pos-HALF_PAD_HEIGHT)) or (ball_pos[1] > (paddle2_pos + HALF_PAD_HEIGHT)):
            score1 += 1 
            spawn_ball(LEFT)
        else: 
            ball_vel[0] += 0.1*ball_vel[0]
     
    
    
    
    # draw scores
    canvas.draw_text(str(score1), (200,100), 32, 'white') 
    canvas.draw_text(str(score2), (400,100), 32, 'white') 
    
def keydown(key):
    global paddle1_vel, paddle2_vel,paddle_vel
    # left player
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -3
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 3
    
    # right player
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -3
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 3
   
def keyup(key):
    global paddle1_vel, paddle2_vel
        # left player
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    
    # right player
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)


# start frame
new_game()
frame.start()
