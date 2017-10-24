from tkinter import Tk, Label, Button, Entry

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI! π")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.text_entry = Entry(master)
        self.text_entry.pack()

    def greet(self):
        print("Greetings!")
        print(self.text_entry.get())

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
