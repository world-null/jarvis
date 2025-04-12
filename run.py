import multiprocessing
from engine.features import hotword
from main import start


# to run jarvis
def startJarvis():
    # code for process 1
    print("process 1 is running")
    start()

# to run hotword
def listenHotWord():
    # code for process 2
    print("process 2 is running")
    hotword()

# start both process
if __name__=='__main__':
    p1=multiprocessing.Process(target=startJarvis)
    p2=multiprocessing.Process(target=listenHotWord)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

        print("system stop")
