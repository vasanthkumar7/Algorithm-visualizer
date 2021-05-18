from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import *
import tkinter.scrolledtext as scrolledtext 
from tkinter import messagebox
import random
from queue import PriorityQueue
import time
from tkinter import messagebox
from PIL import ImageTk,Image
import keyboard

#these are all the algorithm part
from bubble_sort_ import *
from selection_sort_ import *
from merge_sort_ import *
from quick_sort_ import *
from insertion_sort_ import *
from linear_search import *
from binary_search import *

root1 = Tk()


p1 = PhotoImage(file = 'bar-chart.png')

root1.iconphoto(False, p1)

#root1.iconbitmap('icon.ico')
menubar = Menu(root1, background='lightblue', foreground='black',
               activebackground='#004c99', activeforeground='white')
filemenu = Menu(menubar, tearoff=0)
filemenu1 = Menu(menubar, tearoff=0)
filemenu2 = Menu(menubar, tearoff=0)


def change_the_root(l):
    global root,root1,root2,root4,root5
    if l ==1:
        root.pack_forget()
        root4.pack_forget()
        root5.pack_forget()
        root2.pack()
        root1.config(bg="white")
    elif l==2:
        root2.pack_forget()
        root4.pack_forget()
        root5.pack_forget()
        root.pack()
        root1.config(bg="black")
    elif l==3:
        root2.pack_forget()
        root.pack_forget()
        root5.pack_forget()
        root4.pack()
        root1.config(bg="white")
    elif l==4:
        root2.pack_forget()
        root.pack_forget()
        root4.pack_forget()
        root5.pack()
        root1.config(bg="white")
        
        
filemenu.add_command(label="Searching and Sorting",command=lambda:change_the_root(2))
filemenu.add_command(label="Path Finding",command=lambda:change_the_root(1))
filemenu1.add_command(label="Documentation",command=lambda:change_the_root(3))
filemenu2.add_command(label="explanation and codes",command=lambda:change_the_root(4))
menubar.add_cascade(label="Visualization Types", menu=filemenu)
menubar.add_cascade(label="       Documentation", menu=filemenu1)
menubar.add_cascade(label="       Explanation & Codes", menu=filemenu2)
root1.config(menu=menubar)

width=root1.winfo_screenwidth()
spacer=(" "*(int(width)//7))
root1.title(spacer+"ALGORITHM VISUALIZER")
root1.config(bg="black")

root=Frame(root1)
root.config(bg="black")
selected_alg=StringVar()
ui_frame=Frame(root,width=600,height=200,bg="grey")
ui_frame.grid(row=1,column=0,padx=10,pady=5)

natural_width=root1.winfo_screenwidth()-100
natural_height=root1.winfo_screenheight()-250

    
    
canvas=Canvas(root,width=natural_width,height=natural_height,bg="#171717")
canvas.grid(row=0,column=0,padx=20,pady=5)

def drawdata(data,colorarray):
    canvas.delete("all")
    c_height=natural_height
    c_width=natural_width
    x_width=c_width/(len(data)+1)
    offset = 5
    spacing =10
    normalize=[i/max(data) for  i in data]
    
    for i,height  in enumerate(normalize):
        x0,y0=i*x_width+offset+spacing,c_height-height*(natural_height-65)
        x1,y1=(i+1)*x_width+offset+spacing,c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorarray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),fill="white")

    root.update_idletasks()
        




data=[]
Label(ui_frame,text="Algorithm: ",bg="grey").grid(row=0,column=0,padx=5,pady=5,sticky=W)



def change_the_case():
    global algmenu,ui_frame1

    generate()
    if algmenu.get()=="Linear search" or algmenu.get()=="Binary search":
        ui_frame1.grid(row=0,column=4)
    else:
        ui_frame1.grid_forget()
        
