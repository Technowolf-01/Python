num = int(input("Enter the number\n"))
flag=0
m=0
m=num//2
for i in range(2,m):
    if(num%i==0):
        print("Not a prime number")
        flag=1
        break

if(flag==0):
    print("Prime number")
