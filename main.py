import psutil
from threading import Thread
import time
print("Ayad Seghairi")
def get_pid(name):
	process_name = name
	pid = None
	for proc in psutil.process_iter():
    		if process_name in proc.name():
       			pid = proc.pid
	return pid
	
pid_bro_cl = get_pid("client.exe")
pid_bro_gu = get_pid("guardit.exe")
if pid_bro_cl!= None and pid_bro_gu != None :
	print("Client pid : ", pid_bro_cl)
	print("Guardit pid : ", pid_bro_gu)
	def starttimebro(p):
		p.resume()
	def stoptimebro(somepid):
		p = psutil.Process(somepid)
		p.suspend()
		return p
	def client():
		while 1:
			pid_bro_cl = get_pid("client.exe")
			if pid_bro_cl != None:
				p = stoptimebro(pid_bro_cl)
				time.sleep(60)
				starttimebro(p)
				time.sleep(20)
	def Guardit():
		while 1:
			pid_bro_gu = get_pid("guardit.exe")
			if pid_bro_gu != None:
				p = stoptimebro(pid_bro_gu)
				time.sleep(60)
				starttimebro(p)
				time.sleep(20)
	print("Start Hacking time...")
	one_thread = Thread(target=client)
	tow_thread = Thread(target=Guardit)
	one_thread.start()
	tow_thread.start()
else :
	print("bro You are not in an internet cafe .")