algmenu=Spinbox(ui_frame,values=('Bubble Sort','Merge Sort',"Insertion Sort","Quick sort","Selection Sort","Linear search","Binary search"),command=change_the_case,state="readonly")
algmenu.grid(row=0,column=1,padx=5,pady=5)

def generate():
    global data
    global algmenu

    minval=int(minv.get())
    maxval=int(maxv.get())
    size=int(sizeentry.get())
   
    
    data=[]
    for i in range(size):
        data.append(random.randrange(minval,maxval+1))

    if algmenu.get()=="Binary search":
        data.sort()

    
        
    drawdata(data,["red" for x in range(len(data))])

def start_alg():
    global data
    global speedscale
    global algmenu
    global l2

    
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
    elif algmenu.get()=="Linear search":
        if l2.get()=="":
            tkinter.messagebox.showinfo(title="visualizer", message="no input given")
        else:
            Linear_search(data,drawdata,speedscale.get(),int(l2.get()))
    elif algmenu.get()=="Binary search":
        if l2.get()=="":
            tkinter.messagebox.showinfo(title="visualizer", message="no input given")
        else:
            binarySearch (data, 0, len(data)-1, int(l2.get()),drawdata,speedscale.get())
    
        
    

        
        
        
    
        

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
    

ui_frame1=Frame(ui_frame,bg="grey")
Button(ui_frame,text="Randomize",command=generate,bg="red").grid(row=0,column=2,padx=5,pady=5,sticky=W)
Button(ui_frame,text="Start",command=start_alg,bg="green").grid(row=0,column=3,padx=5,pady=5,sticky=W)

l1=Label(ui_frame1,text="Find :",bg="grey")
l1.grid(row=0,column=4,padx=5,pady=5,sticky=W)
l2=Entry(ui_frame1)
l2.grid(row=0,column=5,padx=5,pady=5,sticky=W)



sizeentry=Scale(ui_frame,label="SIZE",from_=3,to=60,length=300, orient = HORIZONTAL,command=rig)
sizeentry.grid(row=1,column=0,padx=5,pady=5,sticky=W,columnspan=4)


speedscale=Scale(ui_frame,label="SPEED SCALE (SEC)",from_=0.01,to=1,length=200,resolution=0.01, orient = HORIZONTAL)
speedscale.grid(row=1,column=4,padx=5,pady=5,sticky=W)


minv=Scale(ui_frame,label="MIN VALUE",from_=1,to=10, orient = HORIZONTAL,command=rig2)
minv.grid(row=1,column=5,padx=5,pady=5,sticky=W)


maxv=Scale(ui_frame,label="MAX VALUE",from_=15,to=99, orient = HORIZONTAL,command=rig3)
maxv.grid(row=1,column=6,padx=5,pady=5,sticky=W)

ulla_frame=Frame(root,bg="grey")
ulla_frame.grid(row=0,column=3,padx=2,pady=5,columnspan=2,rowspan=2)
generate()

#pathfinding part
global_row=23
global_column=40

if root1.wininfo_screenwidth()<1366 or root.wininfo_screenheight()<768:
    global_row-=3
    global_column-=3

root2=Frame(root1)
b1354=Frame(root2,bg="black")
box=Frame(b1354)
start=False
des=False
edulai,edulaj=0,0
img1=ImageTk.PhotoImage(Image.open("images/ma.png").resize((20,20),Image.ANTIALIAS))
img2=ImageTk.PhotoImage(Image.open("images/home.png").resize((20,20),Image.ANTIALIAS))
img3=ImageTk.PhotoImage(Image.open("images/heart.png").resize((20,20),Image.ANTIALIAS))
start_ah=False

des_ah=False

wall_ah=False
speed_enna_pah=0.01
grid=[]
grid1=[]
def fs(x1,y1,sx1,sy1,dx2,dy2):
    return abs(x1-sx1)+abs(y1-sy1)+abs(x1-dx2)+abs(y1-dy2)

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

