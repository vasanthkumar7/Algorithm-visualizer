import time
import tkinter

from tkinter import messagebox

def Linear_search(a,drawdata,timetick,find):
    for i in range(len(a)):
        if a[i]==find:
            drawdata(a,['green' if x==i  else 'red' for x in range(len(a))])
            tkinter.messagebox.showinfo(title="visualizer", message="element found at index: "+str(i+1))
            return
        else:
            drawdata(a,['white' if x==i  else 'red' for x in range(len(a))])
        time.sleep(float(timetick))


    drawdata(a,['red'  for x in range(len(a))])

    tkinter.messagebox.showinfo(title="visualizer", message="element is not found")

    

    
    
