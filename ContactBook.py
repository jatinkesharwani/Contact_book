from tkinter import *
from mypeople import MyPeople
from addpoeple import AddPoeple

class Application(object):
    def __init__(self,master):
        self.master=master

        self.top=Frame(master,height=70,bg="red")
        self.top.pack(fill=X)
        self.bottom=Frame(master,height=580,bg="yellow")
        self.bottom.pack(fill=X)

        self.heading=Label(self.top,text="Contact Book App",font='arial 15 bold',bg="white")
        self.heading.place(x=230,y=20)

        self.mypeople=Button(self.bottom,text="my people",font='arial 15 bold',bg="white",command=self.my_people)
        self.mypeople.place(x=260,y=100)

        self.addpoeple=Button(self.bottom,text="addpeople",font='arial 15 bold',bg="white",command=self.addpersonid)
        self.addpoeple.place(x=255,y=175)

    def my_people(self):
        people = MyPeople()

    def addpersonid(self):
        add=AddPoeple()

        
def main():

    root = Tk() 
    app=Application(root)
    root.geometry("650x550+350+20")  
    root.resizable(0,0)  
    root.title("Contact Book")

    root.mainloop()

if __name__ == '__main__':
    main()
