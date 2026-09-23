# A list in Python is a collection used to stoe multiple values in a single variable.

data=[10,"Python",3.14,True]
print(data)

# ----- List Methods -----

# Creating a List
numbers=[10,20,30,40]
print("Orignal List :",numbers)

# 1. append()
# Adds one element at the end of the list
numbers.append(50)
print("append() :",numbers)

# 2. extend()
# Adds multiple elements to the end 
numbers.extend([60,70])
print("extend() :",numbers)

# 3. insert()
# Inserts an element at a specifix index
numbers.insert(1,15)
print("insert() :",numbers)

# 4. remove() #Remove the first occurance of a Value
numbers.remove(20)
print("remove() :",numbers)

# 5. pop() #Removes and returns an element

removed = numbers.pop()
print("pop():",numbers)
print("Removed :",removed)

# pop(index)

removed = numbers.pop(1)
print("pop(1) :", numbers)
print("Removed",removed)

# 6. clear() 
# Removes all elements

temp = [1,2,3,4]
temp.clear()
print("clear():",temp)

# 7. index() 
#Returns the index of the first occurance 
numbers = [10,20,30,40]
position = numbers.index(30)
print("index():", position)

# 8. count()
#Returns the number of occurances of a value 
count = numbers.count(20)
print("count():",count)

# 9. sort()  Sorts the list in ascending order
numbers.sort()
print("sort():", numbers)

# 10. reverse() Reverses the list
numbers.reverse()
print("reverse():",numbers)