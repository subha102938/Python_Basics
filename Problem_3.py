a = 10
b = 20
c = 30

a=a+b
b=a-b
a=a-b


b, c=c, b

d=a+b+c
e=d/3

print("a =", a, type(a))
print("b =", b, type(b))
print("c =", c, type(c))
print("Sum =", d)
print("Average =", e)
print(d > e * 2)