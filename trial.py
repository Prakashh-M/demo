
a= int(input())
<<<<<<< HEAD
s=10
=======
s=15
>>>>>>> a5e214b0c03c4ff7182fa1a6985c99cb14f00eb5

while (a>0):
    d= a%10
    s= (s*10)+d
    a=a//10
    if s==a:
        print("it is a palindrome")
    else:
        print("No it isn't")
