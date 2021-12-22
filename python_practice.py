"""from playsound import playsound
playsound('D:\\wasim shaikh\\Python Course with Notes\\1. Chapter 1\\play.mp3')"""


''# import os 
# print(os.listdir())  # to list the folders

# press ctrl +/ to comment multiple lines at a same time 

#type casting 
# a= 2
# float(a)
# print(type(a))

# string functions
# list methods

# l1=[55,6486,21,31,54,2]
# l1.sort() #sorts in ascending order 
# print(l1)

# l1.reverse() 
# print(l1)

# print(min(l1))


# l1.append(7) #adds an obj at the end of the list
# print(l1)

# l1.insert(3,5) #inserts an obj at mentioned index(at 3)
# print(l1)

# l1.remove(6486)
# print(l1)

# l1.pop() #removes an ending obj
# print(l1)''


"""# tuple
a = ("wasim") #tuple can not contain only 1 element withour comma
print(a) #returns a single data type not tuple 
a = ("wasim",) #this will return a tuple 
print(a)"""


# a = (5454, 654,4,45)
# print(a)
# # print(a.count(45))
# # print(a.index(45))
# a= 1
# print(a)

# dictionary methods

'''mydict= {
    "name": "wasim",
    "age": 25,
    "sex":"male"
}
print(mydict.keys())
print(mydict.values())
print(mydict.items()) #returns the (key, value) pair for all contents 
updatedict = {"loves": "almas"}
print(mydict.update(updatedict)) #updates a key value pair within a dictionary  
print(mydict)

# diff between [] and .get() method
print(mydict.get("wasim2")) #returns none if key is not in the dict
print(mydict["wasim2"]) #returns error if the key is not in the dict'''

#set: sets is a collection of non repeatative item.
# set is an immutable type, and the objects can be added and removed
# a = {} this syntax will return an empty dictionary
'''b = set() #this will return an empty set 

b.add(3)
b.add(2)
print(b)

#b.add([4,5]) #unhashable type means list is mutable
b.add((2,4,5)) #immutable data types can be added 
print(b)
b.remove(3)
print(b)
b.pop()
print(b)'''

#finding mean median using numpy
import numpy 
list1 =[19, 22, 34, 26, 32, 30, 24, 24]
print(numpy.median(list1))



pythonic_machine_ages = [19, 22, 34, 26, 32, 30, 24, 24]
def mean(dataset):
    return sum(dataset) / len(dataset)

print(mean(pythonic_machine_ages))

list1 =[19, 22, 34, 26, 32, 30, 24, 24]

def maxi(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max
print( maxi(list1))





 