for i in range(global_row):
    f=[]
    for j in range(global_column):
        f.append(0)

    
    grid.append(f)
    
def color_adi(i,j,grid1):
    global start_ah,des_ah,wall_ah,start,des,grid,img1,img2,b1,b2
    global visited
    if start_ah:
        grid1[i][j].config(bg="lightblue",image=img1,width=23,height=20)
        b1.config(bg="lightblue")
        if start!=False:
            visited=[]
            grid1[start[0]][start[1]].config(bg="white",text=" ",width=3,height=1,image="")
            
            
        start=(i,j)
        start_ah=False
    elif des_ah:
        b2.config(bg="#e47ae6")
        grid1[i][j].config(bg="#e47ae6",image=img2,width=23,height=20)
        if des!=False:
            grid1[des[0]][des[1]].config(bg="white",text=" ",width=3,height=1,image="")
        des=(i,j)
        des_ah=False
    elif wall_ah:
        try:
            grid1[i][j].config(bg="black")
            grid[i][j]=1
        except:
            pass

    

def a_star(grid):
    found=0
    global start,des,speed_enna_pah
    openlist=[]
    closedlist=[]
    came_from = {}
    openlist.append(start)

    while len(openlist)!=0 and found!=1:
        fscores_in_open_lsit=[]
        for i in openlist:
            fscores_in_open_lsit.append(fs(i[0],i[1],start[0],start[1],des[0],des[1]))
        q=openlist[fscores_in_open_lsit.index(min(fscores_in_open_lsit))]
        closedlist.append(q)
        openlist.pop(fscores_in_open_lsit.index(min(fscores_in_open_lsit)))
        successor=[]
        successors_f_cost=[]
        
        for i in range(q[0]-1,q[0]+2,1):
            for j in range(q[1]-1,q[1]+2,1):
                if i>=0 and j>=0 and i<len(grid) and j<len(grid) and ((i,j) not in closedlist) and grid[i][j]!=2:
                    successor.append((i,j))
                    openlist.append((i,j))
                    successors_f_cost.append(fs(i,j,start[0],start[1],des[0],des[1]))
        for i in successor:
            if i[0]==des[0] and i[1]==des[1]:
                print("found",i[0],i[1])
                found=1
                break
            else:
                q=successor[successors_f_cost.index(min(successors_f_cost))]
                if q not in closedlist:
                    closedlist.append(q)

        draw(openlist,closedlist,grid1)
        time.sleep(speed_enna_pah)
        
        


def draw_path(path):
    global start,des,img3
    for x in path:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if x[0]==i and x[1]==j:
                    if(x[0]==des[0] and x[1]==des[1]) or (x[0]==start[0] and x[1]==start[1]):
                        grid1[i][j].config(bg="red")
                    else:
                        grid1[i][j].config(bg="red")

                
                    
visited=[]    
def draw(openlist,grid):
    global visited

    path=[]
    for x in openlist:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if x[0]==i and x[1]==j and grid[i][j]["bg"]!="#468ec2" and (i,j) not in path:
                    path.append((i,j))
                    visited.append((i,j))

    for x in path:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if x[0]==i and x[1]==j :
                    grid[i][j].config(bg="#468ec2")

    root1.update_idletasks()

def algorithm( grid, start, end,came_from):
    count = 0
    global grid1
    global speed_enna_pah
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    g_score = {(i,j): float("inf") for i in range(len(grid)) for j in range(len(grid[0]))}
    g_score[start] = 0
    f_score = {(i,j): float("inf") for i in range(len(grid)) for j in range(len(grid[0]))}
    f_score[start] = h(start, end)
    open_set_hash = {start}
    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            return True

        neighbors=[]
        for i in range(current[0]-1,current[0]+2,1):
            for j in range(current[1]-1,current[1]+2,1):
                if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j]!=1:
                    if (i,j)!=start:
                        neighbors.append((i,j))
                            
        for n in neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[n]:
                came_from[n] = current
                g_score[n] = temp_g_score
                f_score[n] = temp_g_score + h(n, end)
                if n not in open_set_hash:
                    count += 1
                    open_set.put((f_score[n], count, n))
                    open_set_hash.add(n)
        
        draw(open_set_hash,grid1)
        time.sleep(speed_enna_pah)
                    
    return False





