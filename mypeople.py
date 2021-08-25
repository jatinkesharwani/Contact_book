from tkinter import *
import mysql.connector
from tkinter import messagebox
from addpoeple import AddPoeple
from updatepeople import Update
from displaypeople import Display

con=mysql.connector.connect(host='localhost',port='3306',user='root',password='K6e1p8je5wpp34@',database='projectfile')
cur=con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x600+600+50")
        self.title("My People")
        self.resizable(0,0)

        self.top=Frame(self,height=150,bg="blue")
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=500,bg="pink")
        self.bottom.pack(fill=X)

        self.heading=Label(self.top,text="My People",font='arial 15 bold',bg="white")
        self.heading.place(x=230,y=50)

        self.listBox=Listbox(self.bottom,width=45,height=27)
        self.listBox.grid(row=0,column=0,padx=(40,0))

        btnadd=Button(self.bottom,text="Add",width=12,font='arial 15 bold',command=self.add_people)
        btnadd.grid(row=0,column=2,padx=20,pady=10,sticky=N)

        btnupdate=Button(self.bottom,text="Update",width=12,font='arial 15 bold',command=self.update_people)
        btnupdate.grid(row=0,column=2,padx=20,pady=70,sticky=N)

        btndisplay=Button(self.bottom,text="Display",width=12,font='arial 15 bold',command=self.display_people)
        btndisplay.grid(row=0,column=2,padx=20,pady=130,sticky=N)

        btndelete=Button(self.bottom,text="Delete",width=12,font='arial 15 bold',command=self.delete_people)
        btndelete.grid(row=0,column=2,padx=20,pady=190,sticky=N)

        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)  
        

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)
        
        cur.execute("select * from projectfile.user")
        persons=cur.fetchall()
        count=0

        for person in persons:
            self.listBox.insert(count,str(person[0]) + ". "+person[1] +" "+person[2])
            count+=1

            self.scroll.grid(row=0,column=1,sticky=N+S)

    def add_people(self):
        add_page = AddPoeple() 

    def update_people(self):
        select_item= self.listBox.curselection()
        person = self.listBox.get(select_item)
        user_id=person.split(".")[0]
        update_page = Update(user_id)

    def display_people(self):
        select_item= self.listBox.curselection()
        person = self.listBox.get(select_item)
        user_id=person.split(".")[0]
        displaypage=Display(user_id)

    def delete_people(self):
        select_item= self.listBox.curselection()
        person = self.listBox.get(select_item)
        user_id=person.split(".")[0]

        query="delete from user where user_id={}".format(user_id)
        string_for_mbox="are you sure you wanna delete",person.split(".")[1], "?"
        answer=messagebox.askquestion("warning","are you sure you wanna delete?")
        if answer=='yes':
            cur.execute(query)
            con.commit()
            messagebox.showinfo("success","person id deleted")
            self.destroy()

       
        
       
        
        

       
        
        

