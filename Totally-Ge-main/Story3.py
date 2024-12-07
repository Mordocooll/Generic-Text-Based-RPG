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

def fight3():
# Launch monster fight demo.py and close the current window
    subprocess.Popen(["python", "monster fight 3.py"])  # Runs game.py
    root.destroy()  # Close the meny.py window


def open_frame6():
    clearFrames()
   
    global text5  # Declare these as global
    
    
    theNext5= Button(root, text="Next", font=("Times", 15), command=open_frame7)
    theNextWindow5 = canvas.create_window(screenwidth/2, screenwidth/2, anchor="nw", window=theNext5)
    
    
    frames.append(theNextWindow5)
   
    story5 = ["The villagers, puzzled but grateful, approach you and thank you for saving them,",
"You ask about the kingdom and learn of survivors who passed through seeking a knight to slay the dragon,",
"They mention a shortcut to the castle through a cave, home to violent goblins,",
"Thanking the villagers, you venture forth toward the cave,"
                ]
    
    textDisplay = "\n".join(story5)
    text5 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
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
    
    
    theNext7= Button(root, text="Next", font=("Times", 15), command=fight3)
    theNextWindow7 = canvas.create_window(screenwidth/2, screenheight/1.5, anchor="nw", window=theNext7)
    
    
    frames.append(theNextWindow7)
   
    story7 = [
           "Inside the dark, cold cave, you feel as if something is watching you,",
"A faint light leads you to a large area with a red circle and a throne made of bones,",
"A loud grunt echoes, and goblins emerge, surrounding you,",
"A giant goblin appears, silencing the others and demanding your purpose,",
"After explaining, the goblin leader offers safe passage in exchange for the dragon's head,",
"You agree, and a group of goblins guides you deeper into the cave,",
"In the cave, you hear something behind a rock,",
"As you near, the unknown creature leaps at you and you prepare for battle"

                ]
    
    textDisplay = "\n".join(story7)
    text7 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text7)



open_frame6()
root.mainloop()