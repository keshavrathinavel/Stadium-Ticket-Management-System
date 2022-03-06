

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

    
        ticket_id=StringVar()
        seat_id=StringVar()
        match_no=StringVar()
        match_date_time = StringVar()
        price=StringVar()
        veg=StringVar()
        nonveg=StringVar()
        snacks = StringVar()

        #Fuctions
        def iExit():
            iExit=tkinter.messagebox.askyesno("Online Ticket Management System", "Do you want to exit?")
            if iExit>0:
                root.destroy()
            return

        def clcdata():
            self.txtticket_id.delete(0,END)
            self.txtseat_id.delete(0,END)
            self.txtmatch_no.delete(0,END)
            self.txtmatch_date_time.delete(0,END)
            self.txtprice.delete(0,END)
            self.txtveg.delete(0,END)
            self.txtnonveg.delete(0,END)
            self.txtsnacks.delete(0,END)
        def adddata():
            if(len(ticket_id.get())!=0):
                backend.addticket(ticket_id.get(),seat_id.get(),match_no.get(),match_date_time.get(),price.get(),veg.get(),nonveg.get(),snacks.get())
                ticketList.delete(0,END)
                ticketList.insert(END,(ticket_id.get(),seat_id.get(),match_no.get(),match_date_time.get(),price.get(),veg.get(),nonveg.get(),snacks.get()))

        def disdata():
            ticketList.delete(0,END)
            for row in backend.viewticket():
                ticketList.insert(END, row, str(""))

        def tickmanager(event):
            global sd
            searchticket=ticketList.curselection()[0]
            sd=ticketList.get(searchticket)
            self.txtticket_id.delete(0,END)
            self.txtticket_id.insert(END,sd[1])
            self.txtseat_id.delete(0,END)
            self.txtseat_id.insert(END,sd[2])
            self.txtmatch_no.delete(0,END)
            self.txtmatch_no.insert(END,sd[3])
            self.txtmatch_date_time.delete(0,END)
            self.txtmatch_date_time.insert(END,sd[4])
            self.txtprice.delete(0,END)
            self.txtprice.insert(END,sd[5])
            self.txtveg.delete(0,END)
            self.txtveg.insert(END,sd[6])
            self.txtnonveg.delete(0,END)
            self.txtnonveg.insert(END,sd[7])
            self.txtsnacks.delete(0,END)
            self.txtsnacks.insert(END,sd[8])


        def deldata():
            if(len(ticket_id.get())!=0):
                backend.deleteticket(sd[0])
                clcdata()
                disdata()

        def searchdb():
            ticketList.delete(0,END)
            for row in backend.searchMatches(ticket_id.get(),seat_id.get(),match_no.get(),match_date_time.get(),price.get(),veg.get(),nonveg.get(),snacks.get()):
                ticketList.insert(END, row, str(""))

        def updata():
            if(len(ticket_id.get())!=0):
                backend.deleteticket(sd[0])
            if(len(ticket_id.get())!=0):
                backend.addticket(ticket_id.get(),seat_id.get(),match_no.get(),match_date_time.get(),price.get(),veg.get(),nonveg.get(),snacks.get())
                ticketList.delete(0,END)
                ticketList.insert(END,(ticket_id.get(),seat_id.get(),match_no.get(),match_date_time.get(),price.get(),veg.get(),nonveg.get(),snacks.get()))

        #Frames
        MainFrame=Frame(self.root, bg="#1e1f10")
        MainFrame.grid()

        TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="#1e1f10", relief=RIDGE)
        TFrame.pack(side=TOP)

        self.TFrame=Label(TFrame, font=('Arial', 51, 'bold'), text="ONLINE ticket TICKET BOOKING SYSTEM", bg="#1e1f10", fg="white")
        self.TFrame.grid() 

        BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="#1e1f10", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="#1e1f10", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="#1e1f10", relief=RIDGE, font=('Arial', 20, 'bold'), text="Ticket Information\n", fg="white")
        DFrameL.pack(side=LEFT)

        DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="#1e1f10", relief=RIDGE, font=('Arial', 20, 'bold'), text="Ticket Details\n", fg="white")
        DFrameR.pack(side=RIGHT)

        #Labels & Entry Box

        self.lblticket_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="ticket ID:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblticket_id.grid(row=0, column=0, sticky=W)
        self.txtticket_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=ticket_id, width=39, bg="#1e1f10", fg="white")
        self.txtticket_id.grid(row=0, column=1) 

        self.lblseat_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="Seat ID:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblseat_id.grid(row=1, column=0, sticky=W) 
        self.txtseat_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=seat_id, width=39, bg="#1e1f10", fg="white")
        self.txtseat_id.grid(row=1, column=1)

        self.lblmatch_no=Label(DFrameL, font=('Arial', 18, 'bold'), text="Match No:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblmatch_no.grid(row=2, column=0, sticky=W) 
        self.txtmatch_no=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=match_no, width=39, bg="#1e1f10", fg="white")
        self.txtmatch_no.grid(row=2, column=1)

        self.lblmatch_no=Label(DFrameL, font=('Arial', 18, 'bold'), text="Match DateTime:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblmatch_no.grid(row=3, column=0, sticky=W) 
        self.txtmatch_no=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=match_date_time, width=39, bg="#1e1f10", fg="white")
        self.txtmatch_no.grid(row=3, column=1)

        self.lblprice=Label(DFrameL, font=('Arial', 18, 'bold'), text="Price:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblprice.grid(row=4, column=0, sticky=W) 
        self.txtprice=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=price, width=39, bg="#1e1f10", fg="white")
        self.txtprice.grid(row=4, column=1)

        self.lblveg=Label(DFrameL, font=('Arial', 18, 'bold'), text="Veg Ordered:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblveg.grid(row=5, column=0, sticky=W) 
        self.txtveg=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=veg, width=39, bg="#1e1f10", fg="white")
        self.txtveg.grid(row=5, column=1)

        self.lblnonveg=Label(DFrameL, font=('Arial', 18, 'bold'), text="Nonveg Ordered:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblnonveg.grid(row=6, column=0, sticky=W) 
        self.txtnonveg=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=nonveg, width=39, bg="#1e1f10", fg="white")
        self.txtnonveg.grid(row=6, column=1)

        self.lblnonveg=Label(DFrameL, font=('Arial', 18, 'bold'), text="Snacks Ordered:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblnonveg.grid(row=7, column=0, sticky=W) 
        self.txtnonveg=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=nonveg, width=39, bg="#1e1f10", fg="white")
        self.txtnonveg.grid(row=7, column=1)


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