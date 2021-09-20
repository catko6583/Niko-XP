def Warning():
    mbox.showwarning('Uh Oh', 'you are not supposed to go there!')
def Error():
    mbox.showerror('Uh Oh', 'there was a error while doing this!')
def restartos():
    os.startfile('startup.py')
    sys.exit('Restarted os')
def shutdown():
    with open('nikosoftware', 'w') as f:
        f.write('no')
    sys.exit('Shutdowned os')
def logout():
    os.startfile('login.pyw')
    sys.exit('Logout')
def Nikosoftware():
    f = open('nikosoftware')
    e = f.read()
    f.close
    if e == 'no':
        Warning()
        Nikosoftwarelogin()
    if e == 'yes':
        Error()
def opennoviruses():
    start('antivirus.pyw')
def browser():
    start('browse.pyw')
        
def Nikosoftwarelogin():
    start('nikosoftwarelogin.py')
def openfiles():
    start('file.py')
def editfiles():
    start('edit.py')

from tkinter import *
from tkinter import messagebox as mbox
import sys
import os
from os import startfile as start

logs = Tk()
logs.geometry("500x500")
logs.title('Niko XP')
logs.resizable(0,0)
def Smenu():
    S = Tk()
    S.geometry("30x65")
    S.title('Shutdown Menu')
    restart = Button(S, bg = "yellow", text = "Restart", fg = "orange", command=restartos)
    restart.place(x = 0, y = 0)
    Shutdown = Button(S, bg = "yellow", text = "Shutdown", fg = "orange", command=shutdown)
    Shutdown.place(x = 0, y = 20)
    Logoff = Button(S, bg = "yellow", text = "Log Out", fg = "orange", command=logout)
    Logoff.place(x = 0, y = 40)
    S.mainloop()
Sbutton = Button(logs, bg = "yellow", text = "Shutdown Menu", fg = "orange", command=Smenu)
Sbutton.place(x = 0, y = 475)
NikoSoftwareonly = Button(logs, bg = "yellow", text = "Niko Software", fg = "orange", command=Nikosoftware)
NikoSoftwareonly.place(x = 415, y = 475)
Browse = Button(logs, bg = "yellow", text = "Niko Browser", fg = "orange", command=browser)
Browse.place(x = 50, y = 0)
Open = Button(logs, bg = "blue", text = "This PC", fg = "black", command=openfiles)
Open.place(x = 0, y = 0)
notepad = Button(logs, bg = "yellow", text = "Niko EDIT", fg = "orange", command=editfiles)
notepad.place(x = 125, y = 0)
Opene = Button(logs, bg = "yellow", text = "Niko antivirus", fg = "orange", command=opennoviruses)
Opene.place(x = 0, y = 10)
logs.mainloop()
