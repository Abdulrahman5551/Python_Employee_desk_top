from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

import sqlite3
import random


class Employee:

    @staticmethod
    def get_date_year():
        list_year = []
        for data in range(1950, 2023):
            list_year.append(data)
        return list_year

    @staticmethod
    def get_date_month():
        list_month = []
        for month in range(1, 13):
            list_month.append(month)
        return list_month

    @staticmethod
    def get_date_day():
        list_day = []
        for day in range(1, 32):
            list_day.append(day)
        return list_day

    def __init__(self, root):
        self.root = root

        # Main window
        self.root.title('Employee Management System')
        self.root.geometry('1210x615+0+0')
        self.root.resizable(False, False)
        self.root.config(bg='#6CD1A3')

        # ----- Variables Frame Tools
        self.full_name_var = StringVar()
        self.job_var = StringVar()
        self.phone_var = StringVar()
        self.email_var = StringVar()
        self.date_year_var = StringVar()
        self.date_month_var = StringVar()
        self.date_day_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()

        # ----------- Start Frame Tools
        self.tools_frame = Frame(self.root, bg='#6CD1A3')
        self.tools_frame.place(x=1, y=1, width=360, height=470)

        self.hide_button = Button(self.tools_frame, text="HIDE", cursor="hand2", bd="3", command=self.get_hide)
        self.hide_button.place(x=260, y=10) # Button hide screen

        self.show_button = Button(self.tools_frame, text="SHOW", cursor="hand2", bd="3", command=self.get_show)
        self.show_button.place(x=310, y=10) # Button show screen

        # Title frame tools
        self.title = Label(self.tools_frame, text='Employee Company', font=('Calibre', 18, 'bold'), bg='#6CD1A3', fg='#3D533F')
        self.title.place(x=10, y=1)

        # Label and Entry's data
        self.label_name = Label(self.tools_frame, text="Name: ", font=('Calibre', 16), bg='#6CD1A3', fg='#3D533F')
        self.label_name.place(x=10, y=50)

        self.entry_name = Entry(self.tools_frame, width=19, font=('Calibre', 15), bg="white", fg="black",
                                justify="center", textvariable=self.full_name_var)
        self.entry_name.place(x=122, y=50)

        self.label_job = Label(self.tools_frame, text="Job: ", font=('Calibre', 16), bg='#6CD1A3', fg='#3D533F')
        self.label_job.place(x=10, y=90)

        self.entry_job = Entry(self.tools_frame, width=19, font=('Calibre', 15),
                          bg="white", fg="black", justify="center", textvariable=self.job_var)
        self.entry_job.place(x=122, y=90)

        label_phone = Label(self.tools_frame, text="Phone: ", font=('Calibre', 16), bg='#6CD1A3', fg='#3D533F')
        label_phone.place(x=10, y=130)

        self.entry_phone = Entry(self.tools_frame, width=19, font=('Calibre', 15),
                            bg="white", fg="black", justify="center", textvariable=self.phone_var)
        self.entry_phone.place(x=122, y=130)

        self.label_emil = Label(self.tools_frame, text="Email: ", font=('Calibre', 16), bg='#6CD1A3', fg='#3D533F')
        self.label_emil.place(x=10, y=170)

        self.entry_emil = Entry(self.tools_frame, width=19, font=('Calibre', 15),
                           bg="white", fg="black", justify="center", textvariable=self.email_var)
        self.entry_emil.place(x=122, y=170)

        self.label_date = Label(self.tools_frame, text="Birth Date: ", font=('Calibre', 16), bg='#6CD1A3', fg='#3D533F')
        self.label_date.place(x=10, y=210)

        self.combobox_data_year = ttk.Combobox(self.tools_frame, state='readonly', width=4, font=('Calibre', 14),
                                               textvariable=self.date_year_var)
        self.combobox_data_year['values'] = Employee.get_date_year()
        self.combobox_data_year.place(x=121, y=210)

        self.combobox_data_month = ttk.Combobox(self.tools_frame, state='readonly', width=4, font=('Calibre', 14),
                                                textvariable=self.date_month_var)
        self.combobox_data_month['values'] = Employee.get_date_month()
        self.combobox_data_month.place(x=195, y=210)

        self.combobox_data_day = ttk.Combobox(self.tools_frame, state='readonly', width=4,font=('Calibre', 14),
                                              textvariable=self.date_day_var)
        self.combobox_data_day['values'] = Employee.get_date_day()
        self.combobox_data_day.place(x=270, y=210)

        label_gender = Label(self.tools_frame, text="Gender: ", font=('Calibre', 16), bg='#6CD1A3', fg='#3D533F')
        label_gender.place(x=10, y=250)

        self.combobox_gender = ttk.Combobox(self.tools_frame, state='readonly', width=10, font=('Calibre', 16),
                                            textvariable=self.gender_var)
        self.combobox_gender["value"] = ["Male", "Female"]
        self.combobox_gender.place(x=120, y=250)

        self.label_address = Label(self.tools_frame, text="Address: ", font=('Calibre', 16), bg='#6CD1A3', fg='#3D533F')
        self.label_address.place(x=10, y=290)

        self.text_address = Text(self.tools_frame, width=19, height=2, font=('Calibre', 14))
        self.text_address.place(x=120, y=290)

        # ----- Buttons Frame
        # ----- Start Buttons Frame
        self.button_frame = Frame(self.tools_frame, bg="#6CD1A3", bd=1, relief=SOLID)
        self.button_frame.place(x=8, y=358, width=348, height=100)

        self.button_add = Button(self.button_frame, text='Add Details', width=12, height=1, font=('Calibre', 16),
                            bg="#23EB0F", fg="black", command=self.insert_employee)
        self.button_add.place(x=4, y=5)

        self.button_update = Button(self.button_frame, text='Update Details', width=12, height=1, font=('Calibre', 16),
                               bg="#23EB0F", fg="black", command=self.update_employee)
        self.button_update.place(x=184, y=5)

        self.button_clear = Button(self.button_frame, text='Clear', width=12, height=1, font=('Calibre', 16),
                              bg="#23EB0F", fg="black", command=self.clear_all)
        self.button_clear.place(x=4, y=53)

        self.button_delete = Button(self.button_frame, text='Delete Details', width=12, height=1, font=('Calibre', 16),
                               bg="#EB2A0F", fg="black", command=self.delete_employee)
        self.button_delete.place(x=184, y=53)

        # ----- End Buttons Frame

        # ----- Start Table Frame
        self.tree_frame = Frame(self.root, bg="#8F94B3")
        self.tree_frame.place(x=365, y=4, width=875, height=607)

        self.table_tree = ttk.Treeview(self.tree_frame, columns=("1","2","3","4","5","6","7","8"), height=60)

        self.table_tree.heading("1", text="ID")
        self.table_tree.column("1", width=80, anchor="center")

        self.table_tree.heading("2", text="Name")
        self.table_tree.column("2", width=140, anchor="center")

        self.table_tree.heading("3", text="Job")
        self.table_tree.column("3", width=80, anchor="center")

        self.table_tree.heading("4", text="Phone")
        self.table_tree.column("4", width=100, anchor="center")

        self.table_tree.heading("5", text="Email")
        self.table_tree.column("5", width=140, anchor="center")

        self.table_tree.heading("6", text="Birth Date")
        self.table_tree.column("6", width=100, anchor="center")

        self.table_tree.heading("7", text="Gender")
        self.table_tree.column("7", width=80, anchor="center")

        self.table_tree.heading("8", text="Address")
        self.table_tree.column("8", width=140, anchor="center")

        self.table_tree['show'] = 'headings'
        self.table_tree.place(x=1, y=1, height=612)

        # ----- End Table Frame

        self.fetch_all()
        self.table_tree.bind("<ButtonRelease-1>", self.set_cursor)

    def get_hide(self):
        self.root.geometry("365x615+450+20")

    def get_show(self):
        self.root.geometry('1210x615+0+0')

    def insert_employee(self):

        db = sqlite3.connect("C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Employee_project_2\\database\\employee.db")
        cursor = db.cursor()

        def create_id():
            random_1 = random.randint(100, 500)
            random_2 = random.randint(500, 999)

            return str(random_1)+str(random_2)
        name = self.full_name_var.get()
        job = self.job_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        date_y = self.date_year_var.get()
        date_m = self.date_month_var.get()
        date_d = self.date_day_var.get()

        date_all = str(date_y)+"-"+str(date_m)+"-"+str(date_d)
        gender = self.gender_var.get()
        address = self.text_address.get("1.0", "end")

        get_id = create_id()
        if len(name) > 1 and len(job) > 0 and len(phone) > 3 and len(date_all) > 5 and len(email) > 2\
                and len(gender) >= 4 and len(address) >= 5:

            sql = f"INSERT INTO employee_tb(id, name, job, phone, email, birth, gender, address)" \
                  f"VALUES('{get_id}', '{name}', '{job}', '{phone}', '{email}', '{date_all}', '{gender}', '{address}')"
            cursor.execute(sql)
            messagebox.showinfo("Done", "Insert New Recorde ..")
            db.commit()
            self.delete_children()
            self.fetch_all()
            self.clear_all()
            db.close()

        else:
            pass

    def delete_employee(self):
        db = sqlite3.connect("C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Employee_project_2\\database\\employee.db")
        cursor = db.cursor()

        if len(self.full_name_var.get()) > 0 and len(self.job_var.get()) > 0:
            cursor_row = self.table_tree.focus()
            contents = self.table_tree.item(cursor_row)
            row = contents['values']

            qu1 = messagebox.askquestion(f'Attention', f'It Will Be Deleted " {row[0]} ", are you sure?')
            if qu1 == 'yes':
                sql = f"DELETE FROM employee_tb WHERE id = {row[0]}"
                cursor.execute(sql)
                db.commit()
                messagebox.showinfo('Done', 'Succeed Delete..')
                db.close()
                self.clear_all()
                self.delete_children()
                self.fetch_all()

            else:
                pass

        else:
            pass

    def update_employee(self):
        db = sqlite3.connect("C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Employee_project_2\\database\\employee.db")
        cursor = db.cursor()

        name = self.full_name_var.get()
        job = self.job_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        date_y = self.date_year_var.get()
        date_m = self.date_month_var.get()
        date_d = self.date_day_var.get()
        date_all = str(date_y)+"-"+str(date_m)+"-"+str(date_d)
        gender = self.gender_var.get()
        address = self.text_address.get("1.0", "end")

        if len(name) > 0:
            cursor_row = self.table_tree.focus()
            contents = self.table_tree.item(cursor_row)
            row = contents['values']
            id_row = row[0]
            if len(str(id_row)) == 6:
                qu1 = messagebox.askquestion(f'Attention', f'It Will Be Change Details " {row[0]} ", are you sure?')
                if qu1 == 'yes':
                    sql = f"UPDATE employee_tb SET name = '{name}', job = '{job}', phone = '{phone}', email = '{email}'," \
                          f"birth = '{date_all}', gender = '{gender}', address = '{address}' WHERE id = '{row[0]}'"

                    cursor.execute(sql)
                    db.commit()
                    messagebox.showinfo('Done', 'Succeed Update..')
                    db.close()
                    self.clear_all()
                    self.delete_children()
                    self.fetch_all()

                else:
                    pass

            else:
                pass

        else:
            pass


    def clear_all(self):
        self.full_name_var.set('')
        self.job_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.date_year_var.set('')
        self.date_month_var.set('')
        self.date_day_var.set('')
        self.gender_var.set('')
        self.text_address.delete("1.0", END)

    def delete_children(self):
        for items in self.table_tree.get_children():
            self.table_tree.delete(items)

    def fetch_all(self):
        db = sqlite3.connect("C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Employee_project_2\\database\\employee.db")
        cursor = db.cursor()

        cursor.execute("SELECT * FROM employee_tb")
        rows = cursor.fetchall()

        if len(rows) != 0:
            self.table_tree.delete(*self.table_tree.children)

            for row in rows:
                self.table_tree.insert("", END, values=row)
            db.commit()
        db.close()

    def set_cursor(self, event):
        cursor_row = self.table_tree.focus()
        contents = self.table_tree.item(cursor_row)
        row = contents['values']

        date_y = row[5][0:4]
        date_m = row[5][5:6]
        date_d = row[5][7]

        self.full_name_var.set(row[1])
        self.job_var.set(row[2])
        self.phone_var.set(row[3])
        self.email_var.set(row[4])
        self.date_year_var.set(date_y)
        self.date_month_var.set(date_m)
        self.date_day_var.set(date_d)
        self.gender_var.set(row[6])
        self.text_address.delete("1.0", END)
        self.text_address.insert("1.0", row[7])


root_tk = Tk()
Employee(root_tk)
logo_1 = PhotoImage(file='C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Employee_project_2\\icons\\employee_1.png')
logo_2 = PhotoImage(file='C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Employee_project_2\\icons\\employee_2.png')

label_logo = Label(root_tk, image=logo_1, bg="#6CD1A3")
label_logo.place(x=30, y=491)

label_logo_2 = Label(root_tk, image=logo_2, bg="#6CD1A3")
label_logo_2.place(x=185, y=492)

root_tk.mainloop()