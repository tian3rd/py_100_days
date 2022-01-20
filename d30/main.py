import tkinter as tk
from tkinter import messagebox
import os.path
from PIL import Image
import string
import random
import pyperclip
import json

BACKGROUND = '#F0F0F0'
DIR_PATH = os.path.dirname(__file__)
PW_FILE = os.path.join(DIR_PATH, 'data.json')
# print(PW_FILE)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(map(str, list(range(10))))
    specials = ['!', '#', '$', '^', '*', '+', '-', '_', '=', '~', '(', ')']

    num_letters = random.randint(6, 8)
    num_numbers = random.randint(2, 4)
    num_specials = random.randint(1, 3)

    password = []

    for _ in range(num_letters):
        password.append(random.choice(letters))

    for _ in range(num_numbers):
        password.append(random.choice(numbers))

    for _ in range(num_specials):
        password.append(random.choice(specials))

    random.shuffle(password)

    password = ''.join(password)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # paste it to the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if website == '' or password == '':
        messagebox.showerror('Error', 'Please don\'t leave any fields blank.')
        return

    if ' ' in website or ' ' in username or ' ' in password:
        messagebox.showerror(
            'Error', 'Please don\'t leave any spaces in your website, username, or password.')
        return

    is_ok = messagebox.askokcancel(
        title='Password Manager', message=f'{website} \n {username} \n {password} \n\n Is it OK to save?')

    if is_ok:
        write_to_file(PW_FILE, website, username, password)
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    website_entry.focus()


def write_to_file(filename, website, username, password):
    new_entry = {website: {'username': username, 'password': password}}
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            data.update(new_entry)
    except FileNotFoundError:
        with open(filename, 'w') as f:
            json.dump(new_entry, f, indent=4)
    else:  # if file exists
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    finally:
        f.close()

# ---------------------------- Search Password -------------------------------- #


def search():
    try:
        with open(PW_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror('Error', 'No passwords saved yet.')
        return
    else:
        website = website_entry.get().strip().lower()
        if website == "":
            messagebox.showerror('Error', 'Please enter a website.')
        elif website in map(str.lower, data.keys()):
            username = data[website]['username']
            password = data[website]['password']
            messagebox.showinfo(
                website, f'FOUND: \n {username} \n {password}')
        else:
            messagebox.showerror(
                'Error', f'No password found for website \"{website}\".')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
window.config(background=BACKGROUND, padx=20, pady=20)

# logo
img_path = os.path.join(os.path.dirname(__file__), "logo.png")
logo_img = Image.open(img_path)
width, height = logo_img.size
logo_bg = tk.PhotoImage(file=img_path)
canvas = tk.Canvas(width=width, height=height,
                   highlightthickness=0, bg=BACKGROUND)
canvas.create_image(width/2, height/2, image=logo_bg)
canvas.grid(row=0, column=1)

# labels, texts and buttons
website_label = tk.Label(text='Website', bg=BACKGROUND)
website_entry = tk.Entry(width=21)
website_entry.focus()
website_search = tk.Button(text='Search', command=search, width=13)
username_label = tk.Label(text='Email/Username', bg=BACKGROUND)
username_entry = tk.Entry(width=38)
username_entry.insert(0, 'tianwu@outlook.com')
password_label = tk.Label(text='Password', bg=BACKGROUND)
password_entry = tk.Entry(width=21)
generate_pw_btn = tk.Button(
    text='Generate Password', bg=BACKGROUND, highlightthickness=0, command=generate_password)
add_btn = tk.Button(text='Add', bg=BACKGROUND, width=36,
                    highlightthickness=0, command=lambda: save())

website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1)
website_search.grid(row=1, column=2)
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_pw_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
