import math
import time
start_time=time.time()

def Get_All_Prime_Numbers(n):
    primelist=[]
    i=int(math.sqrt(n))
    if n<2:
        primelist=[]
    if n==2:
        primelist=[2]
    for b in range(2,i+1):
        if n%b==0:
            return primelist       
    else:
        primelist.append(n)
    return primelist
    
n=int(input('nhap so nguyen duong n'))
primelist=[]
for j in range (2, n -1):
    Get_All_Prime_Numbers(j)
    print(primelist)





    
    

