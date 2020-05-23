import random
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import pyperclip
import webbrowser

DEFAULT_FILE = 'images/Password Generator.jpg'
WIDTH = 300
HEIGHT = 300

# Characters allowed for the password
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

def options():
    # Deletes the password you generate once you hit the generate button to give another password
    entry.delete(0, END)

    # This gets the length of the password
    length = variable2.get()

    # Generates a password with random characters
    num = random.choice(NUMS)
    lower = random.choice(LOWER_CASE_CHARS)
    upper = random.choice(UPPER_CASE_CHARS)
    symbol = random.choice(SYMBOLS)

    weak_password = num + lower
    medium_password = num + lower + upper
    ultimate_password = num + lower + upper + symbol

    password = ''

    # Generates random password with the given length
    # Generates random password by strength level which goes from low to strong (low = 1, medium = 0, strong = 3)
    if variable.get() == 1:
        for i in range(0, length):
            password = password + random.choice(weak_password)
        return password

    elif variable.get() == 0:
        for i in range(0, length):
            password = password + random.choice(medium_password)
        return password

    elif variable.get() == 3:
        for i in range(0, length):
            password = password + random.choice(ultimate_password)
        return password

# Generates random password
def generate_password():
    gen_pass = options()
    entry.insert(10, gen_pass)

# Copying the password to clipboard
def copy():
    copy = entry.get()
    pyperclip.copy(copy)

def hyperlink(url):
    webbrowser.open_new(url)

''''
This is to make the design and functionality of the application
'''
root = Tk()
variable = IntVar()
variable2 = IntVar()

# Title for application
root.title("PassGen")

# Adding an image in the background
canvas = Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()
image = ImageTk.PhotoImage(Image.open(DEFAULT_FILE).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
canvas.background = image
bg = canvas.create_image(0, 0, anchor = NW, image = image)

# A button for generating the password
button = Button(root, text = "Generate Password", command = generate_password)
button_gen = canvas.create_window(2, 2, anchor = NW, window = button)

# A button to copy the password
button2 = Button(root, text = "Copy", command = copy)
button_copy = canvas.create_window(2, 30, anchor = NW, window = button2)

# I created an entry to display the password
entry = Entry(root)
insert_pass = canvas.create_window(118, 125, anchor = NW, window = entry)

# I created a label to the add text
label = Label(root, text = "Password")
insert_label = canvas.create_window(55, 126, anchor = NW, window = label)

label2 = Label(root, text = "Length")
insert_label2 = canvas.create_window(62, 150, anchor = NW, window = label2)

# Adding a hyperlink to label
link = Label(root, text="https://github.com/NimaBaz")
link.pack()
link.bind("<Button-1>", lambda e: hyperlink("https://github.com/NimaBaz"))
add_link = canvas.create_window(141, 280, anchor = NW, window = link)

# Choosing the strength level of your password
choose_low = Radiobutton(root, text = "Low", variable = variable, value = 1)
low = canvas.create_window(95, 175, anchor = NW, window = choose_low)

choose_middle = Radiobutton(root, text = "Medium", variable = variable, value = 0)
middle = canvas.create_window(140, 175, anchor = NW, window = choose_middle)

choose_strong = Radiobutton(root, text = "Strong", variable = variable, value = 3)
strong = canvas.create_window(208, 175, anchor = NW, window = choose_strong)

# A box for length of your password that you would like to choose
combo = Combobox(root, textvariable = variable2)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo = canvas.create_window(110, 150, anchor = NW, window = combo)

root.mainloop()
