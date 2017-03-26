from tkinter import *


def setScript():
    print(Script_Field.get(0.0, END))


def sendToFirebase():


def sendToPresenter():
    top = Frame(root)
    top.grid()
    Label(top, text="Enter Message").grid()
    Button(top,text="Send",command=).grid()
    print("PYREBASE")

root = Tk()
home = Frame(root)
home.grid()
Label(home, text="Enter Your Presentation Script").grid()
Script_Field = Text(home)
Script_Field.grid()



Button(home, text="Set Script", command=setScript).grid()
Button(home, text="Send Message to Presenter", command=sendToPresenter).grid()

home.mainloop()
