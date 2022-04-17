from tkinter import *
from tkinter import messagebox
import mysql.connector

con=mysql.connector.connect(host='localhost',port='3306',user='root',password='jatinmysql',database='projectfile')
cur=con.cursor()

class Update(Toplevel):
    def __init__(self,user_id):
        Toplevel.__init__(self)
        self.geometry("650x600+600+50")
        self.title("Update User Detail")
        self.resizable(0,0)

        print("person id : ",user_id)

        query=cur.execute("select * from user where user_id='"+user_id+"'")
        result=cur.fetchone()
        self.user_id=user_id

        user_name=result[1]
        user_name1=result[2]
        user_email=result[3]
        user_phoneno=result[4]
        user_addr=result[5]

        print("user_name : " +user_name)

        self.top=Frame(self,height=150,bg="blue")
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=500,bg="pink")
        self.bottom.pack(fill=X)

        self.heading=Label(self.top,text="Fill Detail",font='arial 15 bold',bg="white")
        self.heading.place(x=230,y=50)

        self.label_id=Label(self.bottom,text="Id :",font='árial 15 bold')
        self.label_id.place(x=49,y=40)
        self.user_id=Entry(self.bottom,width=30,bd=4)
        self.user_id.insert(0,user_id)
        self.user_id.place(x=164,y=40)

        self.label_name=Label(self.bottom,text="Name :",font='árial 15 bold')
        self.label_name.place(x=49,y=70)
        self.user_name=Entry(self.bottom,width=30,bd=4)
        self.user_name.insert(0,user_name)
        self.user_name.place(x=164,y=70)

        self.label_name1=Label(self.bottom,text="Last Name :",font='árial 15 bold')
        self.label_name1.place(x=49,y=100)
        self.user_name1=Entry(self.bottom,width=30,bd=4)
        self.user_name1.insert(0,user_name1)
        self.user_name1.place(x=164,y=100)

        self.label_email=Label(self.bottom,text="Email :",font='árial 15 bold')
        self.label_email.place(x=49,y=130)
        self.user_email=Entry(self.bottom,width=30,bd=4)
        self.user_email.insert(0,user_email)
        self.user_email.place(x=164,y=130)

        self.label_phoneno=Label(self.bottom,text="Mobile No. :",font='árial 15 bold')
        self.label_phoneno.place(x=49,y=170)
        self.user_phoneno=Entry(self.bottom,width=30,bd=4)
        self.user_phoneno.insert(0,user_phoneno)
        self.user_phoneno.place(x=164,y=170)

        self.label_addr=Label(self.bottom,text="Address :",font='árial 15 bold')
        self.label_addr.place(x=49,y=210)
        self.user_addr=Text(self.bottom,width=23,height=10)
        self.user_addr.insert(1.0,user_addr)
        self.user_addr.place(x=164,y=210)

        btnaddperson=Button(self.bottom,text="Update",command=self.update_people)
        btnaddperson.place(x=270,y=420)

    def update_people(self):
        person_id = self.user_id.get()
        person_name=self.user_name.get()
        person_name1 = self.user_name1.get()
        person_email=self.user_email.get()
        person_phoneno= self.user_phoneno.get()
        person_addr=self.user_addr.get(1.0,'end-1c')   

        cur.execute("update user set user_name='{}',user_name1='{}',user_email='{}',user_phoneno='{}',user_addr='{}' where user_id={}".format(person_name,person_name1,person_email,person_phoneno,person_addr,person_id))
        con.commit()
        messagebox.showinfo("success status","data update successfully")