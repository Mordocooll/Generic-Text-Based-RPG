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

def fight2():
# Launch monster fight demo.py and close the current window
    subprocess.Popen(["python", "monster fight 2.py"])  # Runs game.py
    root.destroy()  # Close the meny.py window


def open_frame5():   
    global  text4 
    
    
    theNext4= Button(root, text="Next", font=("Times", 15), command=fight2)
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
    
    
    
    




open_frame5()
root.mainloop()