from tkinter import *


class GeneratePassword:
    def __init__(self):
        self.window = Tk()
        self.create_layout()

    def create_layout(self):
        scale_numb_initial = 15
        scale_numb = IntVar()
        scale_numb.set(scale_numb_initial)

        self.window.title("Password Generate")
        self.window.config(padx=20, pady=10)

        title_label = Label(text="Password Generator", font=("Arial", 13, "bold"))
        title_label.grid(columnspan=2, sticky="EW")

        password_label = Label(width=25, height=2, bg="gray")
        password_label.grid(columnspan=2)

        scale_title = Label(text="Password Length")
        scale_title.grid(sticky="W")
        scale = Scale(from_=0, to=30, orient=HORIZONTAL, width=15, variable=scale_numb)
        scale.grid(columnspan=2, sticky="EW")

        numb_state = IntVar()
        number_button = Checkbutton(text="Use 0-9", variable=numb_state)
        number_button.grid(columnspan=2, padx=(5, 0), sticky="W")

        special_char_state = IntVar()
        special_char_button = Checkbutton(text="Use !@#$%^*&", variable=special_char_state)
        special_char_button.grid(columnspan=2, padx=(5, 0), sticky="W")

        qnt_numb_label = Label(text="How many numbers: ")
        qnt_numb_label.grid(padx=7, sticky="W")

        qnt_numb_box = Spinbox(from_=0, to=5, width=5)
        qnt_numb_box.grid(column=1, row=6)

        qnt_symbol_label = Label(text="How many symbols: ")
        qnt_symbol_label.grid(padx=7, sticky="W")

        qnt_symbol_box = Spinbox(from_=0, to=5, width=5)
        qnt_symbol_box.grid(column=1, row=7, padx=5)

        close_button = Button(text="Close", command=self.close)
        close_button.grid(columnspan=2)

        mainloop()

    def close(self):
        self.window.destroy()



GeneratePassword()
