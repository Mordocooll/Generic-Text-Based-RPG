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
bg_image = Image.open("end screen.png")  # Replace with your image file
bg_image = bg_image.resize((screenwidth, screenheight), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas for the background image
canvas = Canvas(root, width=screenwidth, height=screenheight)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")


frames = []

Ending = ["Amidst the cheers, you held the princess's hand and walked towards the magnificent palace.", 
"               You and the princess stopped by the king who was sitting on the throne.",
"       The ministers around the king announced your great achievements and your legendary adventure.",
"You then kissed the princess, and the princess looked at you shyly. Later, your great deeds were praised by the world.",
"               You were the first person to kill the dragon, and the last one.",
"       There is no doubt that you are the strongest hero, you deserve this legendary title!" ]

textDisplay = "\n".join(Ending)
text_end = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 18, 'bold'), fill="red")
frames.append(text_end)

#text2 = canvas.create_text(screenwidth/2, screenheight/2,text=textDisplay, anchor="center", font=("Times", 26), fill="white")
    #frames.append(text2)





root.mainloop()