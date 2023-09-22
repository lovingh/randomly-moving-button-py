import tkinter as tk
import random


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Do you love me?")
        self.geometry("400x200")
        self.message_label = tk.Label(self, text="Do you love me?", font=("Helvetica", 16))
        self.message_label.pack(pady=20)
        self.yes_button = tk.Button(self, text="Yes", command=self.show_love)
        self.no_button = tk.Button(self, text="No")
        self.yes_button.pack()
        self.no_button.pack()
        self.no_button.bind("<Enter>", self.move_no_button)

    def show_love(self):
        self.message_label.config(text="I love you too! 😘")

    def move_no_button(self, event):
        x = random.randint(10, 350)
        y = random.randint(10, 150)
        self.no_button.place(x=x, y=y)


app = App()
app.mainloop()
