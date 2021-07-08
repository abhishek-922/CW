import tkinter as tk
import tkinter.font as font
from tkinter import messagebox  # This gives access to message boxes.
from tkinter import simpledialog  # Used for single value data entry.
from tkinter import filedialog  # Returns the path to a file.
from tkinter import colorchooser
import sqlite3
from contextlib import closing
import os


connection = sqlite3.connect("Meetings.db")
cursor = connection.cursor()
# cursor.execute("CREATE TABLE Meeting_List (Title VARCHAR(255), Date TEXT, Time TEXT, Names VARCHAR(255))")


def screen_geometry():
    width, height = 500, 470
    # root.geometry('%dx%d+0+0' % (width, height))

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # root.geometry('%dx%d+0+0' % (screen_width, screen_height))

    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    root.geometry('{}x{}+{}+{}'.format(width, height, x_cord, y_cord))

class meeting_list:
    def __init__(self):
        pass
class attendance:
    def __init__(self):
        pass
class notes:
    def __init__(self):
        pass


def add_meeting():
    meeting_frame.forget()
    add_meet_frame.pack(fill='both', expand=1)


def login_page():
    txt = userid_entry.get()
    with open("members.txt", "r") as file:
        if txt in file.read():
            userid_frame.forget()
            password_frame.pack(fill='both', expand=1)
            entered_id.configure(text=txt, fg='#808080')
        else:
            messagebox.showwarning('Warning', 'Please Enter a valid username')


def back_to_signin():
    password_frame.forget()
    userid_frame.pack(fill='both', expand=1)


def change_to_meeting():
    password_ = str(password_entry.get())
    txt = str(userid_entry.get())
    if password_ == txt[0:-4] or password_ == "1":
        password_frame.forget()
        userid_frame.forget()
        meeting_frame.pack(fill='both', expand=1)
    else:
        messagebox.showerror('Error', 'Entered password does not match')


def if_exists():
    title = str(title_entry.get())
    date = str(dat_entry.get())
    time = str(time_entry.get())
    name1 = str(names_entry1.get())
    name2 = str(names_entry2.get())
    name3 = str(names_entry3.get())
    name4 = str(names_entry4.get())
    name5 = str(names_entry5.get())
#     print(title + date + time + name1 + name2 + name3 + name4 + name5)
    ans = messagebox.askyesno('Meeting', 'Meeting already exists ?')
    if ans:
        back_to_meeting_frame()
    elif not ans:
        cursor.execute("INSERT INTO Meeting_List "
                       f" VALUES('{title}', '{date}', '{time}', '{name1} {name2} {name3} {name4} {name5}')")

        updated = cursor.execute("SELECT * FROM Meeting_List").fetchall()
        print("updated database:", updated)
        messagebox.showinfo('Credentials', 'Information is added to the Meetings List')
        back_to_meeting_frame()


def back_to_meeting_frame():
    add_meet_frame.forget()
    edit_meet_frame.forget()
    meeting_frame.pack(fill='both', expand=1)


def edit_meeting():
    meeting_frame.forget()
    edit_meet_frame.pack(fill='both', expand=1)


def update_edit():
    edit_meet_frame.forget()
    empty_list.clear()
    data = cursor.execute("SELECT * FROM Meeting_List")
    for line in data:
        empty_list.append(line)

    print("updated list", empty_list)

    for x in empty_list:
        edit_db_entry = tk.Entry(edit_meet_frame)
        edit_db_entry.configure(font=('calibri', '14'), width=45)
        edit_db_entry.insert('end', x)
        edit_db_entry.pack()

    edit_meet_frame.pack(fill='both', expand=1)


# __________________Gui starts _____________
root = tk.Tk()
root.title("Meeting Portal")
screen_geometry()

# __________________fonts __________________
lbl_font = font.Font(family='Calibri',
                     size='22')
txt_font = font.Font(family='Calibri',
                     size='14')

