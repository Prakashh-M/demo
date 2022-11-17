
a= int(input())
s=0

while (a>0):
    d= a%10
    s= (s*10)+d
    a=a//10
    if s==a:
        print("it is a palindrome")
    else:
        print("No it isn't")