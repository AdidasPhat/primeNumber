import math
import time

start_time=time.time()

def Get_All_Prime_numbers(n):
    # if n<2:
    #     return []
    # if n == 2:
    #     return [2]
    # #hàm tìm số nguyên tố cơ bản

    # list = [2]
    # for a in range(3,n+1):
    #     i=int(math.sqrt(a))
    #     for b in range(2,i+1):
    #         if a%b==0:
    #             break
    #     else:
    #         list.append(a)
    # return list

 
    # chia n cho a là số nguyên tố nhỏ hơn căn bậc 2 của n

    # list=[2]
    # for a in range (3,n+1):
    #     for b in list:
    #         if a%b==0:
    #             break
    #         if b>int(math.sqrt(a)):
    #             list.append(a)
    #             break
    #     else:
    #         list.append(a)
    # return list
                
    # if n<2:
    #     return []
    # if n==2:
    #     return [2]
    # prime_list=[2]
    # for i in range(3,n+1):
    #     for j in prime_list:
    #         if j>int(math.sqrt(i)):
    #             prime_list.append(i)
    #             break
    #         if i%j==0:
    #             break
    #     else:
    #         prime_list.append(i)
    # return prime_list

    #đệ quy  

    # x=Get_All_Prime_numbers(n-1)
    # for a in x:
    #     if a<=int(math.sqrt(n)):
    #         if n%a==0:
    #             return x
    # x.append(n)
    # return x

#chia n cho tập hợp các số nguyên tố nhỏ hơn căn bậc 2 của n
    if n<2:
        return []
    if n==2:
        return [2]
    list=[2]    
    for i in range(3,n+1):
        for j in list:
            if j>int(math.sqrt(i)):
                list.append(i)
                break
            if i%j==0:
                break
        else:
            list.append(i)
    return list

n=int(input("nhap so nguyen duong n = "))
result=Get_All_Prime_numbers(n)
print(len(result))

end_time=time.time()
print('processing time: ',end_time-start_time)