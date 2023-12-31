from tkinter import *
from PIL import Image,ImageTk
from customer import Customers
from room import Roombooking
from details import Details
from time import strftime
from datetime import datetime




class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")
        #=======================================HEADER IMAGE===================================
        
        img1=Image.open(r"2.jpeg")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        #========================================LOGO IMAGE==================================
        img2=Image.open(r"logo.png")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        
        #========================================TITLE=====================================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        
        #=======================================TIME=======================================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(lbl_title,font=("times new roman",14,"bold"),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=40)
        time()
        
        
        #============================2==============MAIN FRAME======================================
        
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        #======================================MENU=================================================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        
        
        #==========================================BUTTON FRAME======================================
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=220,height=190)
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="ROOM",command=self.Room_booking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0)
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",command=self.Details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0)
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="DEVELOPER",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0)
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0)
        logout_btn.grid(row=4,column=0,pady=1)
        
        #===============================================RIGHT SIDE IMAGE=================================================
        img3=Image.open(r"1.jpeg")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)

        #===============================================down IMAGE=================================================
        img4=Image.open(r"9.jpeg")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)
        
        img5=Image.open(r"7.jpeg")
        img5=img5.resize((230,210),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=210)

    #=====================================BUTTON FUNCTION================================
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customers(self.new_window)
    
    def Room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
        
    def Details(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)
        
    def logout(self):
        self.root.destroy()
        
if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()