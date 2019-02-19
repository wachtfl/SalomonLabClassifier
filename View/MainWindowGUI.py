from tkinter import *
from tkinter import filedialog

# window = Tk()
# window.title("Solomon Lab's EEG Classifier")
# window.geometry('900x600')
# #file = filedialog.askopenfilename()
# menu = Menu(window)
# new_item = Menu(menu)
# new_item.add_command(label='New')
# menu.add_cascade(label='File', menu=new_item)
# window.config(menu=menu)
#
#
# window.mainloop()
from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()