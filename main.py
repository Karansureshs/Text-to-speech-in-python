import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("text to speech")
root.geometry("900x450+200+100")
root.resizable(False,False)
root.configure(bg="yellow")
engine= pyttsx3.init()

def speaknow():
    text=text1.get(1.0,END)
    gender= gen_com.get()
    speed1=speed.get()
    voices= engine.getProperty('voices')

    def setvoice():
        if (gender=='male'):
            engine.setProperty('voice',voices[0].id)
           
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
           
            engine.say(text)
            engine.runAndWait()
    if(text):
        if (speed1 == "fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed1== "normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
            

def download():
    text=text1.get(1.0,END)
    gender= gen_com.get()
    speed1=speed.get()
    voices= engine.getProperty('voices')

    def setvoice():
        if (gender=='male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()
    if(text):
        if (speed1 == "fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed1== "normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
    


#icon
image_icon=PhotoImage(file="s.png")
root.iconphoto(FALSE,image_icon)

#top
tframe=Frame(root,bg="blue",width=900,height=100)
tframe.place(x=0,y=0)

logo=PhotoImage(file="mm.png")
Label(tframe,image=logo,bg="blue").place(x=10,y=5)

Label(tframe,text="TEXT TO VOICE",font="sansbold 20 bold",bg="blue",fg="red").place(x=150,y=30)

################
text1=Text(root,font="roboto,20", bg="blue",relief=GROOVE,wrap=WORD,fg="yellow")
text1.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold",bg="YELLOW",fg="blue").place(x=570,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="YELLOW",fg="blue").place(x=750,y=160)

gen_com=Combobox(root,values=['male','female'],font="arial,14",state='r',width=10)
gen_com.place(x=550,y=200)
gen_com.set('gender')

speed=Combobox(root,values=['fast','normal','slow'],font="arial,14",state='r',width=10)
speed.place(x=730,y=200)
speed.set('speed')


btn=Button(root,text="speak",compound=LEFT,width=10,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)


save=Button(root,text="save",compound=LEFT,width=10,bg="orange",font="arial 14 bold",command=download)
save.place(x=730,y=280)




root.mainloop()
