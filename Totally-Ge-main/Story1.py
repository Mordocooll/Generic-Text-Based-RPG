from tkinter import *
from PIL import Image, ImageTk
import subprocess

root = Tk()
root.attributes('-fullscreen', True)
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight() 
root.title("Username Input with Background")
root.geometry(f'{screenwidth}x{screenheight}')  # Adjust to fit the background image

# Background image setup
bg_image = Image.open("file.png")  # Replace with your image file
bg_image = bg_image.resize((screenwidth, screenheight), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas for the background image
canvas = Canvas(root, width=screenwidth, height=screenheight)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")


# This will add windows to the list of frames
frames = []

#This function clears the windows in the frame to open up new frames
def clearFrames():
    #for every element that is added to the frame
    for elements in frames:
        #delete all the elements in the frame
        canvas.delete(elements)
    #it is now an empty list
    frames.clear()

def fight1():
# Launch monster fight demo.py and close the current window
    subprocess.Popen(["python", "monster fight 1.py"])  # Runs game.py
    root.destroy()  # Close the meny.py window

def open_frame1():
    #If there is any frames from previous windows (frame 2, frame 3) clear those frames
    clearFrames()

    #global variables for windows
    global label_window, username_window, userSubmit, outputWindow


    label = Label(root, text="What is your name?: ", font=("Times", 28))
    label_window = canvas.create_window(screenwidth/3, screenheight/2.7, anchor="nw", window=label)
    #Appending label_window adds to the frames list (see line 20)
    frames.append(label_window)

    username = Entry(root, font=("Times", 28), width=30)
    username_window = canvas.create_window(screenwidth/1.75, screenheight/2.7, anchor="nw", window=username)
    #add to frames list
    frames.append(username_window)
    
    #this function helps user submit there username
    def submit():
        global frame2butt, frame2Window
        #user = username.get() get's the info on the user input
        user = username.get()

        #output prints out what happens if user presses submit
        output.config(text=f"Welcome, {user}. Ready to start?")
    
        
        # This button will access the function open_frame2
        frame2butt = Button(root, text="Let's Go!", font=("Times", 32), command=open_frame2)
        frame2Window = canvas.create_window(screenwidth/2, screenheight/1.85, anchor="nw", window=frame2butt)
        #add to frames list
        frames.append(frame2Window)

        #hides the button after the user presses the button
        canvas.itemconfig(userSubmit, state="hidden")

    #when user presses submit name, the command will run the submit() function
    submit = Button(root, text="Submit Name", font=("Times", 32), command=submit)
    userSubmit = canvas.create_window(screenwidth/2, screenheight/2.25, anchor="nw", window=submit)
    #add to frames list
    frames.append(userSubmit)

    #this output is for the username to be shown in the text
    output = Label(root, text="", font=("Times", 32),)
    outputWindow = canvas.create_window(screenwidth/1.85, screenheight/2, window=output)
    #add to frames list
    frames.append(outputWindow)



def open_frame2():
    #clears frames from previous frames and shows the frames in this function
    clearFrames()
    global  label2_window, start_button_window, return_button_window, text1 # Declare these as global
    
    #750 is the center
    label2 = Label(root, text="Welcome to the Game!", font=("Times", 32))
    label2_window = canvas.create_window(screenwidth/2.55, screenheight/3.75, anchor="nw", window=label2)
    frames.append(label2_window)
    
    theNext= Button(root, text="Next", font=("Times", 15), command=open_frame3)
    theNextWindow = canvas.create_window(screenwidth/2, screenheight/1.5, anchor="nw", window=theNext)
    
    frames.append(theNextWindow)
   
    story = ["Once a noble knight for a grand empire, you were respected and destined to become the king's right-hand man,",
                "The kingdom descends into chaos as a legendary dragon awakens and attacks,",
                "While the military scrambles to fight, the king tasks you with protecting his daughter, the princess,",
                "As the castle crumbles under the dragon's wrath, debris falls, and men flee,",
                "The king orders you to escape and swear to protect the princess with your life,",
                "A massive explosion erupts, and everything goes dark and silent,"
                ]
    
    textDisplay = "\n".join(story)
    text1 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 26), fill="white")
    frames.append(text1)
    

def open_frame3():
    clearFrames()
    
    global text2  # Declare these as global
        
    theNext2= Button(root, text="Next", font=("Times", 15), command=open_frame4)
    theNextWindow2 = canvas.create_window(screenwidth/2, screenheight/1.5, anchor="nw", window=theNext2)
    
    frames.append(theNextWindow2)
   
    story2 = ["After an unknown amount of time, you awaken in a forest, confused and trying to gather your thoughts,",
"You remember the king's last words; this is where your journey begins,",
"Your mission is to return to the castle and rescue the princess, if there's anything to rescue at all,",
"Since the explosion, you’ve lost your equipment and are empty-handed,",
"With no clue where you are, you must navigate the forest to find your way back to the castle,",
"Following hints of disturbed nature, you notice debris leading in one direction and start walking toward it,"

            ]
    
    textDisplay = "\n".join(story2)
    text2 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 26), fill="white")
    frames.append(text2)
   

def open_frame4():
    clearFrames()
   
    global text3 
        
    theNext3= Button(root, text="Next", font=("Times", 15), command=fight1)
    theNextWindow3 = canvas.create_window(screenwidth/2, screenheight/1.5, anchor="nw", window=theNext3)
    
    
    frames.append(theNextWindow3)
   
    story3 = ["Walking down the path, you stumble upon a peculiar graveyard filled with human bones and blank headstones,",
"A glimmer catches your eye, and you see a sword lodged in a skeleton's ribcage,",
"With nothing else on you, you take the sword and feel a surge of power as you grasp the handle,",
"Despair overtakes you as the skeleton begins to reassemble, its empty sockets locking onto you,",
"Realizing this must be necromancy, you recall the tale of a deceitful necromancer who betrayed the kingdom,",
"The skeleton rises and takes a stance, preparing to attack as you ready yourself for battle,",

               ]
    
    textDisplay = "\n".join(story3)
    text3 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 26), fill="white")
    frames.append(text3)
   

def open_frame5():
    clearFrames()
   
    global  text4  # Declare these as global
    
    
    theNext4= Button(root, text="Next", font=("Times", 15), command=open_frame6)
    theNextWindow4 = canvas.create_window(screenwidth/2, screenheight/1.5, anchor="nw", window=theNext4)
    
    
    frames.append(theNextWindow4)
   
    story4 = ["After defeating the monster, you continue your journey, noticing the debris thinning,",
"Through the trees, you spot an opening revealing small cottages,",
"You approach the buildings, hoping to find aid, and discover a village,",
"A dark shadow looms above, terrorizing the villagers,",
"Determined to help, you confront the figure with your sword in hand,",
"It stares blankly before charging an attack, forcing you into battle once again,",

                
                ]
    
    textDisplay = "\n".join(story4)
    text4 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text4)
    
def open_frame6():
    clearFrames()
   
    global text5  # Declare these as global
    
    
    theNext5= Button(root, text="Next", font=("Times", 15), command=open_frame7)
    theNextWindow5 = canvas.create_window(screenwidth/2, screenheight/1.5, anchor="nw", window=theNext5)
    
    
    frames.append(theNextWindow5)
   
    story5 = ["The villagers, puzzled but grateful, approach you and thank you for saving them,",
"You ask about the kingdom and learn of survivors who passed through seeking a knight to slay the dragon,",
"They mention a shortcut to the castle through a cave, home to violent goblins,",
"Thanking the villagers, you venture forth toward the cave,"
                ]
    
    textDisplay = "\n".join(story5)
    text5 = canvas.create_text(screenwidth/2, screenwidth/2,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text5)

def open_frame7():
    clearFrames()
   
    global  text6  # Declare these as global
    
    
    theNext6= Button(root, text="Next", font=("Times", 15), command=open_frame8)
    theNextWindow6 = canvas.create_window(screenwidth/2, screenheight/1.5, anchor="nw", window=theNext6)
    
    
    frames.append(theNextWindow6)
   
    story6 = ["As you walk, you take in the peaceful scenery—breezes, birds, and fresh grass,",
"However, this peace vanishes as you reach the cave entrance, uncertainty creeping in,",
"Remembering your vow to the king, you press forward and enter the cave,"

                ]
    
    textDisplay = "\n".join(story6)
    text6 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text6)

def open_frame8():
    clearFrames()
   
    global text7  # Declare these as global
    
    
    theNext7= Button(root, text="Next", font=("Times", 15), command=open_frame9)
    theNextWindow7 = canvas.create_window(screenwidth/2, screenheight/1.5, anchor="nw", window=theNext7)
    
    
    frames.append(theNextWindow7)
   
    story7 = [
           "Inside the dark, cold cave, you feel as if something is watching you,",
"A faint light leads you to a large area with a red circle and a throne made of bones,",
"A loud grunt echoes, and goblins emerge, surrounding you,",
"A giant goblin appears, silencing the others and demanding your purpose,",
"After explaining, the goblin leader offers safe passage in exchange for the dragon's head,",
"You agree, and a group of goblins guides you deeper into the cave,",

                ]
    
    textDisplay = "\n".join(story7)
    text7 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text7)

def open_frame9():
    clearFrames()
   
    global text8  # Declare these as global
    
    
    theNext8= Button(root, text="Next", font=("Times", 15), command=open_frame9)
    theNextWindow8 = canvas.create_window(screenwidth/2, screenheight/1.5, anchor="nw", window=theNext8)
    
    
    frames.append(theNextWindow8)
   
    story8 = [
                "The goblins lead you to the cave’s exit, staring as you leave toward the castle,",
"Night falls as you reflect on your exhausting journey, but you press on,",
"Finally reaching the castle's base, you find survivors who cheer your arrival,",
"They believe only you can slay the dragon and save the princess,",
"Gathering supplies, you prepare for the final battle,",
"Inside the castle, the dragon awakens as you draw your sword,",
"The moment is now; it's time to slay the dragon,",
                ]
    
    textDisplay = "\n".join(story8)
    text8 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text8)



#I WILL MAKE THE ENDING AFTER SOME FEEDBACK


root.attributes('-fullscreen', True)
open_frame1()
root.mainloop()