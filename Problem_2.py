
n=int(input("Enter the 5 digit number: "))

a=(n//10000)
b=(n//1000)%10
c=(n//100)%10
d=(n//10)%10
e=n%10

s=a+b+c+d+e
p=a*b*c*d*e
rev=e*10000+d*1000+c*100+b*10+a

print("First Digit:", a)
print("Second Digit:", b)
print("Third Digit:", c)
print("Fourth Digit:", d)
print("Fifth Digit:", e)
print("Sum:", s)
print("Product:", p)
print("Reversed Number:", rev)
print("Difference:", n-rev)
print("Middle Digit:", c)