
import math
import time
start_time=time.time()

def Get_All_Prime_Numbers(n):
    if n<2:
        return []

    if n==2: 
        return [2]
#chia n với mỗi số nguyên tố tìm được trong dãy số nguyên tố nhỏ hơn n

    # prime_number=[2]
    # for a in range (2,n+1):
    #     for b in prime_number:
    #         if a%b==0:
    #             break
    #         if b>int(math.sqrt(a)):
    #             prime_number.append(a)
    #             break
    # return prime_number

#tìm số nguyên tố cơ bản sử dụng hàm check bthuog
    # primelist=[]     
    # for a in range (2,n+1):
    #     i=int(math.sqrt(a))
    #     for b in range(2,i+1):
    #         if a%b==0:
    #             break  
    #     else:
    #         primelist.append(a)
    # return primelist
    
# sử dụng đệ quy trong python
    x=Get_All_Prime_Numbers(n-1)
    for a in x:
        if a<=int(math.sqrt(n)):
            if n%a==0:
                return x
    x.append(n)
    return x


    
x = int(input("Nhập số nguyên dương n = "))
result =  Get_All_Prime_Numbers(x)
print(len(result))

end_time = time.time()
print("Processing time: ", end_time - start_time)
        
        
        
        
