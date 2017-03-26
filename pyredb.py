#!/usr/bin/env python3

from pyrebase import *

class ForgetMeNot:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyASyA1nD_CMsjwefumq-8vUJzZxH6BOFNc",
            "authDomain": "wearhacks17-56091.firebaseapp.com",
            "databaseURL": "https://wearhacks17-56091.firebaseio.com",
            "storageBucket": "wearhacks17-56091.appspot.com"
            }
        self.firebase = initialize_app(self.config)

        self.db = self.firebase.database()


    def start(self):
        self.stream = self.db.stream(self.streamHandler)
        print(self.stream)
        # self.addSession("Jeffy", "Guffy", "2:00", "4:00", "Waterloo", "Medicare")
        # self.addSession("Ert", "Geh", "4:00", "9:00", "Yeth", "Medicare")
        # self.addSession("Bob", "Hiw", "1:00", "7:00", "Toronto", "Health Plus")
        #self.editSession("Nim", "Feteov", "15:00", "18:00", "Toronto", "med")
        #self.getAll()
        # times = {"Start Time" : "01:00", "End Time" : "03:00"}
        # self.db.child("Bob Fred").set(times)
        ##endTime = {"End Time": "8:00"}
        ##self.db.child("Bob Fred").set(endTime)
        
    def addSession(self, firstName, lastName, startTime, endTime, location, clinicName):
        self.db.child(firstName + " " + lastName).set({"Start Time" : startTime, "End Time" : endTime, "Location" : location, "Clinic Name" : clinicName})

    def addIndex(self, curIndex):
        self.db.child("stuff").set({"curIndex":curIndex})
        
    def editIndex(self, curIndex):
        self.db.child("stuff").update({"curIndex":curIndex})

    def addScript(self, script):
        self.db.child("scriptText").set({"text":script})
    def editScript(self, script):
        self.db.child("scriptText").update({"text":script})

    def alert(self, state, mssg):
        if state:
            self.db.child("alerts").child("alert").set({"state": "true", "mssg": mssg})
        else:
            self.db.child("alerts").child("alert").set({"state": "false", "mssg": mssg})
    def editSession(self, startTime, endTime, name, location, clinicName):
        if typeOfString == "Start Time" or typeOfString == "End Time":
            self.db.child(oldFirstName + " " + oldLastName).update({typeOfString : newString})

    def getText(self):
        # print((self.db.child("wait-no-more").get()).each())
        # print(type(self.db))
        # print((self.db.child("/").get()).each())
        # for i in range(0, len(self.db)):
        all_users = self.db.child("/").get()
        masterList = []
        for user in all_users.each():
            text = (user.val())["curIndex"]
        print(text)
        return text

    def streamHandler(self, post):
        event = post["event"]
        key = post["path"]
        value = post["data"]

        if event == "put":
            print(key, ":", value)

if __name__ == "__main__":
    a = ForgetMeNot()
    a.start()
    #ForgetMeNot().getText()
    a.editIndex(4)
    
    a.addScript("asdasd")
    a.alert(False, "heee;sad")
