

######### CUSTOMER_TABLE MANAGEMENT #########

from tkinter import *
import tkinter.messagebox
import backend

class customer:
    def __init__(self, root):
        self.root=root
        self.root.title("Online Match Ticket Booking System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#1e1f10")

    
        customer_id=StringVar()
        name=StringVar()
        gender=StringVar()
        ph_no = StringVar()
        email=StringVar()
        password=StringVar()
        bookdatetime=StringVar()
        

        #Fuctions
        def iExit():
            iExit=tkinter.messagebox.askyesno("Online Ticket Management System", "Do you want to exit?")
            if iExit>0:
                root.destroy()
            return

        def clcdata():
            self.txtcustomer_id.delete(0,END)
            self.txtname.delete(0,END)
            self.txtgender.delete(0,END)
            self.txtph_no.delete(0,END)
            self.txtemail.delete(0,END)
            self.txtpassword.delete(0,END)
            self.txtbookdatetime.delete(0,END)

        def adddata():
            if(len(customer_id.get())!=0):
                backend.addCustomer(customer_id.get(),name.get(),gender.get(),ph_no.get(),email.get(),password.get(),bookdatetime.get())
                customerList.delete(0,END)
                customerList.insert(END,(customer_id.get(),name.get(),gender.get(),ph_no.get(),email.get(),password.get(),bookdatetime.get()))

        def disdata():
            customerList.delete(0,END)
            for row in backend.viewCustomer():
                customerList.insert(END, row, str(""))

        def custmanager(event):
            global sd
            searchcustomer=customerList.curselection()[0]
            sd=customerList.get(searchcustomer)
            self.txtcustomer_id.delete(0,END)
            self.txtcustomer_id.insert(END,sd[1])
            self.txtname.delete(0,END)
            self.txtname.insert(END,sd[2])
            self.txtgender.delete(0,END)
            self.txtgender.insert(END,sd[3])
            self.txtph_no.delete(0,END)
            self.txtph_no.insert(END,sd[4])
            self.txtemail.delete(0,END)
            self.txtemail.insert(END,sd[5])
            self.txtpassword.delete(0,END)
            self.txtpassword.insert(END,sd[6])
            self.txtbookdatetime.delete(0,END)
            self.txtbookdatetime.insert(END,sd[7])


        def deldata():
            if(len(customer_id.get())!=0):
                backend.deleteCustomer(sd[0])
                clcdata()
                disdata()

        def searchdb():
            customerList.delete(0,END)
            for row in backend.searchMatches(customer_id.get(),name.get(),gender.get(),ph_no.get(),email.get(),password.get(),bookdatetime.get()):
                customerList.insert(END, row, str(""))

        def updata():
            if(len(customer_id.get())!=0):
                backend.deleteCustomer(sd[0])
            if(len(customer_id.get())!=0):
                backend.addCustomer(customer_id.get(),name.get(),gender.get(),ph_no.get(),email.get(),password.get(),bookdatetime.get())
                customerList.delete(0,END)
                customerList.insert(END,(customer_id.get(),name.get(),gender.get(),ph_no.get(),email.get(),password.get(),bookdatetime.get()))

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

        DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="#1e1f10", relief=RIDGE, font=('Arial', 20, 'bold'), text="Customer Information\n", fg="white")
        DFrameL.pack(side=LEFT)

        DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="#1e1f10", relief=RIDGE, font=('Arial', 20, 'bold'), text="Customer Details\n", fg="white")
        DFrameR.pack(side=RIGHT)

        #Labels & Entry Box

        self.lblcustomer_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="Customer ID:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblcustomer_id.grid(row=0, column=0, sticky=W)
        self.txtcustomer_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=customer_id, width=39, bg="#1e1f10", fg="white")
        self.txtcustomer_id.grid(row=0, column=1) 

        self.lblname=Label(DFrameL, font=('Arial', 18, 'bold'), text="Name:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblname.grid(row=1, column=0, sticky=W) 
        self.txtname=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=name, width=39, bg="#1e1f10", fg="white")
        self.txtname.grid(row=1, column=1)

        self.lblgender=Label(DFrameL, font=('Arial', 18, 'bold'), text="Gender:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblgender.grid(row=2, column=0, sticky=W) 
        self.txtgender=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=gender, width=39, bg="#1e1f10", fg="white")
        self.txtgender.grid(row=2, column=1)

        self.lblgender=Label(DFrameL, font=('Arial', 18, 'bold'), text="Phone Number:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblgender.grid(row=3, column=0, sticky=W) 
        self.txtgender=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=ph_no, width=39, bg="#1e1f10", fg="white")
        self.txtgender.grid(row=3, column=1)

        self.lblemail=Label(DFrameL, font=('Arial', 18, 'bold'), text="E-mail:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblemail.grid(row=4, column=0, sticky=W) 
        self.txtemail=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=email, width=39, bg="#1e1f10", fg="white")
        self.txtemail.grid(row=4, column=1)

        self.lblpassword=Label(DFrameL, font=('Arial', 18, 'bold'), text="Password:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblpassword.grid(row=5, column=0, sticky=W) 
        self.txtpassword=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=password, width=39, bg="#1e1f10", fg="white")
        self.txtpassword.grid(row=5, column=1)

        self.lblbookdatetime=Label(DFrameL, font=('Arial', 18, 'bold'), text="Booking DateTime:", padx=2, pady=2, bg="#1e1f10", fg="white")
        self.lblbookdatetime.grid(row=6, column=0, sticky=W) 
        self.txtbookdatetime=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=bookdatetime, width=39, bg="#1e1f10", fg="white")
        self.txtbookdatetime.grid(row=6, column=1)


        #ListBox & ScrollBar
        sb=Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        customerList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="#1e1f10", fg="white", yscrollcommand=sb.set)
        customerList.bind('<<ListboxSelect>>', custmanager)
        customerList.grid(row=0, column=0, padx=8)
        sb.config(command=customerList.yview)

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
    datbase=customer(root)
    root.mainloop()