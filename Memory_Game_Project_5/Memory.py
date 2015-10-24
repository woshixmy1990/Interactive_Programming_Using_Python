# implementation of card game - Memory

import simplegui
import random
card_list=range(0,8)+range(0,8)
exposed=[False for i in range(16)]
#exposed=[False,True,False,True,True,False,True,False,True,False,False,False,False,True,True,True,]
turns=0
state=0
choice1=0
choice2=0


# helper function to initialize globals
def new_game():  
    global card_list, exposed, turns, state, choice1, choice2
    state = 0
    turns = 0   
    choice1=0
    choice2=0
    exposed=[False for i in range(16)]
    random.shuffle(card_list)
    label.set_text("Turns = " + str(turns))

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, card_list, exposed, choice1, choice2, turns
    card_num=int(pos[0]/50)
    if state == 0:
        state=1
        choice1=card_num
        exposed[card_num]=True
            
    elif state == 1:
        if exposed[card_num]==False:
            choice2=card_num
            exposed[choice2]=True
            state = 2
            turns+=1
          

    elif state==2:
        if exposed[card_num]==False:
            if card_list[choice1]!=card_list[choice2]:
                exposed[choice1]=False
                exposed[choice2]=False
                choice1=card_num
                exposed[card_num]=True
                state=1
            elif card_list[choice1]==card_list[choice2]:
                choice1=card_num
                exposed[choice1]=True
                state=1
    label.set_text("Turns = " + str(turns))
    pass  
            
       
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_list, exposed
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(card_list[i]), (50*i+10, 60), 40, "Red")
        else:
            canvas.draw_polygon([(50*i, 0), (50*i+50, 0), (50*i + 50, 100), (50*i , 100)], 3, "Black", "Green")
    
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label=frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric