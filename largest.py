


# By Loop

NUM = [1, 2, 3, 1, 3]
largest = NUM[0]

for i in NUM:
    if i > largest:
     largest=i
print("Largest Num is :",largest)

# By Method

print("max():",max(NUM))

# WAP to find smallest Elemet

#By Method 
print("min():", min(NUM)) 

# By Loop

smallest = NUM[0]

for i in NUM:
   if i<largest:
      smallest = i
print("Smallest Num is :",smallest)

# WAP to Sum all Elements 

print("sum():", sum(NUM))

#By Loop

sum = NUM[0]

for i in NUM:
   sum = i + sum
print("Sum is :",sum)   


