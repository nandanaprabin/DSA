def is_prime(number):
    if number<=1:
        return False
    if number==2:
        return True
    if number%2==0:
        return False
    for i in range(3,int(number**0.5)+1,2):
        if number%i==0:
            return False
    return True
num=int(input("Enter the number: "))
if is_prime(num):
    print(num,"is prime")
else:
    print(num,"is not prime")