def reconstruct_path(came_from, current,path):
    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.append(des)

def kandu_pidihitan():
    global grid,start,des
    came_from={}
    path=[]
    if algorithm(grid, start, des,came_from):
        reconstruct_path(came_from, des,path)
        draw_path(path)
    else:
        tkinter.messagebox.showinfo(title="visualizer", message="path not found ")
        


def walls(i,j,grid1):
    global grid
    global start_ah,des_ah,wall_ah,start,des,grid,des,start,edulai,edulaj
    
    if wall_ah:

        if keyboard.is_pressed("w"):
            if start!=False and des!=False:
                if grid1[i][j]["bg"]=="white":
                    grid1[i][j].config(bg="black")
                    grid[i][j]=1
            else:
                wall_ah=False

        if keyboard.is_pressed("c"):
            if start!=False and des!=False:
                if grid1[i][j]["bg"]=="black":
                    grid1[i][j].config(bg="white")
                    grid[i][j]=0
            else:
                wall_ah=False
        

        
        
        
def create_butt(i,j):
    global grid1
    jb=Button(box,text=" ",width=3,height=1,command=lambda:color_adi(i,j,grid1),bg="white")
    
    jb.bind("<Enter>",func=lambda event:walls(i,j,grid1))
    return jb
    
def create_grid():
    global grid1,global_row,global_column
   
    
    
    for i in range(global_row):
        f=[]
        for j in range(global_column):
            f.append(create_butt(i,j))
            f[-1].grid(row=i,column=j)

        grid1.append(f)
        
        
create_grid()

box.grid(row=0,column=0,padx=10,pady=10)

box1_mella=Frame(root2,bg="grey")
box1=Frame(box1_mella,bg="grey")
def clear():

    global grid,grid1,start_ah,wall_ah,des_ahm,start,des,b1,b2


    b1.config(bg="lightblue")
    b2.config(bg="#e47ae6")

    start_ah,wall_ah,des_ah=False,False,False
    start,des=False,False
    global img1,img2
    
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j]=0

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            
                
            grid1[i][j].config(bg="white",text=" ",image="",width=3,height=1)
            grid1[i][j].image = ""
    
    
def assignstart():
    global start_ah,b1
    b1.config(bg="#276ea1")
    b2.config(bg="#e47ae6")
    start_ah=True
def assigndes():
    global des_ah,b2
    b1.config(bg="lightblue")
    b2.config(bg="#c865c9")
    des_ah=True
def assignwall():
    global wall_ah
    wall_ah=True
def start_alg():
    global grid,start_ah,wall_ah,des_ah,des,start,algmenu1,route,route_found,visited
    global visited1,visited2,visited_pos_f ,visited_pos_r ,visited_node_f ,visited_node_r ,route_f ,route_r ,parents
    


    if algmenu1.get()=="A star algorithm":
        kandu_pidihitan()
        start_ah,wall_ah,des_ah=False,False,False
        start,des=False,False
        visited=[]
        route = None
        route_found = False
    elif algmenu1.get()=="Dijkstras algorithm":
        kandu_pidihitan2()
        start_ah,wall_ah,des_ah=False,False,False
        start,des=False,False
        visited=[]
        route = None
        route_found = False
    elif algmenu1.get()=="BFS algorithm":
        kandu_pidihitan3()
        start_ah,wall_ah,des_ah=False,False,False
        start,des=False,False
        visited=[]
        route = None
        route_found = False
    elif algmenu1.get()=="Biderctional":
        
        kandu_pidihitan4()
        start_ah,wall_ah,des_ah=False,False,False
        start,des=False,False
        visited=[]
        route = None

        route_f = []
        route_r = []
        route_found = False
        visited1=[]
        visited2=[]
        
        


