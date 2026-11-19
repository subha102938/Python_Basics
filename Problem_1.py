p1=int(input("Price 1: "))
q1=int(input("Quantity 1: "))

p2=int(input("Price 2: "))
q2=int(input("Quantity 2: "))

p3=int(input("Price 3: "))
q3=int(input("Quantity 3: "))

dis=float(input("Discount: "))
gst=float(input("GST: "))

t1=p1*q1
t2=p2*q2
t3=p3*q3

sub=t1+t2+t3
d=sub*dis/100
amt=sub-d
g=amt*gst/100
final=amt+g

print("Product 1 Total:", t1)
print("Product 2 Total:", t2)
print("Product 3 Total:", t3)
print("Subtotal:", sub)
print("Discount:", d)
print("After Discount:", amt)
print("GST:", g)
print("Final Amount:", final)