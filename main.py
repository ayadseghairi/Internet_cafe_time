import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
import webbrowser
import psutil
import sys
win = tkinter.Tk()
win.title("Your Time (Ayad Seghairi & PAPALE)")
win.geometry("500x500")
win.configure(background="black")
#########################################
def get_pid(name):
	process_name = name
	pid = None
	for proc in psutil.process_iter():
    		if process_name in proc.name():
       			pid = proc.pid
	return pid
state = False
pid_bro_cl = get_pid("client.exe")
pid_bro_gu = get_pid("guardit.exe")
if pid_bro_cl== None and pid_bro_gu == None :
	showinfo("Your Time","bro You are not in an internet cafe .")
	sys.exit()
p1 = psutil.Process(pid_bro_cl)
p2 = psutil.Process(pid_bro_gu)
##################################
def start():
	global state
	global p1
	global p2
	if state == True :
		state = False
		showinfo("Time","time is running")
		labelText.set("time is running")
		p1.resume()
		p2.resume()
	elif state == False :
		showinfo("Time","time is running")
	else :
		win.destroy()
def stop():
	global state
	global p1
	global p2
	if state == True :
		showinfo("Time","time has stopped")
	elif state == False :
		state = True
		showinfo("Time","time has stopped")
		labelText.set("time has stopped")
		p1.suspend()
		p2.suspend()
	else :
		win.destroy()
labelText = tkinter.StringVar()
labelText.set("time is running")
tkinter.Label(win,bg="black",fg="red",font=("Ink Free", 50),text="Ayad Seghairi").place(x=25,y=0)
lipttxt = tkinter.Label(win,bg="black",fg="red",font=("Ink Free", 30),textvariable=labelText).place(x=100,y=180)
Startbt= tkinter.Button(win,text="Start Time",font=("Ink Free", 30),bg="red",fg="Green", activebackground="Green", activeforeground="red",command=lambda:start()).place(x=20,y=240)
stopbt= tkinter.Button(win,text="Stop Time",font=("Ink Free", 30),bg="Green",fg="red",activebackground="red", activeforeground="Green",command=lambda:stop()).place(x=260,y=240)
################################################  Follow us   ################################
tkinter.Button(win,text="Facebook",width=16,bg="blue",fg="black",activebackground="black", activeforeground="blue",command=lambda:webbrowser.open("http://facebook.com/ayadseghairi.off")).place(x=0,y=400)
tkinter.Button(win,text="Github",width=16,bg="black",fg="white",activebackground="white", activeforeground="black",command=lambda:webbrowser.open("http://github.com/ayadseghairi")).place(x=167,y=400)
tkinter.Button(win,text="Instagram",width=16,bg="yellow",fg="black",activebackground="black", activeforeground="yellow",command=lambda:webbrowser.open("http://instagram.com/ayadseghairi.off")).place(x=334,y=400)
win.resizable(False,False)
win.mainloop()