#dijkstras algorithm


def kandu_pidihitan4():
    global visited1,visited2,visited_pos_f ,visited_pos_r ,visited_node_f ,visited_node_r ,route_f ,route_r ,parents
    visited1=[]
    visited2=[]
    visited_pos_f = {start}
    visited_pos_r = {des}
    visited_node_f = dict()
    visited_node_r = dict()
    route_f = []
    route_r = []
    parents={}
    route_found = False
    if bidirectional_execute()== False:
        tkinter.messagebox.showinfo(title="visualizer", message="path not found ")
    
 
visited = []
route = None
route_found = False


def kandu_pidihitan3():
    global route_found
    bfs_execute()

    if route_found==False:
        tkinter.messagebox.showinfo(title="visualizer", message="path not found ")
        
    


def kandu_pidihitan2():
    global grid,start_ah,wall_ah,des_ah,des,start,alg_menu1,start,des,visited
    global route,route_found

    

    visited.append(start)
    dist={}
    came_from={}
    path=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j)==start:
                dist[(i,j)]=0
                came_from[(i,j)]=(i,j)
            else:
                dist[(i,j)]=float("inf")
                came_from[(i,j)]=None


    dijkstras(grid,start,start,des,dist,came_from)
    dijkstras_execute()

    visited=[]

    route = None
    route_found = False
    try:
        came_froms(start,des,came_from,path)
        draw_path(path)
    except:
        tkinter.messagebox.showinfo(title="visualizer", message="path not found ")


def print_grid(grid,grid1):
    global start
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==2:
                if grid1[i][j]["bg"]!="yellow" and (i,j)!=start:
                    grid1[i][j].config(bg="yellow")
    root1.update_idletasks()
                    

def checkValid(move):
    global grid
    if move[0]>=0 and move[0]<len(grid) and move[1]>=0 and move[1]<len(grid[0]):
        if grid[move[0]][move[1]]!=1 and move not in visited:
            visited.append(move)
            return True
    return False

def findEnd(first_out,des):
    if first_out == des:
        return True
    return False

def print_grid1(visited):
    global start
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in visited and grid1[i][j]["bg"]!="#468ec2" and (i,j)!=start:
                grid1[i][j].config(bg="#468ec2")

    root1.update_idletasks()
                

def dijkstras_execute():

    global route_found,start,des,grid,route,visited
    queue = [start]
    moves_queue = ['']
    first_out = ''
    first_moves = ''
    path=[]
    global speed_enna_pah

    

    while len(queue) > 0:
            # Parent variables of parent nodes at the given time
        first_out = queue.pop(0)
        first_moves = moves_queue.pop(0)
        for m in ['L', 'R', 'U', 'D','UR','UL','DL','DR']:
            i, j = first_out
                # print('parent:', i, j)
            if m == 'L':
                i -= 1
            elif m == 'R':
                i += 1
            elif m == 'U':
                j -= 1
            elif m == 'D':
                j += 1
            elif m == 'UR':
                i += 1
                j-=1
            elif m == 'UL':
                i-= 1
                j-=1
            elif m == 'DL':
                j += 1
                i-=1
            elif m == 'DR':
                j += 1
                i+=1


            

                # Make new variable "latest_moves" for adding onto the queue again, because you don't want the 'parent' variable to change
            latest_moves = first_moves + str((i,j))+" . "
            if checkValid((i, j)):
                print_grid1(visited)
                time.sleep(speed_enna_pah)
                queue.append((i, j))
                moves_queue.append(latest_moves)

            if findEnd((i, j),des):
                route = latest_moves
                route_found = True
                break
        

        if route_found:
            break

        

