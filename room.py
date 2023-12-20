from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from time import strftime
from datetime import datetime
import random
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+240+225")
        
        
        #======================VARIABLE============================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        #========================================TITLE====================================
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=80)
        #=======================================LOGO IMAGE===================================
        
        img1=Image.open(r"logo.png")
        img1=img1.resize((100,70),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=70)
        
        #=========================================LABEL FRAME===============================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=80,width=425,height=490)

        #=======================================LABEL AND ENTRY=========================================
        
        #===========================CUSTOMER CONTACT NUMBER==========================================
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        
        entry_contact=Entry(labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        entry_contact.grid(row=0,column=1,sticky=W)
        
        #============================FETCH DATA BUTTON======================================
        btnfFetchData=Button(labelframeleft,text="Fetch Data:",command=self.Fetch_contact,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnfFetchData.place(x=340,y=4)
        #=======================CHECK IN DATE
        check_in_date=Label(labelframeleft,text="Check in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)
        
        #=====================================CHECK OUT DATE===================================
        
        lbl_check_out=Label(labelframeleft,text="Check out date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)

        txtcheck_out=Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txtcheck_out.grid(row=2,column=1)
        
        #==========================ROOM TYPE==========================================
        label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
        #======================AVAILABLE ROOM=============================================
        lblRoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        #txtRoomAvailable=Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        #txtRoomAvailable.grid(row=4,column=1)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
        
        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)
        #======================================MEAL==========================
        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        txtMeal=Entry(labelframeleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)
        
        #======================================NO OF DAYS==========================
        lblNoOfDays=Label(labelframeleft,text="No Of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays=Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)
        
        #======================================PAID TAX==========================
        lblPaidTax=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=W)

        txtPaidTax=Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtPaidTax.grid(row=7,column=1)
        
        #======================================SUB TOTAL==========================
        lblSubTotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)

        txtSubTotal=Entry(labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtSubTotal.grid(row=8,column=1)
        
        #======================================TOTAL COST==========================
        lblTotalCost=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)

        txtTotalCost=Entry(labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtTotalCost.grid(row=9,column=1)
        
        #================================BILL BUTTON=============================================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
        
        #=============================BUTTON FRAME================================================
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=2)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=2)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=2)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=2)
        #=======================RIGHT SIDE IMAGE===================================
        img3=Image.open(r"9.jpeg")
        img3=img3.resize((370,250),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=820,y=95,width=370,height=250)
        #=================SEARCH SYSTEM=========================================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=250,width=860,height=320)
        
        lblSearch=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W)
        
        self.Search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.Search_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        
        self.txt_Search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,font=("arial",12,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=2)
        
        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=2)
        
        #===========================================SHOW DATA TABLE=============================================================
        room_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
        room_Table.place(x=0,y=60,width=840,height=220)
        
        scroll_x=ttk.Scrollbar(room_Table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(room_Table,orient=VERTICAL)
        
        self.room_Table=ttk.Treeview(room_Table,column=("Contact","CheckInDate","CheckOutDate","roomtype","RoomAvailable","Meal","NoOfDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)
        
        self.room_Table.heading("Contact",text="Contact")
        self.room_Table.heading("CheckInDate",text="Check-In")
        self.room_Table.heading("CheckOutDate",text="Check-Out")
        self.room_Table.heading("roomtype",text="Room Type")
        self.room_Table.heading("RoomAvailable",text="Room No")
        self.room_Table.heading("Meal",text="Meals")
        self.room_Table.heading("NoOfDays",text="Total Days")
        
       
        
        self.room_Table["show"]="headings"
        self.room_Table.pack(fill=BOTH,expand=1)
        
        self.room_Table.column("Contact",width=100)
        self.room_Table.column("CheckInDate",width=100)
        self.room_Table.column("CheckOutDate",width=100)
        self.room_Table.column("roomtype",width=100)
        self.room_Table.column("RoomAvailable",width=100)
        self.room_Table.column("Meal",width=100)
        self.room_Table.column("NoOfDays",width=100)
        self.room_Table.pack(fill=BOTH,expand=1)
        
        #self.room_Table.bind("<ButtonRelease-1>",self.get_cursor()) 
        self.fetch_data()
       

        #==============================ADD DATA FUNCTION================================================
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),   
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noofdays.get()
                                                                                              
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong {str(es)}",parent=self.root)
                
       # =====================================FETCH DATA FUNCTION==========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #===============================================GET CURSOR DATA FUNCTION=======================
    '''def get_cursor(self,event=""):
        cursor_row=self.room_Table.focus()
        content=self.room_Table.item(cursor_row)
        rows=content["values"]
        
        self.var_contact.set(rows[0])
        self.var_checkin.set(rows[1])
        self.var_checkout.set(rows[2])
        self.var_roomtype.set(rows[3])
        self.var_roomavailable.set(rows[4])
        self.var_meal.set(rows[5])'''
        
        
        
        
        #==================================UPDATE FUNCTIONOT WORKED THE ERROR IS GETCURSOR AREA FIRST CHECK THIS ONE============================================
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in=%s,check_out=%s,roomtype=%s,Room=%s,meal=%s,noOfdays=%s, where Contact=%s",(
                
                                                                                                                                                self.var_checkin.get(),
                                                                                                                                                self.var_checkout.get(),   
                                                                                                                                                self.var_roomtype.get(),
                                                                                                                                                self.var_roomavailable.get(),
                                                                                                                                                self.var_meal.get(),
                                                                                                                                                self.var_noofdays.get(),
                                                                                                                                                self.var_contact.get()
                                                                                                                                            ))
                                                                                                                                                                                            
                                                                                                                                                                          
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Deatils has been updated successfully",parent=self.root)
            
    #==================================DELETE FUNCTIONOT WORKED THE ERROR IS GETCURSOR AREA FIRST CHECK THIS ONE============================================
    def delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you Want Delete Customer data",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
            my_cursor=conn.cursor()
            query="delete from room where Contact =%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
         #==================================RESET FUNCTIONOT WORKED THE ERROR IS GETCURSOR AREA FIRST CHECK THIS ONE============================================
   
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
      #===================FUNCTION FETCH ALL DATA==============================================  
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Plz Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
            #=====================================SHOW DATA FRAME=============================
            showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showDataframe.place(x=450,y=85,width=300,height=150)
            
            lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=0)
            
            
            #========================GENDER QUERY FOR CUSTOMER FILE DATA FETCH================================
            conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
            my_cursor=conn.cursor()
            query=("select Gender from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblName=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
            lblName.place(x=0,y=30)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=30)
             #========================EMAIL QUERY FOR CUSTOMER FILE DATA FETCH================================
            conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
            my_cursor=conn.cursor()
            query=("select Email from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblName=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
            lblName.place(x=0,y=60)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=60)
            
             #========================NATIONALITY QUERY FOR CUSTOMER FILE DATA FETCH================================
            conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
            my_cursor=conn.cursor()
            query=("select Nationality from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblName=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
            lblName.place(x=0,y=90)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=90)
            
             #========================ADDRESS QUERY FOR CUSTOMER FILE DATA FETCH================================
            conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
            my_cursor=conn.cursor()
            query=("select Address from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblName=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
            lblName.place(x=0,y=120)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=120)
        #=================================SEARCH SYSTEM====================================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.Search_var.get())+" LIKE '%"+str(self.txt_Search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
     #===================================TOTAL FUNCTION=======================================       
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
         #=========================================LUXURY PRICE AND THINGS
        
        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.1)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)    
           
        elif (self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.3)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.3))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)      
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.5)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.5))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
            
         #=========================================SINGLE PRICE AND THINGS
            
        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.1)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.3)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.3))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  
            
        
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.5)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.5))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
         #=========================================Double PRICE AND THINGS
            
        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.1)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.3)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.3))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.5)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.5))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
            
        #======================================DUPLEX PRICE AND THINGS===========================    
        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.1)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)     
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Duplex"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.3)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.3))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)       
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Duplex"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.5)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.5))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)     
        #=============================LARGE PRICE AND THINGS==============================
        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Large"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.7)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.7))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Large"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.3)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.3))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Large"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4) 
            Tax="Rs."+str("%.2f"%((q5)*0.5)) 
            ST= "Rs."+str("%.2f"%((q5))) 
            TT="Rs."+str("%.2f"%(q5+((q5)*0.5))) 
            
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)        
            
           
            
                
            
        
        

if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
    
    
    #======================================GET CURSOR HERE PROBLEM ONCE CHECK ERROR VIDEOM MINUTE 15=================
    #======================================SEARCH BUTTON NOT WORKED================================================
    #=====================================LAST MINUET I AM CHANGES DATABASE ASS WELL AS DATA TABLE NAME
