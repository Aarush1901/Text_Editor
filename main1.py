from tkinter import *
import tkinter as tk
from tkinter import filedialog
screen=tk.Tk()
screen.title("File Opener")
def func1():
    open_file=filedialog.askopenfile(filetypes=[("Text File","*.txt")])
    if open_file:
        with open(open_file.name,"r") as file:
            content=file.read()
            text.delete(1.0,tk.END)
            text.insert(tk.END,content)
def func2():
    open_file=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("textfile","*.txt")])
    if open_file:
        content_to_save=text.get(1.0,tk.END)
        with open(open_file,"w") as file:
            file.write(content_to_save)
text=tk.Text(screen,wrap=tk.WORD)
text.pack(fill=tk.BOTH,expand=True)
menu_bar=tk.Menu(screen)
file_menu=tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Open",command=func1)
file_menu.add_command(label="Save",command=func2)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=screen.quit)
menu_bar.add_cascade(label="File",menu=file_menu)
screen.config(menu=menu_bar)
screen.mainloop()