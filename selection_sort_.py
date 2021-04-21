
import time
def sel_sort(a,drawdata,t):

    for i in range(len(a)-1):
        mins=i
        for j in range(i+1,len(a)):
            if a[j]<a[mins]:
                mins=j
                
        if mins!=i:
            drawdata(a,['green' if x==mins or x==i else 'red' for x in range(len(a))])
            time.sleep(t)
            temp=a[mins]
            a[mins]=a[i]
            a[i]=temp
            

    drawdata(a,['green'  for x in range(len(a))])
        



            
