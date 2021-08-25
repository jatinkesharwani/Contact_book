from tkinter import *
from tkinter import messagebox
import mysql.connector

class AddPoeple(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x600+600+50")
        self.title("Fill Detail")
        self.resizable(0,0)

        self.top=Frame(self,height=150,bg="blue")
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=500,bg="pink")
        self.bottom.pack(fill=X)

        self.heading=Label(self.top,text="Fill Detail",font='arial 15 bold',bg="white")
        self.heading.place(x=230,y=50)

        self.label_id=Label(self.bottom,text="Id :",font='árial 15 bold')
        self.label_id.place(x=49,y=40)

        self.user_id=Entry(self.bottom,width=30,bd=4)
        #self.user_id.insert(0,"enter id")
        self.user_id.place(x=164,y=40)

        self.label_name=Label(self.bottom,text="Name :",font='árial 15 bold')
        self.label_name.place(x=49,y=70)

        self.user_name=Entry(self.bottom,width=30,bd=4)
        #self.user_name.insert(0,"enter first name")
        self.user_name.place(x=164,y=70)

        self.label_name1=Label(self.bottom,text="Last Name :",font='árial 15 bold')
        self.label_name1.place(x=49,y=100)

        self.user_name1=Entry(self.bottom,width=30,bd=4)
        #self.user_name1.insert(0,"enter last name")
        self.user_name1.place(x=164,y=100)

        self.label_email=Label(self.bottom,text="Email :",font='árial 15 bold')
        self.label_email.place(x=49,y=130)

        self.user_email=Entry(self.bottom,width=30,bd=4)
        #self.user_email.insert(0,"enter email")
        self.user_email.place(x=164,y=130)

        self.label_phoneno=Label(self.bottom,text="Mobile No. :",font='árial 15 bold')
        self.label_phoneno.place(x=49,y=170)

        self.user_phoneno=Entry(self.bottom,width=30,bd=4)
        #self.user_phoneno.insert(0,"enter no.")
        self.user_phoneno.place(x=164,y=170)

        self.label_addr=Label(self.bottom,text="Address :",font='árial 15 bold')
        self.label_addr.place(x=49,y=210)

        self.user_addr=Text(self.bottom,width=23,height=10)
        self.user_addr.place(x=164,y=210)

        btnaddperson=Button(self.bottom,text="Add Person",command=self.add_person)
        btnaddperson.place(x=270,y=420)

    def add_person(self):
            person_id = self.user_id.get()
            person_name=self.user_name.get()
            person_name1 = self.user_name1.get()
            person_email=self.user_email.get()
            person_phoneno= self.user_phoneno.get()
            person_addr=self.user_addr.get(1.0,'end-1c')

            if person_id=="" or person_name=="" or person_name1=="" or person_email=="" or person_phoneno=="" or person_addr=="":
                messagebox.showinfo("insert status","please fill all detail")
            else:
                con=mysql.connector.connect( host="localhost", port='3306', user="root", db="projectfile",password="K6e1p8je5wpp34@")
                
                query='create table if not exists user(user_id int primary key,user_name varchar(200),user_name1 varchar(200),user_email varchar(300),user_phoneno varchar(12),user_addr varchar(300))'   
                cur=con.cursor()
                cur.execute(query)
                
                query="insert into user(user_id,user_name,user_name1,user_email,user_phoneno,user_addr) values({},'{}','{}','{}','{}','{}')".format(person_id,person_name,person_name1,person_email,person_phoneno,person_addr)
                cur=con.cursor()
                cur.execute(query)
                con.commit()
                





