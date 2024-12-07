from tkinter import *
from PIL import Image, ImageTk
import subprocess

def restart():
    subprocess.Popen(["python", "Run Me.py"]) 
    root.destroy() 

root = Tk()
root.attributes('-fullscreen', True)
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight() 
# background image
bg_image = Image.open("death screen.png")  # Replace with your image file
bg_image = bg_image.resize((screenwidth, screenheight), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create Canvas
canvas1 = Canvas(root, width=screenwidth, height=screenheight)
canvas1.pack(fill="both", expand=True)

# Display image

canvas1.create_image(0, 0, image=bg_photo, anchor="nw")

# Add Text
text = canvas1.create_text(screenwidth/2, screenheight/2.25, text="You Died", fill="dark red", font=("Times", 80))
bbox = canvas1.bbox(text)


# Add Button
button1 = Button(root, text="Restart", command=restart, font=("Times", 60), bg = 'red', fg = 'white')
button1_canvas = canvas1.create_window(screenwidth/2.45, screenheight/2, anchor="nw", window=button1)

# Run the Tkinter event loop
root.mainloop()