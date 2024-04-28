from tkinter import *
import time

window=Tk()
window.title("Digital Clock")
window.geometry("600x400")

def myTime():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    am_pm=time.strftime("%p")
    day=time.strftime("%A")
    zone=time.strftime("%Z")

    myText=hour + ":" + minute+ ":" + second + "" + am_pm
    myText2=day + "," + zone
    mylabe1.config(text=myText)
    mylabe12.config(text=myText2)
    mylabe1.after(1000,myTime)

mylabe1=Label(window,text="Hello world",
              font=("Arial",72),fg="white",bg="green")
mylabe1.pack()
mylabe12=Label(window,text="",font=("Arial",24))
mylabe12.pack()

myTime()

window,mainloop()

