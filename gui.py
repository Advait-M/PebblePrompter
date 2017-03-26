from tkinter import *
import pyredb

pyredb.ForgetMeNot().start()
pyredb.ForgetMeNot().alert(False, "")

def clearSS():
    sendSuccess.config(image=off)

def completeTask(name):
    if name == "script":
        scriptSuccess.config(image=on)

    elif name == "send":
        sendSuccess.config(image=on)
        sendSuccess.after(5000,clearSS)


def setScript():
    # print(Script_Field.get(0.0, END))
    if len(Script_Field.get(0.0, END))!=0:
        pyredb.ForgetMeNot().editScript(Script_Field.get(0.0, END).strip())
        Script_Field.config(state="disabled")
        setS.config(state="disabled")
        completeTask('script')


def sendToPresenter():
    strrr = Alert.get()
    if len(strrr) > 0:
        pyredb.ForgetMeNot().alert(True, strrr)
        Alert.delete(0, END)
        completeTask('send')


root = Tk()
off = PhotoImage(file="close-circle.gif")
on = PhotoImage(file="check-circle.gif")
home = Frame(root)
home.grid(row=1, column=1)
Label(home, text="Enter Your Presentation Script").grid(row=1, column=1)
Script_Field = Text(home, height=20, width=40)
Script_Field.grid(row=2, column=1)
contact = Frame(root)
contact.grid(row=1, column=2, sticky=NW)
Label(contact, text="Enter Message").grid(row=1, column=1)
Alert = Entry(contact, width=30)
Alert.grid(row=2, column=1)
Button(contact, text="Send Message to Presenter", command=sendToPresenter, relief="groove").grid(row=3, column=1)

Label(contact, text="Set Script:").grid(row=4, column=1)
scriptSuccess = Label(contact, image=off)
scriptSuccess.grid(row=4, column=2)

Label(contact, text="Sent Message:").grid(row=5, column=1)
sendSuccess = Label(contact, image=off)
sendSuccess.grid(row=5, column=2)

setS = Button(home, text="Set Script", command=setScript, relief="groove")
setS.grid(row=3, column=1)

home.mainloop()
