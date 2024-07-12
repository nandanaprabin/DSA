n=int(input("Enter a number: "))
sum=0
temp=n
while(n>0):
    d=int(n%10)
    sum=(sum*10)+d
    n=int(n/10)
if(sum==temp):
    print(temp,"is a palindrome")
else:
    print(temp,"is not a palindrome")