num = int(input("enter the number\n"))
rev=0
temp2=num
while(num>0):
    temp=num%10
    rev=(rev*10)+temp
    num = num//10

if(rev==temp2):
    print("palindrome")
else:
    print("Not a Palindrome")