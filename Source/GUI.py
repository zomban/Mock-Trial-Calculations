#!/usr/bin/python
from tkinter import Tk, Label, Button, Entry


class Ballot:
    def __init__(self, master):
        self.master = master
        master.title("Enter ballot results")

# Define the ballot number label and entry field

        self.label_ballot_num = Label(master, text="Ballot #")
        self.label_ballot_num.grid(row=1, column=3)

        self.ballot_num = Entry(master)
        self.ballot_num.grid(row=1, column=4)

# Define side labels

        self.label_p_side = Label(master, text="π")
        self.label_p_side.grid(row=2, column=2)

        self.label_d_side = Label(master, text="Δ")
        self.label_d_side.grid(row=2, column=5)

# Define Prosecution open label and entry field

        self.label_p_open = Label(master, text="π Opening")
        self.label_p_open.grid(row=3, column=1)

        self.p_open_raw = Entry(master)
        self.p_open_raw.grid(row=3, column=2)

# Define Defense open label and entry field

        self.label_d_open = Label(master, text="Δ Opening")
        self.label_d_open.grid(row=3, column=5)

        self.d_open_raw = Entry(master)
        self.d_open_raw.grid(row=3, column=6)

# Define procecution case in chief Label

        self.label_p_case = Label(master, text="π Case in Chief")
        self.label_p_case.grid(row=4, column=2)

# Define the buttons

        self.button_save_ballot = Button(master, text="Print", command=self.save)
        self.button_save_ballot.grid(row=27, column=2)

        self.button_close = Button(master, text="Close", command=master.quit)
        self.button_close.grid(row=27, column=5)

# Function will eventually save results to array, now just prints ballot_num

    def save(self):
        print(self.ballot_num.get())


root = Tk()
gui = Ballot(root)
root.mainloop()
