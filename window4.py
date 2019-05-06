from tkinter import *
import tkinter as tk
from create_window4 import AddStudent as astd
from edit_window4 import EditStudent as edtstd
from add_student_data4 import DatabaseManage

class MainWindow(tk.Frame):

	def __init__(self, parent):
		global rootWindow
		global lstt
		global db
		global listbox

		db = DatabaseManage()
 
		lstt = db.viewData()

		rootWindow = parent
		tk.Frame.__init__(self, parent)
		self.parent = parent
		l=Label(parent,bg="white",text="Hospital Management System",font=("Helvetica 17 bold"))
		l.grid(row=0,column=0,columnspan=4,padx=15,pady=15)
		b=Button(parent,text="Add New Patient",bg="#ffcccc", fg="black",command= lambda: create())
		b.grid(row=1,column=0,sticky=W,padx=15,pady=5)
		
		b2 = Button(parent,text="Reload",bg="#ffcccc", fg="black",command= lambda: refresh())
		b2.grid(row=1,column=1,sticky=W,padx=5,pady=5)
		
		b3 = Button(parent,text="Edit",bg="#ffcccc", fg="black",command= lambda: editData())
		b3.grid(row=1,column=2,sticky=W,padx=5,pady=5)
		
		b4 = Button(parent,text="Delete",bg="#ffcccc", fg="black",command= lambda: deleteData())
		b4.grid(row=1,column=3,sticky=E,padx=15,pady=5)
		
		listbox = Listbox(parent,selectmode=SINGLE, width=55, height=10)
		listbox.grid(row=2,column=0,columnspan=4,sticky=W,padx=15,pady=5)
		listbox.insert("end", *lstt)
# 		scrollbar = Scrollbar(parent, orient=VERTICAL)
# 		scrollbar.grid(row=3,column=1,pady=5)
# 		scrollbar.config(command=listbox.yview)

def create():
	root = tk.Toplevel(rootWindow)
	root.title("Add Student")
	root.resizable(False,False)
	astd(root).grid()
	root.mainloop()
	
def refresh():
	lstt = db.viewData()
	listbox.delete(0, tk.END)
	listbox.insert("end", *lstt)
	
def deleteData():
	listItem = listbox.curselection()
	text = listbox.get(listItem)
	
	arr = text.split(" ")
	db.delData(arr[0])
	lstt = db.viewData()
	listbox.delete(0, tk.END)
	listbox.insert("end", *lstt)

def editData():
	listItem = listbox.curselection()
	if listItem == ():
		print("Atleast select an item to edit")
	else:
		text = listbox.get(listItem)
		arr = text.split(" ")
		
		root = tk.Toplevel(rootWindow)
		root.title("Edit Student")
		root.resizable(False,False)
		edtstd(root, arr[0]).grid()
		root.mainloop()