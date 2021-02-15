import pyttsx3
import os

# pyttsx3.speak("hello gautam good job")

# print()
while True:

    print("1.open chrome")
    print("2.open notepad")
    print("enter your choice: ",end="")
    x=input()

    if ("run" in x) and (("google" in x) or ("chrome" in x)) :
        os.system("chrome")
    elif ("run" in x) and (("notepad" in x) or ("editor" in x)) :
        os.system("notepad")
    elif "exit" in x or "quit" in x:
        break
    else:
        print("out of range",end='')
	    


# listOfFiles={1:"chrome",2:"notepad"}

# os.system(listOfFiles[x])