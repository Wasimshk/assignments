'''
i = 0
j = 0
k = 5
for i in range(0, 51, 5):
    if i==0:
        continue
    if j<11:
        j+=1
    print(j, "X", k, "=", i)'''

'''text1 = "wasim"

print(text1[::-1])'''


'''i = 0
while i <= 10:
    print(i)
    i+=1'''
    
"""
def maximum(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i]>max:
            max = arr[i]
            return max
arr = [5454,464,654,8754,6532]
n = len(arr)
ans = maximum(arr, n)
print(ans) 
"""

#list1 = [10, 20,5645,46986, 4, 45]
#list1.sort()
#print(list1[-1]) method 1 


#print(max(list1)) method 2

#method 3

"""def Largestno(list1):
    max = list1[0]
    for i in list1:
        if i>max:
            max = i
    return max
list1 = [10, 20,5645,14986, 4, 45]
print("the maximum value is: ", Largestno(list1))"""


"""a = int(input("enter the 1st number: "))
b = int(input("enter the 2nd number: "))
c = int(input("enter the 3rd number: "))
d = int(input("enter the 4tt number: "))

if a>b:
    f1=a
else:
    f1=b
if c>d:
    f2=c
else:
    f2=d
if f1>f2:
    print("the greatest value is:", f1)
else:
    print("the greatest value is:", f2)"""

"""sub1 = int(input("Enter the sub1 marks: "))
sub2 = int(input("Enter the sub2 marks: "))
sub3 = int(input("Enter the sub3 marks: "))

if sub1 < 33 or sub2 < 33 or sub3 < 33:
    print("Sorry! You failed in the exam")
elif (sub1+sub2+sub3)/3 < 40:
    print("Sorry! You failed in the exam")
elif sub1 > 100 or sub2 > 100 or sub3 > 100:
    print("invalid marks")
else:
    print("Congratulations! You have cleared the exam")"""


'''spam1 = ["make a lot of money", "buy now", "subscribe this"]
text2 = input("enter the text:")
if text2 in spam1:
    print("this is spam")
else: 
    print("this is not spam")'''

'''my_marks = int(input("Enter the marks\n"))
if my_marks >= 90:
    grade = "O"
elif my_marks >= 75:
    grade = "A"
elif my_marks >= 60:
    grade = "B"
elif my_marks >= 50:
    grade = "C"
elif my_marks >= 40:
    grade = "D"
else:
    grade = "F"
print("your grade is:", grade)
'''


'''print("Maximum of 4,12,151,43.3,19 and 100 is : ")
print (max( 4,12,43.3,151,19,100 ))'''



'''list1.sort()

print(list1[-1])'''

"""list1=[4,12,0.5,43.3,151,19,1]
def mminimum1(list1):
    min = list1[0]
    for i in list1:
        if i < min:
            min=i
    return min
print("maximum number is:", mminimum1(list1))
"""

'''i=0
while i<=50:
    print(i)
    i +=1
print("done")'''

'''for i in range(0,51,5):
    if i == 0:
        continue
    print(i)'''

'''num = int(input("enter a number: "))
for i in range(-10, 0):
    print(num,"X",-i, "=", num*-i)'''
'''
num = int(input("Enter a number to get the multiplication table: \n"))
for i in range(1,11):
    print(num, "X", i, "=", num*i)'''

'''List1 = ["wasim", "azim", "irshad", "wajid", "shaukat"]
for name in List1:
    if name.startswith("wa"):
    print("assalamu alaikum", name)'''

'''num = int(input("enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i
print("the factorial of this number is ", factorial)'''


'''string1 = "IT IS IN LOWERCASE."  
string1 = string1.swapcase()
print(string1)'''



"""def max1(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max=i
    return max
print("maximum number is:", max1(list1))"""

'''list1=[4,12,0.5,43.3,151,19,1]
def max1(list1):
    max=list1[0]
    for i in list1:
        if i>max:
            max=i
    return max
print(max1(list1))'''

'''list1=[4,12,0.5,43.3,151,19,1]
def max1(list1), :
    max = list1[0]
    min = list1[0]
    for i in list1:
        if i> max:
            max=i
    
    for j in list1:
        if j< min:
            min=j
    return (max, min) 

print("the max is ", max1(list1), "&", "the min is",  min1(list1) )'''

'''import random
def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater = []
    items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort(random.sample(range(20, 50), 10)))'''


import random
rand=random.sample(range(1,5),3)
print(rand)



def factorial(n):
    factorial1=1
    for i in range(n):
        factorial1=factorial1*(i+1)
    return factorial1
print(factorial(3))