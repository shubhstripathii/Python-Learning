num = int(input("Enter a number: "))
ans = 0
for x in range(2,num+1):
    if num%x == 0:
         ans = 1
         break
if(ans):
     print(num, "is not a Prime Number")
else:
     print(num, "is Prime Numer")     
