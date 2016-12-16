#!python
import time
from daemon import runner
import threading

class App():
    """
    An app to run as a Linux service in the background.  This app is
    designed to run with minimal user interaction but will facilitate
    that interaction when necessary.
    """
    x=1
    name="me"
    workerThread=None
    keepLooping=True
    def __init__(self):

        """
        This is the primary information for the app class.  This
        contains the status file path and the processID (pid) path.
        """
        self.pid = 0 ##getPid() ##TBD
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/IPythonDaemon.pid'
        self.status_path  =  '/tmp/IPythonDaemon.status' 
        self.pidfile_timeout = 5

    def run(self):
        """
        The function that runs when the "start" function is called.
        This is what python will do to start the worker thread and the
        IPython kernel in the background.  Users can access the ipython console  with 
        ipython console --existing kernel-<pid>.json

        where pid is the pid above
        """
        import IPython
        statusString="Howdy! Starting  %d %s"%(self.x, self.name)
        self.writeStatus(statusString)

        t1=threading.Thread(target=self.runScript, args=())
        t1.start()
        self.workerThread=t1
        IPython.embed_kernel()
        
        return "done"

    def writeStatus(self, statusString):
        """
        Write status string to the status_path file
        """
        with open(self.status_path, 'w') as f:
            f.write(statusString)
            
    def runScript(self):
        """
        Here is what python (IPython) will do in the background as a
        process.  As a default, this only loops through an
        (semi)infinite loop and increments a number.  Change this to
        whatever you want to do instead.
        """
        while self.keepLooping:
            
            #print(statusString )
            self.x=self.x+1
            statusString="continuing the Howdy!  %d %s"%(self.x, self.name)
            self.writeStatus(statusString)
            time.sleep(10)
        statusString="Finished the loop!  %d %s"%(self.x, self.name)
        self.writeStatus(statusString)
        
    def stop(self):
        """
        Execute this to stop the process.  This will run a cold-kill
        through the command terminal.  Same as kill -9 pid.
        """
        statusString="Finished!  %d %s"%(self.x, self.name)
        self.writeStatus(statusString)

    def status(self):
        """
        
        """
        with open(self.status_path, 'r') as f:
            lines=f.read()
            print lines

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()


##start at shell with ./daemonApp4IPython.py start
##this will echo script every 10 seconds
##stop with ./daemonApp4IPython.py stop
##view the status with ./daemonApp4IPython.py status


##remote in to ipython console 
##ipython console --existing kernel-3358.json
##access self variable
##self.name
##'sample python daemon'
##self.x   ##see this value increment
##8
##self.keepLooping
##True
##self.keepLooping=False  ##This will end the infinite loop at the next interval
