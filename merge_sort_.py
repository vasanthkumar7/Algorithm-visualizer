import time
def merge(a,l,m,r,drawdata,t):
    drawdata(a,getcolorarray(len(a),l,m,r))
    time.sleep(t)
    
    f=a[l:m+1]
    g=a[m+1:r+1]
    i=0
    j=0
    k=l
    
    while i<len(f) and j<len(g):
        if f[i]<g[j]:
            a[k]=f[i]
            i+=1
            k+=1
        else:
            a[k]=g[j]
            j+=1
            k+=1
    if i!=len(f):
        while(i<len(f)):
            a[k]=f[i]
            i+=1
            k+=1
    if j!=len(g):
        while(j<len(g)):
            a[k]=g[j]
            j+=1
            k+=1

    drawdata(a,["green" if x>=l and x<=r else "red" for x in range(len(a))])
    time.sleep(t)

    

    

    
    
        
            
def merge_sort(a,l,r,drawdata,t):
    if l<r:
        m=int((l+r)/2)
        merge_sort(a,l,m,drawdata,t)
        merge_sort(a,m+1,r,drawdata,t)
        
        merge(a,l,m,r,drawdata,t)
        
def getcolorarray(l,left,middle,right):
    colorarray=[]

    for i in range(l):
        if i>=left and i<=right:
            if i>=left and i<=middle:
                colorarray.append("yellow")
            else:
                colorarray.append("#424bf5")
        else:
            colorarray.append("red")

    return colorarray
                
        



    
