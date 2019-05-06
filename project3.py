
from tkinter import*
from main import*
from main1 import*
from main2 import*
from main3 import*
from main4 import*
from main5 import*
from main6 import*
from main7 import*
from main8 import*
import sqlite3
from login import*
# tk=Tk()
# tk.geometry('800x800')
# tk.configure(bg="purple")
def new():
	tk1=Tk()
	tk1.geometry('800x800')
	tk1.configure(bg="sky blue")

	def new1():
		tk2=Tk()
		tk2.geometry('800x800')
		tk2.configure(bg="yellow")
		def newdata():
			main()
			# database()
			# database1()
			# database2()
			# database3()





		lable0=Label(tk2,text="DOCTOR LIST:",width=13,font=("bold",25),bg="blue",fg="black")
		lable0.grid(row=1,column=0)

		lable1=Label(tk2,text=" 1 :",width=20,font=("bold",25),bg="green",fg="black")
		lable1.grid(row=2,column=0)
		btn1=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:main(),font=('arial',20,'bold'),text="DR.SOURAV NAGA ")
		btn1.grid(row=2,column=1)

		lable2=Label(tk2,text=" 2 :",width=20,font=("bold",25),bg="green",fg="black")
		lable2.grid(row=3,column=0)
		btn2=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main5(),text="DR.S CHOWDHURY")
		btn2.grid(row=3,column=1)

		lable3=Label(tk2,text=" 3 :",width=20,font=("bold",25),bg="green",fg="black")
		lable3.grid(row=4,column=0)
		btn3=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main6(),text="  DR.N MAJUMDAR ")
		btn3.grid(row=4,column=1)
		# lable4=Label(tk2,text=" 4 :",width=20,font=("bold",25),bg="green",fg="black")
		# lable4.grid(row=5,column=0)
		# btn4=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main(),text="  DR.SUJOY DA      ")
		# btn4.grid(row=5,column=1)
		# lable5=Label(tk2,text=" 5 :",width=20,font=("bold",25),bg="green",fg="black")
		# lable5.grid(row=6,column=0)
		# btn5=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main(),text="  DR.PUCHKI          ")
		# btn5.grid(row=6,column=1)
		btn6=Button(tk2,text='EXIT',padx=16,pady=14,bd=8,bg='purple',fg='black',command=tk2.destroy,font=('arial',20,'bold'))
		btn6.grid(row=7,column=0)
		tk2.mainloop()
#############################################################################################################################################################

	def new2():
		tk2=Tk()
		tk2.geometry('800x800')
		tk2.configure(bg="yellow")
		def newdata():
			main()
			# database()
			# database1()
			# database2()
			# database3()





		lable0=Label(tk2,text="DOCTOR LIST:",width=13,font=("bold",25),bg="blue",fg="black")
		lable0.grid(row=1,column=0)

		lable1=Label(tk2,text=" 1 :",width=20,font=("bold",25),bg="green",fg="black")
		lable1.grid(row=2,column=0)
		btn1=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:main1(),font=('arial',20,'bold'),text="     DR.TKM      ")
		btn1.grid(row=2,column=1)

		lable2=Label(tk2,text=" 2 :",width=20,font=("bold",25),bg="green",fg="black")
		lable2.grid(row=3,column=0)
		btn2=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main7(),text=" DR.S MISHRA ")
		btn2.grid(row=3,column=1)

		lable3=Label(tk2,text=" 3 :",width=20,font=("bold",25),bg="green",fg="black")
		lable3.grid(row=4,column=0)
		btn3=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main7(),text="  DR.N N JANA ")
		btn3.grid(row=4,column=1)
		btn6=Button(tk2,text='EXIT',padx=16,pady=14,bd=8,bg='purple',fg='black',command=tk2.destroy,font=('arial',20,'bold'))
		btn6.grid(row=7,column=0)
		tk2.mainloop()



############################################################################################################################################

	def new3():
		tk2=Tk()
		tk2.geometry('800x800')
		tk2.configure(bg="yellow")
		def newdata():
			main()
			# database()
			# database1()
			# database2()
			# database3()





		lable0=Label(tk2,text="DOCTOR LIST:",width=13,font=("bold",25),bg="blue",fg="black")
		lable0.grid(row=1,column=0)

		lable1=Label(tk2,text=" 1 :",width=20,font=("bold",25),bg="green",fg="black")
		lable1.grid(row=2,column=0)
		btn1=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:main22(),font=('arial',20,'bold'),text="   DR.SOURAV   ")
		btn1.grid(row=2,column=1)

		lable2=Label(tk2,text=" 2 :",width=20,font=("bold",25),bg="green",fg="black")
		lable2.grid(row=3,column=0)
		btn2=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main22(),text=" DR.B MISHRA ")
		btn2.grid(row=3,column=1)

		lable3=Label(tk2,text=" 3 :",width=20,font=("bold",25),bg="green",fg="black")
		lable3.grid(row=4,column=0)
		btn3=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main22(),text=" DR.N P GHOSH")
		btn3.grid(row=4,column=1)
		btn6=Button(tk2,text='EXIT',padx=16,pady=14,bd=8,bg='purple',fg='black',command=tk2.destroy,font=('arial',20,'bold'))
		btn6.grid(row=7,column=0)
		tk2.mainloop()



