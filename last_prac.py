# import random
# randl=random.sample(range(1,20), 5)
# print(randl)
# randl=[10, 12, 4, 17, 16]



# def min1(x):
#     min=randl[0]
#     for i in randl:
#         if i<min:
#             min=i
#     return min
# print("min",min1(randl))

# def max1(x):
#     max=randl[0]
#     for i in randl:
#         if i>max:
#             max=i
#     return max
# print("max",max1(randl))

# n=len(randl)
# def mean1(x):
#     sum1=0
#     for i in range(0,n):
#         sum1=sum1+randl[i]
#     return sum1/n
# print("mean", mean1(randl))

# randl.sort()
# def median1(x):
#     if n%2==0:
#         median1 =randl[n//2]
#         median2=randl[n//2-1]
#         median=(median1+median2)/2
#     else:
#         median=randl[n//2]
#     return median
# print("median", median1(randl))


num=int(input("enter a number: "))
def factorial1(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact
print(factorial1(num))


print("welcome")
p=int(input("enter the pin"))
if p==1234:
    print("1-withdraw\n2-balance inquiry")
    t=int(input("choose your transaction: "))
    if t==1:
        w=int(input("please enter the amount"))
        if w%100!=0:
            print("enter the amount multiple of 100")
        elif w<=20000:
            print("pleae collect your cash\nThank you")
        elif w>20000:
            print("insufficiant balance")
    elif t==2:
        print("Your available balance is 200000")
else:
    print("invalid pin")
        
