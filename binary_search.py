import time
from tkinter import messagebox
import tkinter
def binarySearch (a, l, r, x,drawdata,t):
    if r >= l:
        mid = l + (r - l) // 2
        if a[mid] == x:
            drawdata(a,["green" if x==mid else "red" for x in range(len(a))])
            tkinter.messagebox.showinfo(title="visualizer", message="element found at index: "+str(mid+1))
            
        elif a[mid] > x:
            drawdata(a,getcolorarray(len(a),l,mid-1))
            time.sleep(t)
            return binarySearch(a, l, mid-1, x,drawdata,t)
        else:
            drawdata(a,getcolorarray(len(a),mid+1,r))
            time.sleep(t)
            return binarySearch(a, mid + 1, r, x,drawdata,t)
    else:
        tkinter.messagebox.showinfo(title="visualizer", message="element is not found")

def getcolorarray(l,left,right):
    colorarray=[]
    for i in range(l):
        if i>=left and i<=right:
            colorarray.append("#424bf5")
        else:
            colorarray.append("red")

    return colorarray