# __________________ Menu Bar _______________
menu_bar = tk.Menu(root)
menu_bar.add_cascade(label='Exit', command=quit)

# __________________ Image _________________
uog_img = tk.PhotoImage(file='logo.png')

# ___________________Frames start ______________
userid_frame = tk.Frame(root)
userid_frame.config(bg='white')

password_frame = tk.Frame(root)
password_frame.configure(bg='white')

meeting_frame = tk.Frame(root)
meeting_frame.configure(bg='white')

add_meet_frame = tk.Frame(root)
add_meet_frame.config(bg='white')

edit_meet_frame = tk.Frame(root)
edit_meet_frame.config(bg='white')

delete_meet_frame = tk.Frame(root)
delete_meet_frame.config(bg='white')

# ___________________Data base entries ____________________

cursor.execute("INSERT INTO Meeting_List"
               f" VALUES('Hello World','4.4.2021', '12:00', 'Abhishek Aniruddh Amol Anuradha')")

cursor.execute("INSERT INTO Meeting_List"
               f" VALUES('Hello Python','5.6.2021', '11:00', 'Abhishek Aniruddh Anuradha')")

get1 = cursor.execute("SELECT * FROM Meeting_List").fetchall()

print("DataBase:", get1)

# __________________ User id frame starts __________________
uog_label = tk.Label(userid_frame, image=uog_img, bg='white')
uog_label.pack(pady=10)

sign_in_label = tk.Label(userid_frame,
                         text='Sign in',
                         font=lbl_font,
                         bg='white')

sign_in_label.pack(pady=15)

userid_entry = tk.Entry(userid_frame, font=txt_font, width=25)
userid_entry.configure(border=1)
userid_entry.pack(pady=20)

next_btn = tk.Button(userid_frame, text='Next', fg='white', bg='#0096FF')
next_btn.config(width=8, height=1,
                font=txt_font,
                command=login_page)
next_btn.pack(pady=20)

# _______________ password frame ________________
pass_label = tk.Label(password_frame, image=uog_img, bg='white')
pass_label.pack(pady=10)

entered_id = tk.Label(password_frame, font=txt_font, bg='white')
entered_id.pack(pady=10)

password_label = tk.Label(password_frame, text='Enter Password', font=lbl_font, bg='white')
password_label.pack(pady=5)

password_entry = tk.Entry(password_frame, font=txt_font, width=25)
password_entry.pack(pady=5)

Sign_in_btn = tk.Button(password_frame,
                        text='Sign in',
                        fg='white',
                        bg='#0096FF',
                        width=10, height=1,
                        font=txt_font,
                        command=change_to_meeting)
Sign_in_btn.pack(pady=20)

back_btn = tk.Button(password_frame,
                     text='Back', font=txt_font,
                     width=10, command=back_to_signin)
back_btn.pack()

# _____________meeting frame _________________

add_meet_ = tk.Button(meeting_frame,
                  text='Add Meeting',
                  bg='white',
                  font=txt_font,
                  command=add_meeting)
# add_meet_.pack(pady=15, ipady=5, ipadx=5)
add_meet_.place(y=140, x=100)

edit_meet_ = tk.Button(meeting_frame,
                  text='Edit Meeting',
                  bg='white',
                  font=txt_font,
                  command=edit_meeting)
# edit_meet_.pack(pady=15, ipady=5, ipadx=5)
edit_meet_.place(y=200, x=100)

del_meet_ = tk.Button(meeting_frame,
                  text='Delete Meeting',
                  bg='white',
                  font=txt_font)
del_meet_.place(y=260, x=100)

# _____________________add_meet_frame ____________________

add_meet_lbl = tk.Label(add_meet_frame, image=uog_img, bg='white')
add_meet_lbl.pack(pady=10)
# title
title_lbl = tk.Label(add_meet_frame,
                      text='Title: ',
                     font=('calibri', '17'),
                     bg='white')
title_lbl.place(x=50, y=75)

