import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import colorchooser, font
from tkinter.filedialog import *
from tkinter import dialog

def change_font_color():
    font_color = colorchooser.askcolor(title="Choose font color")
    text_area.config(fg=font_color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get(), font_style.get()))

def copy():
    text_area.event_generate("<<Copy>>")

def cut(): 
    text_area.event_generate("<<Cut>>")

def paste():
    text_area.event_generate("<<Paste>>")

def create_new_file():
    window.title("Untitled")
    # delete the text
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    
    # read the file
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)
        file = open(file, "r")
        text_area.insert(1.0, file.read())
    except Exception:
        print("Error reading file")
    finally:
        file.close()

def save_file():
    file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file is None:
        return
    else:
        try:
            # write on file
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
        except Exception:
            print("Error saving file")
        finally:
            file.close()

def about():
    showinfo("About", "This is a simple text editor written in Python by FelicityBlue.")

def exit():
    window.destroy()

# dark mode light mode bee mode
def set_mode(*args):
    fg_color = ""
    bg_color = ""
    if(mode.get() == "dark"):
        bg_color = "black"
        fg_color = "white"
    elif(mode.get() == "light"):
        bg_color = "linen"
        fg_color = "black"
    elif(mode.get() == "bee"):
        bg_color = "gold"
        fg_color = "black"
        font_style.set("bold")
        font_size.set(18)
    elif(mode.get() == "barbie"):
        bg_color = "hot pink"
        fg_color = "white"
        font_size.set(15)
    else:
        return
    text_area.configure(bg = bg_color)
    text_area.config(font=(font_name.get(), font_size.get(), font_style.get()), fg = fg_color)

window = Tk()
window.title("Text Editor")
file = None

# width of height of the editor
window_width = 350
window_height = 350

# get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

mode = StringVar(window)
mode.set("light")

# set default font's properties
font_name = StringVar(window)
font_name.set("Times New Roman")

font_size = StringVar(window)
font_size.set("12")

font_style = StringVar(window)
font_style.set("normal")

font_color = StringVar(window)
font_color.set("black")

text_area = Text(window, font=(font_name.get(), font_size.get(), font_style.get()), fg=font_color.get())
set_mode(mode)
text_area.grid(padx=5, pady=5)

scroll_bar = Scrollbar(text_area) 
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

# widgets
frame = Frame(window)
frame.grid()

# change font

button_font = OptionMenu(frame, font_name, *font.families(), command=change_font)
button_font.grid(row=0, column=0)

button_color = Button(frame, text="font color", command=change_font_color)
button_color.grid(row=0, column=1)

button_style = OptionMenu(frame, font_style, "normal", "bold", "italic", "underline", command=change_font)
button_style.grid(row=0, column=2)

button_size = Spinbox(frame, from_= 8, to_= 100, textvariable= font_size, command = change_font)
button_size.grid(row=1, column=0)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=create_new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()

palette_menu = Menu(edit_menu, tearoff=0)
edit_menu.add_cascade(label="Palette", menu=palette_menu)
palette_menu.add_command(label= "light", command = lambda:[mode.set("light"), set_mode()])
palette_menu.add_command(label= "dark", command = lambda:[mode.set("dark"), set_mode()])
palette_menu.add_command(label= "bee", command = lambda:[mode.set("bee"), set_mode()])
palette_menu.add_command(label= "barbie", command = lambda:[mode.set("barbie"), set_mode()])   


about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=about_menu)
about_menu.add_command(label="About Us")

scroll_bar.pack(side=RIGHT, fill=Y)
scroll_bar.config(command=text_area.yview)

window.mainloop()