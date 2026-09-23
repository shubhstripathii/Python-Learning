#WAP to count even and odd numbers from list 

NUM = [0,1,2,3,4,5,6,7,8,9]


even = []
odd = []

for i in NUM:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even_count = len(even)
odd_count = len(odd)
num_count = len(NUM)

print("Even numbers:", even)
print("Even count:", even_count)

print("Odd numbers:", odd)
print("Odd count:", odd_count)
print("Odd count:", num_count)