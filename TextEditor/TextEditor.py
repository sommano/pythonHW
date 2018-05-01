from tkinter import*
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
import sys

def open_file():
    file = filedialog.askopenfile(mode="r")
    if file != None:
        text.delete("1.0", END)
        text.insert("1.0", file.read())
        file.close()

def save_file():
    file = filedialog.asksaveasfile(mode="w")
    if file != None:
        file.write(text.get("1.0", END))
        file.close()

def about_dialog():
    messagebox.showinfo("About", "Version 1.0\nEnjoy!")

def exit_app():
    sys.exit(0)

root_win = Tk()
root_win.title("Text Editor")
root_win.geometry("640x480")

main_menu = Menu(root_win)
root_win.config(menu = main_menu)

file_menu = Menu(main_menu)
main_menu.add_cascade(label="File", menu = file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command = save_file)
file_menu.add_command(label="About", command = about_dialog)
file_menu.add_command(label="Exit", command = exit_app)

text = scrolledtext.ScrolledText(root_win, width = 80, height = 30)
text.pack(fill = "both", expand = "yes")

root_win.mainloop()
