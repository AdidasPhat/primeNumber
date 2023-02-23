import math
import time
start_time=time.time()

def Get_All_Prime_Numbers(n):
    if n < 2:
        return []
    if n==2:
        return [2]
    x=Get_All_Prime_Numbers(n-1)
    for i in x:
        if i<=int(math.sqrt(n)):
            if n%i==0:
                return x
    x.append(n)
    return x
n=int(input("nhap so nguyen duong n = "))
result=Get_All_Prime_Numbers(n)
print(len(result))

end_time=time.time()
print('proccessing time: ', end_time-start_time)
