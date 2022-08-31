from tkinter import *
from datetime import date
import os

root = Tk()
root.title("Age Calculator App")

root.geometry("1280x825")
root.resizable(False, False)
# root.iconbitmap("./Photos/data2.ico")
root.iconbitmap("E:\images\date2.ico")


def register():
    global root
    root = Toplevel(root)
    root.title("Register")
    root.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(root, text="Please enter details below", bg="blue").pack()
    Label(root, text="").pack()
    username_lable = Label(root, text="Username * ")
    username_lable.pack()
    username_entry = Entry(root, textvariable=username)
    username_entry.pack()
    password_lable = Label(root, text="Password * ")
    password_lable.pack()
    password_entry = Entry(root, textvariable=password, show='*')
    password_entry.pack()
    Label(root, text="").pack()
    Button(root, text="Register", width=10, height=1,
           bg="blue", command=register_user).pack()


def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(root, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()


def login():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10,
           height=1, command=login_verify).pack()

# Designing window for login


def login():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10,
           height=1, command=login_verify).pack()

# Implementing event on register button


def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(root, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()

# Implementing event on login button


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           command=delete_login_success).pack()

# Designing popup for login invalid password


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()

# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()

# Deleting popups


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


frameAuth = Frame(root, width=400,  height=150,
                  highlightcolor="#a59fd5", highlightthickness=2)
frameAuth.place(x=50, y=-20)

b1 = Button(frameAuth, text="Login", fg="#dad9da",
            bg='#3E497A',  width="50", command=login)
b1.place(x=-70, y=50)

b2 = Button(frameAuth, text="register", fg="#dad9da",
            bg='#3E497A',  width="50", command=register)
b2.place(x=-70, y=100)


def calculate():
    time = date.today()
    # =========
    year = int(enterY.get())
    month = int(enterM.get())
    day = int(enterD.get())
    # =========

    age = time.year - year - ((time.month, time.day) < (month, day))
    age1 = StringVar()
    age1.set(str(age))

    birthday = Label(frameFunc, text="Your age is:", font=(
        "Overpass Mono", 13, "bold"), fg="#F9D371", bg="#5584AC")
    birthday.place(x=65, y=400)

    display = Entry(frameFunc, textvariable=age1, bg="#3E497A", fg="#F9D371", font=("Overpass Mono", 13, "bold"), justify=CENTER, highlightbackground="#F9D371",
                    highlightcolor="#3E497A", highlightthickness=2)
    display.place(x=60, y=450)


photo = PhotoImage(file="E:\images\main2.png")
image = Label(root, image=photo,  width=1080, height=825)
image.place(x=260, y=-30)

frameFunc = Frame(root, width=350, bg="#668ee2",  height=500,
                  highlightbackground="#71b4e2", highlightcolor="#a59fd5", highlightthickness=2)
frameFunc.place(x=40, y=170)


photo2 = PhotoImage(file="E:\images\date1.png")
image2 = Label(frameFunc, image=photo2, bg="#668ee2")
image2.place(x=110, y=0)


instraction = Label(frameFunc, text="Please Enter your birthday:", font=(
    "Overpass Mono", 13, "bold"), fg="white", bg="#668ee2")
instraction.place(x=10, y=140)

enterY = Entry(frameFunc, bg="#a59fd5", fg="#dad9da", font=("Overpass Mono", 13, "bold"), justify=CENTER, highlightbackground="#71b4e2",
               highlightcolor="#a59fd5", highlightthickness=2)
enterY.place(x=90, y=200)

textY = Label(frameFunc, text="Year", font=(
    "Overpass Mono", 11, "bold"), fg="#71b4e2")
textY.place(x=35, y=200)


enterM = Entry(frameFunc, bg="#a59fd5", fg="#dad9da", font=("Overpass Mono", 13, "bold"), justify=CENTER, highlightbackground="#71b4e2",
               highlightcolor="#a59fd5", highlightthickness=2)
enterM.place(x=90, y=250)

textM = Label(frameFunc, text="Month", font=(
    "Overpass Mono", 11, "bold"), fg="#71b4e2", )
textM.place(x=25, y=250)


enterD = Entry(frameFunc, bg="#a59fd5", fg="#dad9da", font=("Overpass Mono", 13, "bold"), justify=CENTER, highlightbackground="#71b4e2",
               highlightcolor="#a59fd5", highlightthickness=2)
enterD.place(x=90, y=300)

textD = Label(frameFunc, text="Day", font=(
    "Overpass Mono", 11, "bold"), fg="#71b4e2")
textD.place(x=42, y=300)


b = Button(frameFunc, width=50, bg="#a59fd5", fg="#dad9da", text="Calculate", font=(
    "Overpass Mono", 10, "bold"), activebackground="#22577E", activeforeground="white", command=calculate)
b.place(x=-30, y=350)


# Header UI

menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)


menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

# create the Window menu
window_menu = Menu(
    menubar,
    tearoff=0
)

window_menu.add_command(label='appearance')
window_menu.add_command(label='contact us')

menubar.add_cascade(
    label="View",
    menu=window_menu,
    underline=0
)


# create the View menu
view_menu = Menu(
    menubar,
    tearoff=0
)

view_menu.add_command(label='Setup')
view_menu.add_command(label='Restart')

menubar.add_cascade(
    label="Window",
    menu=view_menu,
    underline=0
)


# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)

root.mainloop()