title_entry = tk.Entry(add_meet_frame,
                       font=txt_font)
title_entry.place(y=79, x=140)

# date
dat_lbl = tk.Label(add_meet_frame,
                       text='Date: ',
                       font=('calibri', '17'),
                       bg='white')
dat_lbl.place(x=50, y=115)

dat_entry = tk.Entry(add_meet_frame,
                         font=txt_font)
dat_entry.place(x=140, y=119)

# time
time_lbl = tk.Label(add_meet_frame,
                      text='Time: ',
                     font=('calibri', '17'),
                     bg='white')
time_lbl.place(x=50, y=155)

time_entry = tk.Entry(add_meet_frame,
                       font=txt_font)
time_entry.place(y=159, x=140)

# Names label
names_lbl = tk.Label(add_meet_frame,
                     text='Names: ',
                     font=('calibri', '17'),
                     bg='white')
names_lbl.place(x=50, y=195)

names_entry1 = tk.Entry(add_meet_frame,
                       font=txt_font)

names_entry1.place(x=140, y=199)

names_entry2 = tk.Entry(add_meet_frame,
                       font=txt_font)

names_entry2.place(x=140, y=239)

names_entry3 = tk.Entry(add_meet_frame,
                       font=txt_font)

names_entry3.place(x=140, y=279)

names_entry4 = tk.Entry(add_meet_frame,
                       font=txt_font)

names_entry4.place(x=140, y=319)

names_entry5 = tk.Entry(add_meet_frame, font=txt_font)

names_entry5.place(x=140, y=359)


add_btn = tk.Button(add_meet_frame,
                    text='Add Details',
                    fg='white',
                    bg='#0096FF',
                    width=10, height=1,
                    font=txt_font,
                    command=if_exists)
add_btn.place(y=399, x=220)

bck_btn = tk.Button(add_meet_frame,
                    text='Back',
                    width=10, height=1,
                    font=txt_font, command=back_to_meeting_frame)
bck_btn.place(y=399, x=360)
# _________________ edit meet frame __________________________
edit_meet_lbl = tk.Label(edit_meet_frame, image=uog_img, bg='white')
edit_meet_lbl.pack(pady=10)


Meet_btn = tk.Label(edit_meet_frame, text='MEETING LIST')
Meet_btn.configure(font=('Calibri', '18'), bg='#89CFF0', border=4)
Meet_btn.pack(pady=10)

empty_list = list()

data = cursor.execute("SELECT * FROM Meeting_List").fetchall()
for line in data:
    to_list = list(line)
    empty_list.append(to_list)

print("to list", empty_list)

for x in empty_list:
    edit_db_entry = tk.Listbox(edit_meet_frame)
    edit_db_entry.configure(font=('calibri', '14'), width=45)
    edit_db_entry.insert('end', x)
    edit_db_entry.pack()

edit = tk.Button(edit_meet_frame, text='Edit')
edit.configure(width=6, font=('calibri', '14'))
edit.pack(pady=10)

# ____________ deletion of entry widget ________________________
"""for x in empty_list:
    edit_db_entry.delete(0, 'end')

update_btn = tk.Button(edit_meet_frame, text='Update', command=update_edit)
update_btn.config(width=8, font=('calibri', '14'))
update_btn.pack(pady=10)

edit_back_btn = tk.Button(edit_meet_frame, text='Back', width=6, height=1, font=txt_font, command=back_to_meeting_frame)
edit_back_btn.pack(pady=10)"""

# _______________frame package ______________

userid_frame.pack(fill='both', expand=1)
# password_frame.pack(fill='both', expand=1)
# meeting_frame.pack(fill='both', expand=1)
# add_meet_frame.pack(fill='both', expand=1)
# edit_meet_frame.pack(fill='both', expand=1)
# delete_meet_frame.pack(fill='both', expand=1)

"""with closing(sqlite3.connect("test.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()"""

root.config(menu=menu_bar)
root.mainloop()