def dijkstras(grid,src,start,des,dist,came_from):
    for i in range(start[0]-1,start[0]+2,1):
        for j in range(start[1]-1,start[1]+2,1):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and (i,j)!=src and (i,j)!=start and grid[i][j]==0:
                if dist[(i,j)]>1+dist[start]:
                    came_from[(i,j)]=start
                    dist[(i,j)]=1+dist[start]
                    dijkstras(grid,src,(i,j),des,dist,came_from)
                        
                    
def came_froms(src,des,came_from,path):
    if came_from[des]==src:
        path.append(des)
        path.append(src)
        return True
    else:
        path.append(des)
        came_froms(src,came_from[des],came_from,path)


#bfs algorithm


def bfs_execute():

    global route_found,start,des,grid,route,visited
    queue = [start]
    moves_queue = ['']
    first_out = ''
    first_moves = ''
    path=[]
    global speed_enna_pah
    while len(queue) > 0:
            
        first_out = queue.pop(0)
        first_moves = moves_queue.pop(0)
        for m in ['L', 'R', 'U', 'D','UR','UL','DL','DR']:
            i, j = first_out
            if m == 'L':
                i -= 1
            elif m == 'R':
                i += 1
            elif m == 'U':
                j -= 1
            elif m == 'D':
                j += 1
            elif m == 'UR':
                i += 1
                j-=1
            elif m == 'UL':
                i-= 1
                j-=1
            elif m == 'DL':
                j += 1
                i-=1
            elif m == 'DR':
                j += 1
                i+=1



            latest_moves = first_moves + str((i,j))+" . "
            if checkValid((i, j)):
                print_grid1(visited)
                time.sleep(speed_enna_pah)
                queue.append((i, j))
                moves_queue.append(latest_moves)

            if findEnd((i, j),des):
                route = latest_moves
                route_found = True
                break
        

        if route_found:
            path=break1(route.split(" . "))
            path.append(start)
            draw_path(path)
            break

def break1(l):
    path=[]
    for i in l:
        if i!="":
            k=i.split(",")
            path.append((int(k[0][1:]),int(k[1][:len(k[1])-1])))

    return path


#bidirectonal algorithm


def print_grid2(visited1,visited2):
    global grid1,start,des,visited
    paths=[]
    for i in visited1:
        if i not in visited:
            visited.append(i)
            paths.append(i)
    for i in visited2:
        if i not in visited:
            visited.append(i)
            paths.append(i)
    for i in paths:
        if grid1[i[0]][i[1]]["bg"]!="#276ea1" and (i[0],i[1])!=start  and i in visited1:
            visited.append(i)
            grid1[i[0]][i[1]].config(bg="#276ea1")

        elif grid1[i[0]][i[1]]["bg"]!="#c865c9" and (i[0],i[1])!=des and i in visited2:
            visited.append(i)
            grid1[i[0]][i[1]].config(bg="#c865c9")
    root1.update_idletasks()
                
def checkValid1(node, visited_node, visited_pos):
    if node[0][0]>=0 and node[0][1]>=0 and node[0][0]<len(grid) and node[0][1]<len(grid[1]):
        if node[0] not in visited_pos and grid[node[0][0]][node[0][1]]!=1:
            visited_node[node[0]] = node
            visited_pos.add(node[0])
            return True
    return False

def findRoute( first_out, opp_visited):
    if first_out in opp_visited:
        return True
    return False

def backTrack( opp_visited_node_list, converge_node_pos, first_out):
    global parents

    current = first_out
    current_opp = opp_visited_node_list[converge_node_pos]

    while current is not None:
        route_f.append(current[0])
        
        current = current[1]

    while current_opp is not None:
        route_r.append(current_opp[0])
        
        current_opp = current_opp[1]


count123=0


def combine_list(l1,l2):
    path=l1

    for i in l2:
        path.append(i)

    return path

