

######### TICKET_TABLE MANAGEMENT #########

from tkinter import *
import tkinter.messagebox
import backend

class ticket:
    def __init__(self, root):
        self.root=root
        self.root.title("Online Match Ticket Booking System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#1e1f10")

    
        match_no=StringVar()
        offer_id=StringVar()
        
        #Fuctions
        def iExit():
            iExit=tkinter.messagebox.askyesno("Online Ticket Management System", "Do you want to exit?")
            if iExit>0:
                root.destroy()
            return

        def clcdata():
            self.txtmatch_no.delete(0,END)
            self.txtoffer_id.delete(0,END)
       
        def adddata():
            if(len(match_no.get())!=0):
                backend.addiscount(match_no.get(),offer_id.get(),match_no.get())
                ticketList.delete(0,END)
                ticketList.insert(END,(match_no.get(),offer_id.get(),match_no.get()))

        def disdata():
            ticketList.delete(0,END)
            for row in backend.viewiscount():
                ticketList.insert(END, row, str(""))

        def tickmanager(event):
            global sd
            searchticket=ticketList.curselection()[0]
            sd=ticketList.get(searchticket)
            self.txtmatch_no.delete(0,END)
            self.txtmatch_no.insert(END,sd[1])
            self.txtoffer_id.delete(0,END)
            self.txtoffer_id.insert(END,sd[2])
            


        def deldata():
            if(len(match_no.get())!=0):
                backend.deletediscount(sd[0])
                clcdata()
                disdata()


        def updata():
            if(len(match_no.get())!=0):
                backend.deleteticket(sd[0])
            if(len(match_no.get())!=0):
                backend.addiscount(match_no.get(),offer_id.get(),match_no.get())
                ticketList.delete(0,END)
                ticketList.insert(END,(match_no.get(),offer_id.get(),match_no.get()))

        #Frames
        MainFrame=Frame(self.root, bg="#1e1f10")
        MainFrame.grid()

        TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="#1e1f10", relief=RIDGE)
        TFrame.pack(side=TOP)

        self.TFrame=Label(TFrame, font=('Arial', 51, 'bold'), text="ONLINE TICKET MANAGEMENT SYSTEM", bg="#1e1f10", fg="white")
        self.TFrame.grid() 

        BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="#1e1f10", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="#1e1f10", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="#1e1f10", relief=RIDGE, font=('Arial', 20, 'bold'), text="Discount Information\n", fg="white")
        DFrameL.pack(side=LEFT)

        DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="#1e1f10", relief=RIDGE, font=('Arial', 20, 'bold'), text="Discount Details\n", fg="white")
        DFrameR.pack(side=RIGHT)

        #Labels & Entry Box

        self.lblmatch_no=Label(DFrameL, font=('Arial', 18, 'bold'), text="Match No:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblmatch_no.grid(row=0, column=0, sticky=W)
        self.txtmatch_no=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=match_no, width=39, bg="#1e1f10", fg="white")
        self.txtmatch_no.grid(row=0, column=1) 

        self.lbloffer_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="Offer ID:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lbloffer_id.grid(row=1, column=0, sticky=W) 
        self.txtoffer_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=offer_id, width=39, bg="#1e1f10", fg="white")
        self.txtoffer_id.grid(row=1, column=1)


        #ListBox & ScrollBar
        sb=Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        ticketList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="#1e1f10", fg="white", yscrollcommand=sb.set)
        ticketList.bind('<<ListboxSelect>>', tickmanager)
        ticketList.grid(row=0, column=0, padx=8)
        sb.config(command=ticketList.yview)

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
    datbase=ticket(root)
    root.mainloop()