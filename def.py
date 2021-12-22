# mean, median, min, max using user defined function

'''l1=[1,2,4,3,5]
def mean1(x):
    sum1=0
    n=len(l1)
    for i in range(0,n):
        sum1=sum1+l1[i]
    return sum1/n
print(mean1(l1))

l1=[1,2,4,3,5]
n=len(l1)
l1.sort()
def median1(x):
    if n%2==0:
        median1 =l1[n//2]
        median2 =l1[n//2-1]
        median= (median1+median2)/2
    else:
        median=l1[n//2]
    return median
print(median1(l1))

l1=[1,2,4,3,5]
def max1(x):
    max=l1[0]
    for i in l1:
        if i > max:
            max=i
    return max
print(max1(l1)) 

def min1(x):
    min=l1[0]
    for i in l1:
        if i<min:
            min = i
    return min
print(min1(l1))'''


# ATM operation

'''print("welcome")
p=int(input("enter the pin: "))
if p==1234:
    print("1-withdraw\n2-account balance")
    t=int(input("choose your transaction: "))
    if t==1:
        w=int(input("enter the amount"))
        if w>20000:
            print("invalid amount")
        else:
            print("collect your cash\nThank you")
    elif t==2:
        print("your account balance is 20000")
else:
        print("invalid pin")

'''

# import random 
# rand_list = random.sample(range(1, 50), 10)
# print(rand_list)

# rand_list = [14, 15, 9, 34, 37, 47, 40, 49, 25]
# n=len(rand_list)
# def mean1(x):
#     sum1=0
#     for i in range(0,n):
#         sum1 = sum1 + rand_list[i]
#     return sum1/n
# print(mean1(rand_list))

# rand_list.sort()

# def median1(x):
#     if n%2==0:
#         median1=rand_list[n//2]
#         median2=rand_list[n//2-1]
#         median=(median1+median2)/2
#     else:
#         median=rand_list[n//2]
#     return median
# print(median1(rand_list))




# import random
# rand = random.sample(range(1,10), 5)
# print(rand)

rand = [3, 6, 4, 9, 7]
def max1(x):
    max=rand[0]
    for i in rand:
        if i>max:
            max=i
    return max
print(max1(rand))

def min1(x):
    min = rand[0]
    for i in rand:
        if i<min:
            min=i
    return min
print(min1(rand))



n=len(rand)
def mean(x):
    sum1=0
    for i in range(0,n):
        sum1+=rand[i]
    return sum1/n
print(mean(rand))

rand.sort()
def median(x):
    if n%2==0:
        median1=rand[n//2]
        median2=rand[n//2-1]
        median=(median1+median2)/2
    else:
        median=rand[n//2]
    return median 
print(median(rand))

print("welcome")
p=int(input("Enter your ATM PIN"))
if p==1234:
    print("1-withdraw\n2-balance inquiry")
    t=int(input("Choose your transaction: "))
    if t==1:
        w=int(input("enter the amount: "))
        if w%100!=0:
            print("please enter the amount multiple of 100")
        elif w<=25000:
            print("please collect your cash\nThank you")
        else:
            print("insufficiant balance")
    elif t==2:
        print("your available balance is 25000")
else:
    print("invalid pin")