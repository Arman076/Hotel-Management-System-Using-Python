from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox





class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+240+225")
        #================================VARIABLES==============================
        self.var_floor=StringVar()
        self.var_roomNo=StringVar()
        self.var_RoomType=StringVar()
        
        
    #-------------------------------TITLES====================================
        lbl_title=Label(self.root,text="ROOM ADDING DEPARTMENT",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
    #=======================================LOGO IMAGE===================================
        
        img1=Image.open(r"logo.png")
        img1=img1.resize((100,70),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        
    #=========================================LABEL FRAME===============================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Rooms Add",padx=2,font=("times new roman",15,"bold"),fg="green",bg="white")
        labelframeleft.place(x=5,y=60,width=540,height=350)
        
        #===========================FLOOR  NUMBER==========================================
        lbl_floor=Label(labelframeleft,text="Floor:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",13,"bold"),width=20)
        entry_floor.grid(row=0,column=1,sticky=W)
        
        #===========================Room No  NUMBER==========================================
        lbl_RoomNo=Label(labelframeleft,text="Room No:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        
        
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,font=("arial",13,"bold"),width=20)
        entry_RoomNo.grid(row=1,column=1,sticky=W)
        
        #===========================ROOM TYPE==========================================
        lbl_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        
        
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,font=("arial",13,"bold"),width=20)
        entry_floor.grid(row=2,column=1,sticky=W)
        
        
         #=============================BUTTON FRAME================================================
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=2)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=2)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=2)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=2)
        
        #=======================================SEARCH SYETEM===========================
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=550,y=60,width=600,height=350)
        
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")
        
        
       
        
        self.room_table["show"]="headings"
        self.room_table.pack(fill=BOTH,expand=1)
        
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
     #==============================ADD DATA FUNCTION================================================
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                self.var_floor.get(),
                                                                                self.var_roomNo.get(),
                                                                                self.var_RoomType.get(),   
                                                                                
                                                                                              
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong {str(es)}",parent=self.root)
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]     
       
        self.var_floor.set(row[2])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])
        
        
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                self.var_floor.get(),
                                                                                                self.var_RoomType.get(), 
                                                                                                self.var_roomNo.get()
                
                
            ))
            
            
            
            
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Data Has Been Updated",parent=self.root)
            
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you Want Delete Customer data",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database="hotel")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set(""),
        
    
        
        
        






if __name__=="__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop()