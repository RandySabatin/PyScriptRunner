import sys
import os
import signal
import multiprocessing
from multiprocessing import Process
import importlib

### add libraries to be imported by external script ###
import time
###

if getattr(sys, 'frozen', False): 
    VAR_CWD = os.path.dirname(sys.executable)
    sys.path.insert(1, VAR_CWD)

sys.path.insert(1, os.getcwd())

def handlerSIGINT(signum, frame):
    try:
        print("Ctrl-c was pressed.")
        sys.exit(0) 
    except Exception as err:
        print("handler" + str(err))
#end def

def executeScript(moduleName):
    
    try:
        signal.signal(signal.SIGINT, handlerSIGINT) #create a CTRL-C handler on child process
        current_module = importlib.import_module(moduleName)

        #To call your script's main() method 
        if hasattr(current_module, 'main'):
            current_module.main()
       
        return
    except Exception as err:
        print("Child process encountered an exception: " + str(err)) 
#end def

if __name__ == '__main__':
    try:
        multiprocessing.freeze_support()    #to support multi-thread/multi-process with pyinstaller
        signal.signal(signal.SIGINT, handlerSIGINT) #create a CTRL-C handler

        if len(sys.argv) > 1:
            script = sys.argv[1]
            module = os.path.splitext(os.path.basename(script))[0]
        else:
            print("No script name was provided")
            sys.exit(0)

        runProcess = Process(target=executeScript, args=(module,))
        runProcess.start()
        runProcess.join()

    except Exception as err:
        print("Main process encountered an exception: " + str(err)) 