def bidirectional_execute():
    global route_found,route_r,route_f,count123,speed_enna_pah
    start_node =start
    end_node = des

    start_node =(start, None)
    end_node = (des, None)

    fwd_queue = [start_node]
    rev_queue = [end_node]
    global parents
        # Initialize start/end nodes
    visited_node_f[start_node[0]] = start_node
    visited_node_r[end_node[0]] = end_node


    visited1.append(start_node[0])
    visited2.append(end_node[0])

    while len(fwd_queue) and len(rev_queue) > 0:
            # Parent variables of parent nodes at the given time
        first_out_f = fwd_queue.pop(0)
        first_out_r = rev_queue.pop(0)

        for m in ['L', 'R', 'U', 'D',"UL","UR","DL","DR"]:
            try:
                i, j = first_out_f[0]
            except:
                return False

            try:
                a, b = first_out_r[0]
            except:
                return False
            
            if m == 'L':
                i -= 1
                a -= 1
            elif m == 'R':
                i += 1
                a += 1
            elif m == 'U':
                j -= 1
                b -= 1
            elif m == 'D':
                j += 1
                b += 1
            elif m == 'UR':
                i += 1
                j-=1
                a += 1
                b-=1
            elif m == 'UL':
                i-= 1
                j-=1
                a-= 1
                b-=1
            elif m == 'DL':
                j += 1
                i-=1
                b += 1
                a-=1
            elif m == 'DR':
                j += 1
                i+=1
                b += 1
                a+=1

            new_node_f =((i, j), first_out_f)
            new_node_r =((a, b), first_out_r)
            ethi1=0
            ethi2=0
            if checkValid1(new_node_f, visited_node_f, visited_pos_f):
                    #print(new_node_f.position)
                

                if new_node_f[0] not in visited1:
                    ethi1=1
                    visited1.append(new_node_f[0])
                fwd_queue.append(new_node_f)

            if checkValid1(new_node_r, visited_node_r, visited_pos_r):
                
                if new_node_r[0] not in visited2:
                    ethi2=1
                    visited2.append(new_node_r[0])
                rev_queue.append(new_node_r)


            if ethi1==1 or ethi2==1:
                print_grid2(visited1,visited2)
                time.sleep(speed_enna_pah)


            

                # Check if some route has been found from either ends
            if findRoute((i, j), visited_pos_r):
                route_found = True
                    # Backtrack the route from each ends
                backTrack(visited_node_r, new_node_f[0], first_out_f)
                break

            elif findRoute((a, b), visited_pos_f):
                route_found = True
                backTrack(visited_node_f, new_node_r[0], first_out_r)
                break

        if route_found:
            draw_path(combine_list(route_r[::-1],route_f))
            return True
            break

    return False

def speed_change():
    global speed_enna_pah,algmenu2

    if algmenu2.get()=="Noraml":
        speed_enna_pah=0.01
    elif algmenu2.get()=="Fast":
        speed_enna_pah=0.005
    elif algmenu2.get()=="Super Fast":
        speed_enna_pah=0.001
    else:
        speed_enna_pah=0.1

#documenation
root4=Frame(root1)
root4.config(bg="white")
imag=["documentation/1-Cover.jpg",
"documentation/2-Topics.jpg",
"documentation/3-Topics.jpg",
"documentation/4-Topics.jpg",
"documentation/5-Topics.jpg",
"documentation/6-Topics.jpg"]
docimg=[ImageTk.PhotoImage(Image.open(i).resize((root1.winfo_screenwidth()-200,root1.winfo_screenheight()-200),Image.ANTIALIAS)) for i in imag]
doccount=0
docimages=Label(root4,image=docimg[0])
docimages.grid(row=0,column=0,padx=40,pady=20)
hjk=Frame(root4)
def gor(a):
    global doccount,imag,docimg
    if a==1:
        doccount-=1
    else:
        doccount+=1

    if doccount<0:
        doccount=len(imag)-1
    if doccount>=len(imag):
        doccount=0
    docimages.config(image=docimg[doccount])
