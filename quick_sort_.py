import time


def partisition(a,li,hi):
    
    pi=a[hi]
    i=li-1

    for j in range(li,hi):
        if a[j]<pi:
            i+=1
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            

    

    
            
    temp=a[i+1]
    a[i+1]=a[hi]
    a[hi]=temp

    

    return i+1

def quicksort(a,li,hi,drawdata,t):
    if hi>li:
        pi=partisition(a,li,hi)
        drawdata(a,getcolorarray(len(a),li,pi,hi))
        time.sleep(t)
        quicksort(a,li,pi-1,drawdata,t)
        quicksort(a,pi+1,hi,drawdata,t)


def getcolorarray(l,left,middle,right):
    colorarray=[]

    for i in range(l):
        if i>=left and i<=right:
            if i>=left and i<middle:
                colorarray.append("yellow")
            elif i==middle:
                colorarray.append("white")
            else:
                colorarray.append("#424bf5")
        else:
            colorarray.append("red")

    return colorarray
