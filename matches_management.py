

######### MATCH_TABLE MANAGEMENT #########

from tkinter import *
import tkinter.messagebox
import backend

class match:
	def __init__(self, root):
		self.root=root
		self.root.title("Online Match Ticket Booking System")
		self.root.geometry("1350x750+0+0")
		self.root.config(bg="#1e1f10")

		
		match_id=StringVar()
		home=StringVar()
		away=StringVar()
		duration=StringVar()

		#Fuctions
		def iExit():
			iExit=tkinter.messagebox.askyesno("Online Ticket Management System", "Do you want to exit?")
			if iExit>0:
				root.destroy()
			return

		def clcdata():
			self.txtmatch_id.delete(0,END)
			self.txthome.delete(0,END)
			self.txtduration.delete(0,END)
			self.txtaway.delete(0,END)

		def adddata():
			if(len(match_id.get())!=0):
				backend.addMatches(match_id.get(),home.get(),away.get(),duration.get())
				matchList.delete(0,END)
				matchList.insert(END,(match_id.get(),home.get(),away.get(),duration.get()))

		def disdata():
			matchList.delete(0,END)
			for row in backend.viewMatches():
				matchList.insert(END, row, str(""))

		def matchrec(event):
			global sd
			searchmatch=matchList.curselection()[0]
			sd=matchList.get(searchmatch)
			self.txtmatch_id.delete(0,END)
			self.txtmatch_id.insert(END,sd[1])
			self.txthome.delete(0,END)
			self.txthome.insert(END,sd[2])
			self.txtaway.delete(0,END)
			self.txtaway.insert(END,sd[3])
			self.txtduration.delete(0,END)
			self.txtduration.insert(END,sd[4])

		def deldata():
			if(len(match_id.get())!=0):
				backend.deleteMatches(sd[0])
				clcdata()
				disdata()

		def searchdb():
			matchList.delete(0,END)
			for row in backend.searchMatches(match_id.get(),home.get(),away.get(),duration.get()):
				matchList.insert(END, row, str(""))

		def updata():
			if(len(match_id.get())!=0):
				backend.deleteMatches(sd[0])
			if(len(match_id.get())!=0):
				backend.addMatches(match_id.get(),home.get(),away.get(),duration.get())
				matchList.delete(0,END)
				matchList.insert(END,(match_id.get(),home.get(),away.get(),duration.get()))

		#Frames
		MainFrame=Frame(self.root, bg="#1e1f10")
		MainFrame.grid()

		TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="#1e1f10", relief=RIDGE)
		TFrame.pack(side=TOP)

		self.TFrame=Label(TFrame, font=('Arial', 51, 'bold'), text="ONLINE MATCH TICKET BOOKING SYSTEM", bg="#1e1f10", fg="white")
		self.TFrame.grid() 

		BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="#1e1f10", relief=RIDGE)
		BFrame.pack(side=BOTTOM)

		DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="#1e1f10", relief=RIDGE)
		DFrame.pack(side=BOTTOM)

		DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="#1e1f10", relief=RIDGE, font=('Arial', 20, 'bold'), text="Match Information\n", fg="white")
		DFrameL.pack(side=LEFT)

		DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="#1e1f10", relief=RIDGE, font=('Arial', 20, 'bold'), text="Match Details\n", fg="white")
		DFrameR.pack(side=RIGHT)

		#Labels & Entry Box

		self.lblmatch_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="match ID:", padx=2, pady=2, bg="#1e1f10", fg="white")
		self.lblmatch_id.grid(row=0, column=0, sticky=W)
		self.txtmatch_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=match_id, width=39, bg="#1e1f10", fg="white")
		self.txtmatch_id.grid(row=0, column=1) 

		self.lblhome=Label(DFrameL, font=('Arial', 18, 'bold'), text="home (y/n):", padx=2, pady=2, bg="#1e1f10", fg="white")
		self.lblhome.grid(row=5, column=0, sticky=W) 
		self.txthome=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=home, width=39, bg="#1e1f10", fg="white")
		self.txthome.grid(row=5, column=1)

		self.lblaway=Label(DFrameL, font=('Arial', 18, 'bold'), text="away (y/n):", padx=2, pady=2, bg="#1e1f10", fg="white")
		self.lblaway.grid(row=6, column=0, sticky=W) 
		self.txtaway=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=away, width=39, bg="#1e1f10", fg="white")
		self.txtaway.grid(row=6, column=1)

		self.lblduration=Label(DFrameL, font=('Arial', 18, 'bold'), text="duration", padx=2, pady=2, bg="#1e1f10", fg="white")
		self.lblduration.grid(row=7, column=0, sticky=W) 
		self.txtduration=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=duration, width=39, bg="#1e1f10", fg="white")
		self.txtduration.grid(row=7, column=1)

		#ListBox & ScrollBar
		sb=Scrollbar(DFrameR)
		sb.grid(row=0, column=1, sticky='ns')

		matchList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="#1e1f10", fg="white", yscrollcommand=sb.set)
		matchList.bind('<<ListboxSelect>>', matchrec)
		matchList.grid(row=0, column=0, padx=8)
		sb.config(command=matchList.yview)

		#Buttons
		self.btnadd=Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="white", command=adddata)
		self.btnadd.grid(row=0, column=0)

		self.btndis=Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="white", command=disdata)
		self.btndis.grid(row=0, column=1)

		self.btnclc=Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="white", command=clcdata)
		self.btnclc.grid(row=0, column=2)

		self.btndel=Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="white", command=deldata)
		self.btndel.grid(row=0, column=4)

		self.btnup=Button(BFrame, text="Update", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="white", command=updata)
		self.btnup.grid(row=0, column=5)

		self.btnx=Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="white", command=iExit)
		self.btnx.grid(row=0, column=6)


if __name__=='__main__':
	root=Tk()
	datbase=match(root)
	root.mainloop()