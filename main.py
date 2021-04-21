from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import *
import tkinter.scrolledtext as scrolledtext 

import random
from bubble_sort_ import *
from selection_sort_ import *
from merge_sort_ import *
from quick_sort_ import *
from insertion_sort_ import *
root = Tk()
root.title("Algorithm visualizer")

root.config(bg="black")
selected_alg=StringVar()
ui_frame=Frame(root,width=600,height=200,bg="grey")


ui_frame.grid(row=1,column=0,padx=10,pady=5)

canvas=Canvas(root,width=900,height=530,bg="#171717")
canvas.grid(row=0,column=0,padx=10,pady=5)

def drawdata(data,colorarray):
    canvas.delete("all")
    c_height=530
    c_width=900
    x_width=c_width/(len(data)+1)
    offset = 5
    spacing =10
    normalize=[i/max(data) for  i in data]
    
    for i,height  in enumerate(normalize):
        x0,y0=i*x_width+offset+spacing,c_height-height*465
        x1,y1=(i+1)*x_width+offset+spacing,c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorarray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),fill="white")

    root.update_idletasks()
        




data=[]
Label(ui_frame,text="Algorithm: ",bg="grey").grid(row=0,column=0,padx=5,pady=5,sticky=W)


def rem():
   
    global songbox
    songbox.delete(0,END)
    
def open_doc():
    global txt
    global songbox
    global algmenu
    global what_in
    global wht
    global b1,b2

    

    rem()


    wht.configure(text=algmenu.get())
    if what_in=="e":
        b1.configure(bg="black",fg="white")
        b2.configure(bg="white",fg="black")
        text_file=open("explanations\\"+algmenu.get()+".txt","r")
    else:
        b2.configure(bg="black",fg="white")
        b1.configure(bg="white",fg="black")
        text_file=open("codes\\"+algmenu.get()+".txt","r")
        
    stuff=text_file.read()

    dgf=""
    lables=[]
    for i in stuff:
        if i=="\n":
            lables.append(dgf)
            dgf=""
        else:
            dgf+=i

    for i in range(len(lables)):
        songbox.insert(END,lables[i])
        
algmenu=Spinbox(ui_frame,values=('Bubble Sort','Merge Sort',"Insertion Sort","Quick sort","Selection Sort"),command=open_doc)
algmenu.grid(row=0,column=1,padx=5,pady=5)

def generate():
    global data
    

    try:
        minval=int(minv.get())
    except:
        minval=5

    try:
        maxval=int(maxv.get())
    except:
        maxval=40

    try:
        size=int(sizeentry.get())
    except:
        size=30

    if minval<0:
        minval=0
    if maxval>100:
        maxval=100
    
        


    data=[]

    for i in range(size):
        data.append(random.randrange(minval,maxval+1))
    drawdata(data,["red" for x in range(len(data))])

def start_alg():
    global data
    global speedscale
    global algmenu

    
    if algmenu.get()=='Bubble Sort':
        bub_sort(data,drawdata,speedscale.get())
    elif algmenu.get()=='Merge Sort':
        merge_sort(data,0,len(data),drawdata,speedscale.get())
    elif algmenu.get()=="Insertion Sort":
        insertion_sort(data,drawdata,speedscale.get())
    elif algmenu.get()=="Quick sort":
        quicksort(data,0,len(data)-1,drawdata,speedscale.get())
        drawdata(data,["green"  for x in range(len(data))])
    elif algmenu.get()=="Selection Sort":
        sel_sort(data,drawdata,speedscale.get())
    
        

what_in="e"

def change_waht(a):
    global what_in

    what_in=a

    open_doc()

    

len_son=0

def rig(e):
    generate()

def rig2(e):
    generate()

def rig3(e):
    generate()
    
    
Button(ui_frame,text="Generate",command=generate,bg="red").grid(row=0,column=2,padx=5,pady=5,sticky=W)
Button(ui_frame,text="Start",command=start_alg,bg="green").grid(row=0,column=3,padx=5,pady=5,sticky=W)



sizeentry=Scale(ui_frame,label="SIZE",from_=3,to=60,length=300, orient = HORIZONTAL,command=rig)
sizeentry.grid(row=1,column=0,padx=5,pady=5,sticky=W,columnspan=4)


speedscale=Scale(ui_frame,label="SPEED SCALE",from_=0.1,to=1,length=200,resolution=0.1, orient = HORIZONTAL)
speedscale.grid(row=1,column=4,padx=5,pady=5,sticky=W)


minv=Scale(ui_frame,label="MIN VALUE",from_=1,to=10, orient = HORIZONTAL,command=rig2)
minv.grid(row=1,column=5,padx=5,pady=5,sticky=W)


maxv=Scale(ui_frame,label="MAX VALUE",from_=15,to=99, orient = HORIZONTAL,command=rig3)
maxv.grid(row=1,column=6,padx=5,pady=5,sticky=W)




ulla_frame=Frame(root,bg="grey")
ulla_frame.grid(row=0,column=3,padx=2,pady=5,columnspan=2,rowspan=2)

ulla_frame3=Frame(ulla_frame,bg="grey")

wht=Label(ulla_frame3,text="Algorithm",font=("arial",15),bg="grey")
wht.grid(row=0,column=0,padx=5)
b1=Button(ulla_frame3,text="Explanation",command=lambda:change_waht("e"))
b1.grid(row=0,column=1,padx=5)
b2=Button(ulla_frame3,text="Code",command=lambda:change_waht("c"))
b2.grid(row=0,column=2,padx=5)
ulla_frame3.grid(row=0,column=0,padx=2,pady=5)
ui_frame2=Frame(ulla_frame,bg="grey")


ui_frame2.grid(row=1,column=0,padx=2,pady=5)

myscroll2=Scrollbar(ui_frame2,orient=HORIZONTAL)
myscroll=Scrollbar(ui_frame2,orient=VERTICAL)
songbox=Listbox(ui_frame2,width=45,height=30,borderwidth=0,bg="#171717",fg="white",yscrollcommand=myscroll.set,font=("arial",13),xscrollcommand=myscroll2.set)
myscroll.config(command=songbox.yview)
myscroll2.config(command=songbox.xview)
myscroll.pack(side=RIGHT,fill=Y)
myscroll2.pack(side=BOTTOM,fill=X)
songbox.pack()


generate()
open_doc()

root.mainloop()
