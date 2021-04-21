import time

def bub_sort(a,drawdata,timetick):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                temp=a[j+1]
                a[j+1]=a[j]
                a[j]=temp
                drawdata(a,['green' if x==j or x==j+1 else 'red' for x in range(len(a))])
                time.sleep(float(timetick))
    drawdata(a,['green'  for x in range(len(a))])

    
            


            
