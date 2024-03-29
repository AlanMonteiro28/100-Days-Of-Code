from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
from search_website import Search

BLACK = "#363636"
WHITE = "#EEEEEE"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #3

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join([char for char in password_list])
    password_entry.delete(0, END)
    password_entry.insert(END, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD // CLEAR ENTRYS------------------------------- #

def save():
    website_count = 1
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    data = None

    if not website or not email or not password:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
    finally:
        if website in data and email != data[website]["email"]:
            email_existing = data.get(website, {}).get("email", "")
            password_existing = data.get(website, {}).get("password", "")
            website_count = data.get(website, {}).get("count", 0) + 1
            new_website = f"{website}_{website_count - 1}"
            # update
            data.update({
                website: {
                    "email": email_existing,
                    "password": password_existing,
                    "count": website_count
                },
                new_website: {
                    "email": email,
                    "password": password,
                }
            })
        else:
            # update
            data.update({
                website: {
                    "email": email,
                    "password": password,
                    "count": website_count,
                }
            })

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


def clear():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- SEARCH BUTTON ------------------------------- #
def find_password():
    search_window = Search(window)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=BLACK)
window.resizable(width=False, height=False)

# IMAGE
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BLACK)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# WEBSITE
website_label = Label(text="Website:", font=18, bg=BLACK, fg=WHITE)
website_label.grid(column=0, row=1, padx=(0, 5), pady=2)

website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

website_button = Button(text="Search", command=find_password)
website_button.grid(column=2, row=1, sticky="EW", padx=(5, 0))

# EMAIL
email_label = Label(text="Email/Username:", font=18, bg=BLACK, fg=WHITE)
email_label.grid(column=0, row=2, pady=2)

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# PASSWORD
password_label = Label(text="Password:", font=18, bg=BLACK, fg=WHITE)
password_label.grid(column=0, row=3, pady=2)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW", padx=(5, 0))

# ADD
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", pady=2)

# CLEAR
clear_button = Button(text="Clear", command=clear, highlightthickness=0)
clear_button.grid(column=0, row=4, padx=(0, 5), pady=2, sticky="E")

window.mainloop()
