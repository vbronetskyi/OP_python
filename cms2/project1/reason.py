import mysql.connector
from tkinter import *
from tkinter import messagebox


class DB:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="rgukt123",database="test")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cab (cabid text, driver text, arrival text,destination text)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM cab")
        rows = self.cur.fetchall()
        return rows

    def insert(self):
        cabd=cabid_text.get()
        dri=driver_text.get()
        arr=arrival_text.get()
        dest=destination_text.get()
        self.cur.execute("INSERT INTO cab VALUES ('%s','%s','%s','%s')"%(cabd,dri, arr,dest))
        self.conn.commit()
        self.view()


    def delete(self):
        cabd=cabid_text.get()
        self.cur.execute("DELETE FROM cab WHERE cabid='%s'"% (cabd,))
        self.conn.commit()
        self.view()



db = DB()


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)

    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_command():
    list1.delete(0, END)
    for row in db.view():
        list1.insert(END, row)





window = Tk()

window.title("Cab Booking Form")


def on_closing():
    dd = db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        del dd


window.protocol("WM_DELETE_WINDOW", on_closing)  # handle window closing

l1 = Label(window, text="CabId",fg="green",font=("bold",12))
l1.grid(row=0, column=0)

l2 = Label(window, text="Driver",font=("bold",12),fg="green")
l2.grid(row=0, column=2)

l3 = Label(window, text="Arrival",font=("bold",12),fg="green")
l3.grid(row=1, column=0)

l4 = Label(window, text="Destination",font=("bold",12),fg="green")
l4.grid(row=1, column=2)

l5 = Label(window, text="Note:Please delete through CabIid!",bg="red",fg="white")
l5.grid(row=8, column=1)


cabid_text = StringVar()
e1 = Entry(window, textvariable=cabid_text,bg="white")
e1.grid(row=0, column=1)

driver_text = StringVar()
e2 = Entry(window, textvariable=driver_text,bg="white")
e2.grid(row=0, column=3)

arrival_text = StringVar()
e3 = Entry(window, textvariable=arrival_text,bg="white")
e3.grid(row=1, column=1)

destination_text = StringVar()
e4 = Entry(window, textvariable=destination_text,bg="white")
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12,fg="white",bg="black", command=view_command)
b1.grid(row=2, column=3)
#b1.pack()


b3 = Button(window, text="Add entry", width=12, fg="white",bg="black",command=db.insert)
b3.grid(row=4, column=3)


b5 = Button(window, text="Delete Cabid", width=12,fg="white",bg="black", command=db.delete)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12,fg="white",bg="black", command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