forward=Button(hjk,text="<< Backward",command=lambda:gor(1))
forward.grid(row=0,column=0,padx=10,pady=10)
backward=Button(hjk,text="Forward >>",command=lambda:gor(0))
backward.grid(row=0,column=1,padx=10,pady=10)
hjk.grid(row=1,column=0)

#codes and explanation
root5=Frame(root1)
root5.config(bg="white")
imag1=["explanations/1-Title.jpg",
    "explanations/2-Welcome.jpg",
"explanations/3-Welcome-copy-2.jpg",
"explanations/4-Welcome-copy-3.jpg",
"explanations/5-Welcome-copy-1.jpg",
"explanations/6-Welcome-copy-4.jpg",
"explanations/7-Welcome-copy-5.jpg",
"explanations/8-Welcome-copy-6.jpg",
"explanations/9-Welcome-copy-7.jpg",
"explanations/10-Welcome-copy-8.jpg",
"explanations/11-Welcome-copy-9.jpg",
"explanations/12-Welcome-copy-10.jpg",
]

docimg1=[ImageTk.PhotoImage(Image.open(i).resize((root5.winfo_screenwidth()-200,root5.winfo_screenheight()-200),Image.ANTIALIAS)) for i in imag1]
doccount1=0
docimages1=Label(root5,image=docimg1[0])
docimages1.grid(row=0,column=0,padx=40,pady=20)


hjk1=Frame(root5)
def gor1(a):
    global doccount1,imag1,docimg1
    if a==1:
        doccount1-=1
    else:
        doccount1+=1

    if doccount1<0:
        doccount1=len(imag1)-1
    if doccount1>=len(imag1):
        doccount1=0
    docimages1.config(image=docimg1[doccount1])
forward1=Button(hjk1,text="<< Backward",command=lambda:gor1(1))
forward1.grid(row=0,column=0,padx=10,pady=10)

backward1=Button(hjk1,text="Forward >>",command=lambda:gor1(0))
backward1.grid(row=0,column=1,padx=10,pady=10)

hjk1.grid(row=1,column=0)

def change_color_button(which):
    global b1,b2,b3,b4

    if which==1:
        b1.config(bg="#276ea1")
    elif which==2:
        b2.config(bg="#c865c9")
        
wht1=Label(box1,text="Algorithm :",bg="grey")
wht1.grid(row=0,column=0,padx=3)
algmenu1=Spinbox(box1,values=("Dijkstras algorithm","A star algorithm","BFS algorithm","Biderctional"),state="readonly")
algmenu1.grid(row=0,column=1,padx=3,pady=5)
wht2=Label(box1,text="Speed :",bg="grey")
wht2.grid(row=0,column=2,padx=3)
algmenu2=Spinbox(box1,values=("Normal","Fast","Super Fast","Slow"),command=speed_change,state= "readonly")
algmenu2.grid(row=0,column=3,padx=3,pady=5)
b1=Button(box1,text="Source Node",command=assignstart,bg="lightblue")
b1.grid(row=0,column=4,padx=3,pady=5)
b2=Button(box1,text="Destination Node",command=assigndes,bg="#e47ae6")
b2.grid(row=0,column=5,padx=3,pady=5)
b3=Button(box1,text="Walls",command=assignwall,bg="black",fg="white").grid(row=0,column=6,padx=3,pady=5)

b4=Button(box1,text="Visualize",command=start_alg,bg="green").grid(row=0,column=7,padx=3,pady=5)
Button(box1,text="Clear Board",command=clear).grid(row=0,column=8,padx=3,pady=5)

box1.grid(row=0,column=0,padx=20,pady=5)
box1_mella.grid(row=1,column=0)
b1354.grid(row=0,column=0,padx=50,pady=5)
root.pack()
root1.mainloop()
