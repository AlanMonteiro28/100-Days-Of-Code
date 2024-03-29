import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import pyperclip

BLACK = "#363636"
WHITE = "#EEEEEE"
FONT = ("Courier New", 18, "bold")
LABEL_FONT = ("Courier New", 10, "normal")

class Search(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.data = None
        self.title("Website Search")
        self.config(padx=20, pady=20, background=BLACK)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.filter_label = tk.Label(self, text="DATABASE", font=FONT, bg=BLACK, fg=WHITE)
        self.filter_label.grid(column=0, row=0, columnspan=3)

        self.filter_entry = tk.Entry(self)
        self.filter_entry.grid(column=0, row=1, sticky="EW")

        self.filter_btn = tk.Button(self, text="Filter", relief="ridge", bg=BLACK, fg=WHITE, command=self.filter_data)
        self.filter_btn.grid(column=1, row=1, padx=(10, 5), sticky="EW")

        self.filter_label = tk.Label(self, text="💎 Double click to copy password", font=LABEL_FONT, bg=BLACK, fg=WHITE)
        self.filter_label.grid(column=0, row=2, sticky="W")

        self.tree = ttk.Treeview(self, columns=("WEBSITE", "EMAIL", "PASSWORD"), show="headings", displaycolumns=(0, 1, 2))
        self.tree.heading("WEBSITE", text="WEBSITE")
        self.tree.heading("EMAIL", text="EMAIL")
        self.tree.heading("PASSWORD", text="PASSWORD")
        self.tree.column("WEBSITE", stretch=tk.NO, width=150)
        self.tree.column("EMAIL", stretch=tk.NO, width=150)
        self.tree.column("PASSWORD", stretch=tk.NO, width=150)
        self.tree.grid(column=0, row=3, columnspan=3, pady=5, sticky="EW")

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview, width=20)
        self.scrollbar.grid(column=3, row=3, pady=5, sticky="NS")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.bind("<Double-1>", self.on_tree_double_click)

        self.load_data()
        self.update_tree()

    def load_data(self):
        try:
            with open('data.json', 'r') as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No Data File Found.")
            self.on_close()

    def update_tree(self, data_list_box=None):
        self.tree.delete(*self.tree.get_children())

        if data_list_box is None:
            data_list_box = self.data

        for site_name, site_data in data_list_box.items():
            website = site_name
            email = site_data.get('email', 'Not Set')
            password = site_data.get('password', 'Not Set')
            self.tree.insert("", "end", values=(website, email, password), tags=("separator",))

    def filter_data(self):
        filter_term = self.filter_entry.get().lower()
        filtered_data = {key: value for key, value in self.data.items() if filter_term in key.lower() or filter_term in value.get('email', '').lower()}
        self.update_tree(filtered_data)

    def on_tree_double_click(self, event):
        item = self.tree.selection()
        if item:
            column = self.tree.identify_column(event.x)
            if column == "#2":
                values = self.tree.item(item, 'values')
                password = values[2]
                if password:
                    pyperclip.copy(password)

    def on_close(self):
        self.destroy()
