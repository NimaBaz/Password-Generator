import random
from tkinter import *
from PIL import Image, ImageTk
import pyperclip

DEFAULT_FILE = 'images/Password Generator.jpg'
WIDTH = 300
HEIGHT = 300

# Character allowed for the password
NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOWER_CASE_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z']

UPPER_CASE_CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                    'Z']

SYMBOLS = ['@', '#', '$', '%', '!', '=', ':', '?', '.', '/', '|', '~',
           '>', '*']

# We want the all the characters from above to go in one array
ULTIMATE_PASSWORD = NUMS + LOWER_CASE_CHARS + UPPER_CASE_CHARS + SYMBOLS

# Max length of the password
MAX_LEN = 12

# This will randomly generate characters from each of these
num = random.choice(NUMS)
lower = random.choice(LOWER_CASE_CHARS)
upper = random.choice(UPPER_CASE_CHARS)
symbol = random.choice(SYMBOLS)

# Generates a password with random characters that are selected from above
password = num + lower + upper + symbol

def generate_password():

    # Generates random password with the given length and the number of passwords
    for x in range(1):
        password = ''
        for y in range(MAX_LEN):
            password += random.choice(ULTIMATE_PASSWORD)

    # This is to make the label to display the password when I hit the generate button
    z = "".join(str(i) for i in password)
    label.config(text = z)

    # Copy the password to clipboard
    pyperclip.copy(password)

# Kills the program
def exit():
    root.destroy()

'''
This is to make a title, button, label (label being where the password is displayed),
background image, and text
'''
root = Tk()
root.title("PassGen")

close = Frame(root)
canvas = Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()
close.pack()

image = ImageTk.PhotoImage(Image.open(DEFAULT_FILE).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
canvas.background = image
bg = canvas.create_image(0, 0, anchor = NW, image = image)

button = Button(root, text = "Generate Password", fg = 'yellow', bg = "blue", command = generate_password)
button_gen = canvas.create_window(2, 2, anchor = NW, window = button)

button2 = Button(root, text = "Close Window", fg = 'yellow', bg = "blue", command = exit)
button_close = canvas.create_window(107, 270, anchor = NW, window = button2)

label = Label(root, font = ("times", 15, "bold"), fg = 'yellow', bg = "black")
label_pass = canvas.create_window(80, 225, anchor = NW, window = label)

title = Label(root, text = "Welcome to PassGen", font = ("times", 15, "bold"), fg = 'yellow', bg = "black")
insert_title = canvas.create_window(60, 40, anchor = NW, window = title)

root.mainloop()
