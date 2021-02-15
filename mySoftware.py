import pyttsx3
import os

# pyttsx3.speak("hello gautam good job")

# print()
print("1.open chrome")
print("2.open notepad")
print("enter your choice: ",end="")
x=int(input())

if x==1 :
    os.system("chrome")
elif x==2 :
    os.system("notepad")
else:
    print("out of range",end='')


# listOfFiles={1:"chrome",2:"notepad"}

# os.system(listOfFiles[x])