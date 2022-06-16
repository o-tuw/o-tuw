from tkinter import *
Omar=Tk()
Omar.title("Omar Calculator")
Omar.geometry("600x500")
Omar.config(bg="#ebecf0")

class Marks:
    def __init__(self,m):
        self.Stu=Label(m, text="Student Marks",font = ('arial',17), bg="#ebecf0")
        self.Stu.place(x=230,y=20)

        self.m1=Label(m, text="Mark 1",font = ('arial',17), bg="#ebecf0")
        self.m1.place(x=120,y=120)

        self.m2 = Label(m, text="Mark 2",font = ('arial',17), bg="#ebecf0")
        self.m2.place(x=120, y=170)

        self.m3 = Label(m, text="Mark 3", font = ('arial',17), bg="#ebecf0")
        self.m3.place(x=120, y=220)

        self.q1 = Entry(bd=10, text="Mark 1", font = ('arial',14))
        self.q1.place(x=200, y=120)

        self.q2 = Entry(bd=10, text="Mark 2", font = ('arial',14))
        self.q2.place(x=200, y=170)

        self.q3 = Entry(bd=10, text="Mark 3",font = ('arial',14))
        self.q3.place(x=200, y=220)

        self.q4 = Entry(bd=10, text="Total",font = ('arial',14))
        self.q4.place(x=200, y=300)

        self.q5 = Entry(bd=10, text="Average",font = ('arial',14))
        self.q5.place(x=200, y=400)

        self.button1=Button(m,width=6,text="Add",font = ('arial',13),command=self.total)
        self.button1.place(x=120, y= 305)

        self.button2 = Button(m, width=6, text="Average",font = ('arial',13), command=self.average)
        self.button2.place(x=120, y= 405)

        self.button3 = Button(m, width=6, text="Clear",font = ('arial',13), command=self.clear)
        self.button3.place(x=450, y=300)

        self.button4 = Button(m, width=6, text="Exit",font = ('arial',13), command=Omar.quit)
        self.button4.place(x=450, y=400)

    def total(self):
        self.q4.delete(0,"end")
        n1=int(self.q1.get())
        n2=int(self.q2.get())
        n3=int(self.q3.get())
        result=(n1+n2+n3)
        self.q4.insert(END, str(result))

    def average(self):
        self.q5.delete(0,"end")
        n1=int(self.q1.get())
        n2=int(self.q2.get())
        n3=int(self.q3.get())
        result=(n1+n2+n3)/3
        self.q5.insert(END, str(result))

    def clear(self):
        self.q5.delete(0, "end")
        self.q4.delete(0, "end")
        self.q3.delete(0, "end")
        self.q2.delete(0, "end")
        self.q1.delete(0, "end")

my=Marks(Omar)
Omar.mainloop()
