#Q.1- Print the current day using Datetime module.

from datetime import date
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days[date.weekday(date.today())])

#Q.2- Open your browser and play a video using webbrowser module in python.

import webbrowser
webbrowser.open('https://www.youtube.com/watch?v=MQ1PBPdUVB8')

#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.

import os
os.rename('abc.txt','abc.jpg')
