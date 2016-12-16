#!python
import time
from daemon import runner
import threading

class App():
    x=1
    name="sample python daemon"
    workerThread=None
    keepLooping=True
    def __init__(self):
        self.pid = 0 ##getPid() ##TBD
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/pythonDaemon.pid'
        self.status_path  =  '/tmp/pythonDaemon.status' 
        self.pidfile_timeout = 5

    def run(self):
        import IPython
        statusString="Howdy! Starting  %d %s"%(self.x, self.name)
        self.writeStatus(statusString)

        t1=threading.Thread(target=self.runScript, args=())
        t1.start()
        self.workerThread=t1
        ##IPython.embed_kernel()
        
        return "done"

    def writeStatus(self, statusString):
        with open(self.status_path, 'w') as f:
            f.write(statusString)
            
    def runScript(self):
        while self.keepLooping:
            
            #print(statusString )
            self.x=self.x+1
            statusString="continuing the Howdy!  %d %s"%(self.x, self.name)
            self.writeStatus(statusString)
            time.sleep(10)
        statusString="Finished the loop!  %d %s"%(self.x, self.name)
        self.writeStatus(statusString)
        
    def stop(self):
        statusString="Finished!  %d %s"%(self.x, self.name)
        self.writeStatus(statusString)

    def status(self):
        with open(self.status_path, 'r') as f:
            lines=f.read()
            print lines

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()


##start at shell with ./daemonApp.py start
##this will echo script every 10 seconds
##stop with ./daemonApp.py stop
##view the status with ./daemonApp.py status



##remote in to python console 
##pyrasite-shell <PID>
##access 
##app.name
##'sample python daemon'
##app.x   ##see this value increment
##8
##app.keepLooping
##True
##app.keepLooping=False  ##This will end the infinite loop at the next interval

