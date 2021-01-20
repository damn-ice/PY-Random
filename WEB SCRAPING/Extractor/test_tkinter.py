from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x500')
        self.title('Data Crawler')
        self.iconbitmap('snake.ico')
        first_label = Label(text="Website")
        first_label.grid(row=0, column=0, padx=20, pady=10)
        first_button = Button(text='CRAWL', command=testing, fg='red', relief=RIDGE)
        App.first_entry = Entry(width=90)
        App.first_entry.grid(row=0, column=2, pady=10)
        output = Text()
        output.grid(row=1, column=1, columnspan=4, pady=20)
        first_button.grid(row=2, column=2) 


def testing():
    x = App.first_entry.get()
    print(x)
    App.first_entry.delete(0, END)

app = App()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
app.bind("<Key>", handle_keypress)
app.configure(bg='black')
app.mainloop()

# import tkinter as tk

# class App(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack()

#         self.entrythingy = tk.Entry()
#         self.entrythingy.pack()

#         # Create the application variable.
#         self.contents = tk.StringVar()
#         # Set it to some value.
#         self.contents.set("this is a variable")
#         # Tell the entry widget to watch this variable.
#         self.entrythingy["textvariable"] = self.contents

#         # Define a callback for when the user hits return.
#         # It prints the current value of the variable.
#         self.entrythingy.bind('<Key-Return>',
#                              self.print_contents)

#     def print_contents(self, event):
#         print("Hi. The current entry content is:",
#               self.contents.get())

# root = tk.Tk()
# myapp = App(root)
# myapp.mainloop()

