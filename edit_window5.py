import tkinter as tk
from tkinter import *
from add_student_data5 import DatabaseManage
class EditStudent(tk.Frame):
    
    def __init__(self, parent, id):
        global db
        global std_id
        std_id = id
        db = DatabaseManage()
        totalData = db.fetchData(id)
        global rootWindow
        rootWindow = parent
        global e1, e2
        tk.Frame.__init__(self, parent)
        self.parent = parent
        
        l=Label(parent,bg="white",text="Hospital Management System",font=("Helvetica 17 bold"))
        l.grid(row=0,column=0,columnspan=3,padx=15,pady=15)
        
        lbl2 = Label(parent, text="PATIENT NAME : ").grid(row=1, sticky=E, pady=5)
        lbl3 = Label(parent, text="AGE: : ").grid(row=2, sticky=E)
        #lbl4 = Label(parent, text="ADDRESS:: : ").grid(row=3, sticky=E)
        e1 = Entry(parent)
        e2 = Entry(parent)
        #e3 = Entry(parent)
        e1.grid(row=1, column=1, pady=5)
        e2.grid(row=2, column=1)
        #e3.grid(row=3, column=1)
        e1.insert(0, totalData[0][0])
        e2.insert(0, totalData[0][1])
        #e3.insert(0, totalData[0][2])
        

        b1=Button(parent, text="Update", width=10,bg="#ffcccc", fg="black",command= lambda: update_data())
        b1.grid(row=3, columnspan=3, pady=10)

        b=Button(parent,text="Close",bg="red", fg="white",command= lambda: deleteWindow())
        b.grid(row=3,column=2,columnspan=3,sticky=W,padx=15,pady=5)
 
def update_data():
    name = e1.get()
    classname = e2.get()
    e1.delete(0, END)
    e2.delete(0, END)
    db.updateData(std_id, name, classname)
        
def deleteWindow():
    rootWindow.destroy()