###########################################################################################################################################33
	def new4():
		tk2=Tk()
		tk2.geometry('800x800')
		tk2.configure(bg="yellow")
		def newdata():
			main()
			# database()
			# database1()
			# database2()
			# database3()





		lable0=Label(tk2,text="DOCTOR LIST:",width=13,font=("bold",25),bg="blue",fg="black")
		lable0.grid(row=1,column=0)

		lable1=Label(tk2,text=" 1 :",width=20,font=("bold",25),bg="green",fg="black")
		lable1.grid(row=2,column=0)
		btn1=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:main3(),font=('arial',20,'bold'),text="  DR.JAYDEV  ")
		btn1.grid(row=2,column=1)

		lable2=Label(tk2,text=" 2 :",width=20,font=("bold",25),bg="green",fg="black")
		lable2.grid(row=3,column=0)
		btn2=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main3(),text=" DR.K MISHRA ")
		btn2.grid(row=3,column=1)

		lable3=Label(tk2,text=" 3 :",width=20,font=("bold",25),bg="green",fg="black")
		lable3.grid(row=4,column=0)
		btn3=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main3(),text="  DR.N R DAS ")
		btn3.grid(row=4,column=1)

		btn6=Button(tk2,text='EXIT',padx=16,pady=14,bd=8,bg='purple',fg='black',command=tk2.destroy,font=('arial',20,'bold'))
		btn6.grid(row=7,column=0)
		tk2.mainloop()





####################################################################################################################################

	def new5():
		tk2=Tk()
		tk2.geometry('800x800')
		tk2.configure(bg="yellow")
		def newdata():
			main()
			# database()
			# database1()
			# database2()
			# database3()





		lable0=Label(tk2,text="DOCTOR LIST:",width=13,font=("bold",25),bg="blue",fg="black")
		lable0.grid(row=1,column=0)

		lable1=Label(tk2,text=" 1 :",width=20,font=("bold",25),bg="green",fg="black")
		lable1.grid(row=2,column=0)
		btn1=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:main4(),font=('arial',20,'bold'),text=" DR.K L DHOR ")
		btn1.grid(row=2,column=1)

		lable2=Label(tk2,text=" 2 :",width=20,font=("bold",25),bg="green",fg="black")
		lable2.grid(row=3,column=0)
		btn2=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main4(),text=" DR.K MISHRA ")
		btn2.grid(row=3,column=1)

		lable3=Label(tk2,text=" 3 :",width=20,font=("bold",25),bg="green",fg="black")
		lable3.grid(row=4,column=0)
		btn3=Button(tk2,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:main4(),text="  DR.k N dHOR ")
		btn3.grid(row=4,column=1)
		btn6=Button(tk2,text='EXIT',padx=16,pady=14,bd=8,bg='purple',fg='black',command=tk2.destroy,font=('arial',20,'bold'))
		btn6.grid(row=7,column=0)
		tk2.mainloop()
##################################################################################################################################3

	lable0=Label(tk1,text=" PLEASE SELECT ANYONE :",width=25,font=("bold",25),bg="blue",fg="black")
	lable0.grid(row=1,column=0)



	lable1=Label(tk1,text=" 1 :",width=20,font=("bold",25),bg="green",fg="black")
	lable1.grid(row=2,column=0)
	btn0=Button(tk1,padx=16,pady=14,bd=8,fg="black",bg="pink",command=lambda:new1(),font=('arial',20,'bold'),text="SKIN SPECALIST")
	btn0.grid(row=2,column=1)
	lable2=Label(tk1,text=" 2 :",width=20,font=("bold",25),bg="green",fg="black")	
	lable2.grid(row=3,column=0)

	btn1=Button(tk1,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:new2(),text="GYNOCOLOGIST")
	btn1.grid(row=3,column=1)

	lable3=Label(tk1,text=" 3 :",width=20,font=("bold",25),bg="green",fg="black")
	lable3.grid(row=4,column=0)
	btn2=Button(tk1,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:new3(),text=" NEUROLOGIST ")
	btn2.grid(row=4,column=1)

	lable4=Label(tk1,text=" 4 :",width=20,font=("bold",25),bg="green",fg="black")
	lable4.grid(row=5,column=0)
	btn3=Button(tk1,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:new4(),text="CARDIOLOGIST")
	btn3.grid(row=5,column=1)


	lable5=Label(tk1,text=" 5 :",width=20,font=("bold",25),bg="green",fg="black")
	lable5.grid(row=6,column=0)
	btn4=Button(tk1,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:new5(),text="NEFROLOGIST")
	btn4.grid(row=6,column=1)

	# lable6=Label(tk1,text=" 6 :",width=20,font=("bold",25),bg="green",fg="black")
	# lable6.grid(row=7,column=0)
	# btn5=Button(tk1,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),text="PSYCHIATRIST")
	# btn5.grid(row=7,column=1)




	btn6=Button(tk1,text='EXIT',padx=16,pady=14,bd=8,bg='purple',fg='black',command=tk1.destroy,font=('arial',20,'bold'))
	btn6.grid(row=8,column=0)






























	tk1.mainloop()


















# lable0=Label(tk,text=" WELCOME TO CEMK HOSPITAL",width=40,font=("bold",25),bg="yellow",fg="black")
# lable0.grid(row=1,column=0)
# btn0=Button(tk,padx=16,pady=14,bd=8,fg="black",bg="pink",font=('arial',20,'bold'),command=lambda:new(),text="PLEASE CLICK HERE")
# btn0.grid(row=2,column=0)
# btn1=Button(tk,text='EXIT',padx=16,pady=14,bd=8,bg='yellow',fg='black',command=tk.destroy,font=('arial',20,'bold'))
# btn1.grid(row=8,column=0)
# tk.mainloop()
# from babaai import*