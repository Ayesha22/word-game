# import the modules  
import tkinter 
import random
from tkinter import messagebox
from tkinter import *
  
# list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','Purple','Brown']
incorrect=['RBID','OCLD','GDOL','IGHLT','AMRS',
           'YEE','NOSG','IEWF','IIFW','OPT',
           'ANM','TALIY','DIANI','PAINS','CAINH',
           'OORD','OYTS','ERINDFS','TAH','BNEGALRUU']
correct=['BIRD','COLD','GOLD','LIGHT','ARMS','MARS',
         'EYE','SONG','WIFE','WIFI','TOP','POT',
         'MAN','ITALY','INDIA','CHINA','CHAIN','SPAIN',
         'DOOR','TOYS','FRIENDS','HAT','BENGALURU']

#the initial score is 0
score = 0

#shuffle the colours
random.shuffle(colours)

#shuffle the incorrect words
random.shuffle(incorrect)

#shuffle the colours
random.shuffle(correct)

#index to acess one incorrect word at a time
i=0

# the game time left, initially 30 seconds. 
timeleft = 60
  
# function that will start the game. 
def startGame(event): 
    global i
    if timeleft == 60:     
        # start the countdown timer. 
        countdown()
    # run the function to 
    # choose the next colour.
    nextColour() 
  
# Function to choose and 
# display the next colour. 
def nextColour():
    # use the globally declared 'score' 
    # and 'play' variables above. 
    global i
    global score 
    global timeleft
    # if a game is currently in play 
    if timeleft > 0:
            # make the text entry box active. 
            e.focus_set() 
            # if the colour typed is equal 
            # to the colour of the text
            for j in correct:
                if e.get().lower() == j.lower(): 
                    score += 1
            # clear the text entry box. 
            e.delete(0, tkinter.END)
        
            if(i<20):
                # change the colour to type, by changing the
                # text _and_ the colour to a random colour value
                label.config(fg=str(colours[i%9]),text = str(incorrect[i])) 
                i=i+1
                # update the score.
                scoreLabel.config(text = "Score: " + str(score),bg='#99ccff',fg='#00264d')
            else:
                if score==len(incorrect):
                    messagebox.showinfo('Results','You won'+str(score))
                    exit(0)
                else:
                    messagebox.showinfo('Results','Your Score is '+str(score))
                    exit(0)
           
        
  
# Countdown timer function  
def countdown(): 
  
    global timeleft 
  
    # if a game is in play 
    if timeleft > 0: 
  
        # decrement the timer. 
        timeleft -= 1
          
        # update the time left label 
        timeLabel.config(text = "Time left: "
                               + str(timeleft),bg='#99ccff',fg='#00264d') 
                                 
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown) 
    if timeleft ==0:
        if score==len(incorrect):
            messagebox.showinfo('Results','You won '+str(score))
            exit(0)
        else:
            messagebox.showinfo('Results','Your Score is '+str(score))
            exit(0)
  
# Driver Code 
def user_screen():
    global root
    global timeLabel
    global scoreLabel
    global e
    global label
    # create a GUI window
    root=Toplevel(screen1)
    # set the title
    root.title("WORD GAME")
    # set the size
    root.geometry("375x200")
    root.configure(background='#99ccff')
    # add an instructions label
    instructions = tkinter.Label(root, text = "Type in the correct word ",font = ('Helvetica', 14),bg='#99ccff',fg='#00264d')
    instructions.pack()
    
    userLabel = tkinter.Label(root, text = "Username : "+ username.get(),font = ('Helvetica', 12),bg='#99ccff',fg='#00264d')
    userLabel.pack()
    # add a score label
    scoreLabel = tkinter.Label(root, text = "Press enter to start",font = ('Helvetica', 12),bg='#99ccff',fg='#00264d')
    scoreLabel.pack()
    # add a time left label
    timeLabel = tkinter.Label(root, text = "Time left: "+ str(timeleft),font = ('Helvetica', 12),bg='#99ccff',fg='#00264d')
    timeLabel.pack()
    # add a label for displaying the colours
    label = tkinter.Label(root, font = ('Helvetica', 40),bg='#99ccff',fg='#00264d')
    label.pack()
    # add a text entry box for
    # typing in colours
    e = tkinter.Entry(root,font = ('Helvetica',14))
    # run the 'startGame' function
    # when the enter key is pressed
    root.bind('<Return>', startGame)
    e.pack()
    # set focus on the entry box
    e.focus_set()
    # start the GUI

def main_screen():
    #to store players name
    global username
    #screen1 of gui
    global screen1
    #create gui window
    screen1=tkinter.Tk()
    #title of window
    screen1.title("WORD GAME")
    #size of window
    screen1.geometry("375x200")
    #setting background color for screen1
    screen1.configure(background='#99ccff')
    #username is string type
    username=StringVar()
    Label(screen1,text="",bg='#99ccff',fg='#00264d').pack()
    Label(screen1,text="",bg='#99ccff',fg='#00264d').pack()
    #create lable for user name
    Label(screen1,text="USERNAME ",font = ('Helvetica', 25),bg='#99ccff',fg='#00264d').pack()
    #an entry box to enter username
    username_entry = Entry(screen1,font = ('Helvetica', 16),textvariable=username)
    username_entry.pack()
    Label(screen1,text="",bg='#99ccff',fg='#00264d').pack()
    #button to start game
    Button(screen1,text="START",font = ('Helvetica', 14),width=10,height=1,bg='#ccccff',fg='#00264d',command=user_screen).pack()

main_screen()
