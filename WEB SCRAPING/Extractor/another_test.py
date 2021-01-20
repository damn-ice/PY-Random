# from tkinter import *


# def add(a, b, c):
#     x = a+b
#     c.delete('1.0', END)
#     c.insert('1.0', x)

# window = Tk()

# first_label = Label(text='first', foreground='white', background='black')
# first_entry = Entry()
# second_label = Label(text='second', foreground='white', background='black')
# second_entry = Entry()
# output = Text()
# submit = Button(text='Submit', fg='red', command=lambda: add(int(first_entry.get()), int(second_entry.get()), output))

# first_label.pack()
# first_entry.pack()
# second_label.pack()
# second_entry.pack()
# output.pack()
# submit.pack()

# window.mainloop()

# from functools import partial 
  
# # A normal function 
# def f(a, b, c, x): 
#     return 1000*a + 100*b + 10*c + x 
  
# # A partial function that calls f with 
# # a as 3, b as 1 and c as 4. 
# g = partial(f, 3, 1, 4) 
  
# # Calling g() 
# print(g(5)) 

# import tkinter as tk

# window = tk.Tk()

# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# window.mainloop()

# import tkinter as tk

# window = tk.Tk()

# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()

# window.mainloop()

# import tkinter as tk

# def fahrenheit_to_celsius():
#     """Convert the value for Fahrenheit to Celsius and insert the
#     result into lbl_result.
#     """
#     fahrenheit = ent_temp.get()
#     celsius = (5/9) * (float(fahrenheit) - 32)
#     lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
# window = tk.Tk()

# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# btn_decrease = tk.Button(master=window, text="-")
# btn_decrease.grid(row=0, column=0, sticky="nsew")

# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)

# btn_increase = tk.Button(master=window, text="+")
# btn_increase.grid(row=0, column=2, sticky="nsew")

# window.mainloop()
# window.title('Temp')

# frm_entry = tk.Frame(master=window)
# ent_temp = tk.Entry(master=frm_entry, )
# lbl_temp = tk.Label(master=frm_entry, text='\N{DEGREE FAHRENHEIT}')

# ent_temp.grid(row=0, column=1, sticky='e')
# lbl_temp.grid(row=0, column=0, sticky='w')


# btn_convert = tk.Button(
#     master=window,
#     text="\N{RIGHTWARDS BLACK ARROW}",
#     command=fahrenheit_to_celsius
# )
# lbl_result = tk.Label(text='\N{DEGREE CELSIUS}')
# frm_entry.grid(row=0, column=0, padx=10)
# btn_convert.grid(row=0, column=1, pady=10)
# lbl_result.grid(row=0, column=2, padx=10)
# window.mainloop()

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    file_name = askopenfilename(filetypes=[
        ('Text Files', '*.txt'),
        ('All Files', '*.*')
    ])
    if not file_name:
        return
    text_box.delete('1.0', END)
    with open(file_name, 'r') as file_obj:
        text = file_obj.read()
        text_box.insert(END, text)
    window.title(f"Simple Text Editor - {file_name}")

def save_file():
    file_name = asksaveasfilename(filetypes=[
        ('Text Files', '*.txt'),
        ('All Files', '*.*')
    ], defaultextension='txt')
    if not file_name:
        return
    with open(file_name, 'w') as file_obj:
        text = text_box.get('1.0', END)
        file_obj.write(text)
    window.title(f"Simple Text Editor - {file_name}")


window = Tk()
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

frm = Frame(master=window)
btn_save = Button(master=frm, text='Save As...', command=save_file)
btn_open = Button(master=frm, text='Open', command=open_file)
btn_save.grid(row=0, column=0, sticky='ew',pady=20, padx=20)
btn_open.grid(row=1, column=0, sticky='ew', pady=20, padx=20)

text_box = Text(master=window)

frm.grid(row=0, column=0, sticky='ns')
text_box.grid(row=0, column=1, sticky='nsew')



window.mainloop()