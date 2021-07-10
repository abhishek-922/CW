from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
from datetime import date
import sqlite3
from contextlib import closing

connect = sqlite3.connect("my_teams.db")
cursor = connect.cursor()
"""cursor.execute("CREATE TABLE Meeting (MeetingID NOT NULL PRIMARY KEY,"
               " Title TEXT,"
               " Date TEXT,"
               " Time TEXT,"
               " Names TEXT)")"""
connect.commit()
connect.close()


def screen_geometry():
    width, height = 700, 670
    root.geometry('%dx%d+0+0' % (width, height))

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # root.geometry('%dx%d+0+0' % (screen_width, screen_height))
    # root.geometry("500x700")

    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    root.geometry('{}x{}+{}+{}'.format(width, height, x_cord, y_cord))


class meeting_functions:

    def __init__(self, master):
        self.master = master

        self.meeting_function_frame = Frame(self.master)
        self.meeting_function_frame.config(bg='white')

        self.add_details_frame = Frame(self.master)
        self.add_details_frame.config(bg='white')

        self.edit_details_frame = Frame(self.master)
        self.edit_details_frame.config(bg='white')

        # ______________________ function invoke ___________________________
        #self.meeting_function()
        #self.get_details()
        self.edit_meeting_1()

    def meeting_function(self):
        screen_geometry()
        bg = PhotoImage(file='logo.png')
        uni_label = Label(self.meeting_function_frame, image=bg, bg='white')
        uni_label.photo = bg
        uni_label.pack(pady=10)

        add_meeting_lbl = Button(self.meeting_function_frame, text='ADD MEETING', font=('calibri', '18'),
                                 command=lambda: self.change_to_add_meeting())
        add_meeting_lbl.place(x=230, y=150)

        edit_meeting_lbl = Button(self.meeting_function_frame, text='EDIT MEETING', font=('calibri', '18'))
        edit_meeting_lbl.place(x=230, y=280)

        delete_meeting_lbl = Button(self.meeting_function_frame, text='DELETE MEETING', font=('calibri', '18'))
        delete_meeting_lbl.place(x=230, y=410)
        self.meeting_function_frame.pack(fill='both', expand=1)

    def change_to_meeting_function(self):

        self.add_details_frame.forget()
        self.meeting_function_frame.pack(fill='both', expand=1)

    def change_to_add_meeting(self):

        self.add_details_frame.pack(fill='both', expand=1)
        self.meeting_function_frame.forget()

    def clear_details(self):

        self.title_entry.delete(0, 'end')
        self.date_entry.delete(0, 'end')
        self.time_entry.delete(0, 'end')
        self.notes_entry.delete(0, 'end')
        self.names_entry.delete(0, 'end')

    def get_details(self):

        bg = PhotoImage(file='logo.png')

        # ____________________________ frame starts _______________________________

        uni_label = Label(self.add_details_frame, image=bg, bg='white')
        uni_label.photo = bg
        uni_label.pack(pady=10)

        # ____________________________ add details label in the db _______________________

        lbl = Label(self.add_details_frame, text='ADDING DETAILS IN DATABASE', font=('calibri', '18'), bg='white')
        lbl.pack(pady=10)

        # ________________________________ Labels part 1 _____________________________________

        tit_lbl = Label(self.add_details_frame, text='ADD TITLE:')
        tit_lbl.config(font=('calibri', '15'), bg='white')
        tit_lbl.place(relx=0.05, rely=0.3)

        self.title = StringVar()
        self.title_entry = Entry(self.add_details_frame, font=('calibri', '14'), textvariable=self.title)
        self.title_entry.place(relx=0.21, rely=0.3)

        # ________________________________ Labels part 2 _____________________________________

        date_lbl = Label(self.add_details_frame, text='ADD DATE:')
        date_lbl.config(font=('calibri', '15'), bg='white')
        date_lbl.place(relx=0.05, rely=0.4)

        self.date = StringVar()
        self.date_entry = Entry(self.add_details_frame, bd=1, textvariable=self.date,
                                font=('calibri', '14'))
        self.date_entry.place(relx=0.21, rely=0.4)

        # ________________________________ Labels part 3 _____________________________________

        time_lbl = Label(self.add_details_frame, text='ADD TIME:')
        time_lbl.config(font=('calibri', '15'), bg='white')
        time_lbl.place(relx=0.05, rely=0.5)

        self.time = StringVar()
        self.time_entry = Entry(self.add_details_frame, bd=1, textvariable=self.time,
                           font=('calibri', '14'))
        self.time_entry.place(relx=0.21, rely=0.5)

        # ________________________________ Labels part 4 _____________________________________

        notes_lbl = Label(self.add_details_frame, text='ADD NOTES:')
        notes_lbl.config(font=('calibri', '15'), bg='white')
        notes_lbl.place(relx=0.55, rely=0.3)

        self.notes = StringVar()
        self.notes_entry = Entry(self.add_details_frame, bd=1, textvariable=self.notes,
                           font=('calibri', '14'))
        self.notes_entry.place(relx=0.55, rely=0.4)

        # ______________________________ Labels part 5 _______________________________________

        names_lbl = Label(self.add_details_frame, text='ADD NAMES:')
        names_lbl.config(font=('calibri', '15'), bg='white')
        names_lbl.place(relx=0.045, rely=0.6)

        self.names = StringVar()
        self.names_entry = Entry(self.add_details_frame, bd=1, textvariable=self.names,
                            font=('calibri', '14'))
        self.names_entry.place(relx=0.21, rely=0.6)

        # ______________________________ Add button __________________________________________________

        add_btn = Button(self.add_details_frame, text='ADD DETAILS TO D.B', font=('calibri', '15'), bg='#0096FF',
                         fg='white', command= lambda: self.add_meeting())
        add_btn.place(relx=0.35, rely=0.75)

        # _______________________________________________________________________________________________

    def add_meeting(self):
        answer = ms.askyesno('Meeting Details', 'Is there an existing meeting with the same details?')
        if answer:
            self.clear_details()
            self.change_to_meeting_function()
        else:
            ms.showinfo('Data', 'Data has been successfully transferred into the Data Base')
            connect = sqlite3.connect("my_teams.db")
            cursor = connect.cursor()
            cursor.execute("INSERT INTO Meeting (Title, Date, Time, Notes, Names) VALUES(?, ?, ?, ?, ?)",
                           (self.title.get(), self.date.get(), self.time.get(), self.notes.get(), self.names.get()))
            connect.commit()
            connect.close()
            self.clear_details()
            self.change_to_meeting_function()

        # _______________________________________________________________________________________________

    def edit_meeting_1(self):
        # delete screen geo function after non commenting above 2 functions in  init
        screen_geometry()

        bg = PhotoImage(file='logo.png')
        uni_label = Label(self.edit_details_frame, image=bg, bg='white')
        uni_label.photo = bg
        uni_label.pack(pady=10)

        edit_lbl = Label(self.edit_details_frame, text='EDIT MEETING DETAILS', font=('calibri', '18'), bg='white')
        edit_lbl.pack(pady=10)

        Lb_1 = Listbox(self.edit_details_frame, bg='white', height=5, width=55, font=('calibri', '15'), border=2)
        #Lb_1.pack(pady=40)

        connect = sqlite3.connect("my_teams.db")
        cursor = connect.cursor()
        # result = cursor.execute("SELECT * FROM Meeting").fetchall()
        # print(result)
        a = cursor.execute("SELECT MeetingID, Title, Date, Time, Names FROM Meeting").fetchall()
        # print(a)
        temp = list()
        for items in a:
            temp.append(items)
        # print("temp", temp)

        for x in temp:
            counter = 1
            Lb_1.insert(counter, x)
            # print("inserted", x)
            counter += 1

        connect.commit()
        connect.close()

        display_select_btn = Button(self.edit_details_frame, text='DISPLAY SELECTED', font=('calibri', '15'),
                                    bg='lightblue', command=lambda: self.selected_items(Lb_1))
        display_select_btn.pack(pady=5)


        # tree view

        my_tree = ttk.Treeview(self.edit_details_frame)
        my_tree['columns'] = ("meeting id", "title", "date", "time", "names")

        # format out cols
        my_tree.column("#0", width=120, minwidth=25)
        my_tree.column("meeting id", anchor=CENTER, width=120)
        my_tree.column("title", anchor=CENTER, width=120)
        my_tree.column("date", anchor=CENTER, width=120)
        my_tree.column("time", anchor=CENTER, width=120)
        my_tree.column("names", anchor=CENTER, width=120)

        # heading

        my_tree.heading("#0", text="Label", width=120, minwidth=25)
        my_tree.heading("")
        my_tree.heading("")
        my_tree.heading("")
        my_tree.heading("")
        my_tree.heading("")

        # insert

        my_tree.insert(parent='', index='end', )


        # temp packing
        self.edit_details_frame.pack(fill='both', expand=1)

    def selected_items(self, label_1):

        Listb = Text(self.edit_details_frame, bg='white', height=5, width=55, font=('calibri', '15'), border=2)
        Listb.pack(pady=10)

        for i in label_1.curselection():
            Lb_2 = Entry(self.edit_details_frame, bg='white', width=55, font=('calibri', '15'), border=2)
            # Lb_2.pack(pady=30)
            #print(label_1.get(i))
            # count = 0
            for e in label_1.get(i):
                Listb.insert(INSERT, e)
                Listb.insert(INSERT, '\n')
                #print(e, end='\n')
        #Listb.get('1.0', END)

        # edit button

        edit_btn = Button(self.edit_details_frame, text='EDIT', font=('calibri', '15'),
                          command=lambda: self.edit_meeting_2(Listb))
        edit_btn.pack(pady=10)

    def edit_meeting_2(self, edited_list):

        print("edited list \n", edited_list.get("1.0", END))
        temp2 = list()
        edited_title = edited_list.get("1.0")
        print("Meeting id", edited_title)


        print(temp2, end='')
        """connect = sqlite3.connect("my_teams.db")
        cursor = connect.cursor()
        cursor.execute("UPDATE Meeting SET Title=?, Date=?, Time=?, Names=? WHERE MeetingID=?",
                       (edited_list.get()))
        connect.commit()
        connect.close()"""


root = Tk()
call = meeting_functions(root)
root.mainloop()
