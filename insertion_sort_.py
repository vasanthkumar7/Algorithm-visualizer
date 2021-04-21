import time
def swap(a,b):
    temp=a
    a=b
    b=temp



def insertion_sort(a,drawdata,t):
    
    for i in range(0,len(a)):
        j=0
        mins=-1
        minelement=0
        prev=a[i]
        while(j<i):
            if a[j]>a[i]:
                mins=j
                
                break
            j+=1
            
        if mins!=-1:
            for w in range(i,mins-1,-1):
                a[w]=a[w-1]
                
            
            a[mins]=prev
            drawdata(a,getcolorarray(a,i,mins))
            time.sleep(t)
            
        

    drawdata(a,['green'  for x in range(len(a))])

def getcolorarray(a,l,mins):
    colorarray=[]

    for i in range(len(a)):
        if i!=mins and i<=l:
            colorarray.append("green")
        elif i==mins:
            colorarray.append("white")
        else:
            colorarray.append("red")

    return colorarray

    
    


         

        
            
            
