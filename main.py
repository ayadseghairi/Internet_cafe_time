import psutil
from threading import Thread
import time
def get_pid(name):
        process_name = name
        pid = None
        for proc in psutil.process_iter():
                if process_name in proc.name():
                        pid = proc.pid
        return pid
def stoptimebro(somepid):
        p = psutil.Process(somepid)
        p.suspend()
        time.sleep(60)
        p.resume()
        time.sleep(20)
def client():
        while 1:
                pid_bro_cl = get_pid("client.exe")
                if pid_bro_cl != None
                        stoptimebro(pid_bro_cl)
def Guardit()
        while 1:
                pid_bro_gu = get_pid("guardit.exe")
                if pid_bro_gu != None
                        stoptimebro(pid_bro_gu)

one_thread = Thread(target=client)
tow_thread = Thread(target=Guardit)
one_thread.start()
tow_thread.start()
