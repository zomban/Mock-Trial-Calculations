#!/usr/bin/python
from tkinter import Tk, Label, Button, Entry


class Ballot:
    def __init__(self, master):
        self.master = master
        master.title("Enter ballot results")

# This section defines the ballot number label and entry field

        self.label = Label(master, text="Ballot #")
        self.label.grid(row=1, column=3)

        self.text_entry = Entry(master)
        self.text_entry.grid(row=1, column=4)

        self.greet_button = Button(master, text="Print", command=self.save)
        self.greet_button.grid(row=27, column=2)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=27, column=5)

    def save(self):
        print(self.text_entry.get())


root = Tk()
gui = Ballot(root)
root.mainloop()
