# pythonLinuxService
Python utilities running as linux services in the background as daemons
## daemonApp
1. start at shell with ./daemonApp.py start -- this will echo script every 10 seconds
2. stop with ./daemonApp.py stop
3. view the status with ./daemonApp.py status
 -- continuing with loop x=13 sample python daemon

###remote in to python console 
/opt/anaconda/bin/pyrasite-shell PID

```python
app.name
'sample python daemon'
app.x   ##see this value increment
8
app.keepLooping
True
app.keepLooping=False  ##This will end the infinite loop at the next interval

```
##daemonApp4IPython
1. start at shell with ./daemonApp4IPython.py start --this will echo script every 10 seconds
2. stop with ./daemonApp4IPython.py stop
3. view the status with ./daemonApp4IPython.py status


###remote in to ipython console 

/opt/anaconda/bin/ipython console --existing kernel-3358.json

####access self variable
```python
self.name
'sample python daemon'
self.x   ##see this value increment
8
self.keepLooping
True
self.keepLooping=False  ##This will end the infinite loop at the next interval

```
