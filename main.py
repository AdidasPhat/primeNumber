import math

import time


start_time = time.time()
#check số nguyên tố nhỏ hơn căn bậc 2 của n
def isPrimeNumber(n):
    if (n < 2):
        return False
    i = int(math.sqrt(n)) #i=căn bậc 2 của n
    for j in range(2, i + 1): #với j trong khoảng từ 2 đến căn bậc 2 của n
        if (n % j == 0):
            return False
    return True

 
n = int(input("Nhập số nguyên dương n = "))
sqrn=int(math.sqrt(n))
count=1

#tìm số nguyên tố nhỏ hơn căn bậc 2 của n
if (sqrn>=2):
    thislist=[2]
for i in range(3, sqrn + 1):
    if isPrimeNumber(i):
        thislist.append(i) #thêm n là số nguyên tố vào trong thislist
#print(thislist)

def isPrimeNumber1(n):
    if (n < 2):
        return False
    i = int(math.sqrt(n)) #i=căn bậc 2 của n
    for j in thislist: #với j là các số nguyên tố nhỏ hơn căn bậc 2 của n tìm đc
        if (n % j == 0):
            return False
    return True

sb=[]
for j in range(3,n+1): 
    if isPrimeNumber1(j):
        sb.append(j)
sb1=sb+thislist

          
print("số các số nguyên tố nhỏ hơn",n, 'là:')
print(len(sb1))

end_time = time.time()
print("Processing time: ", end_time - start_time)