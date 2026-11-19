a = input("Input 1: ")
b = input("Input 2: ")
c = input("Input 3: ")

print("Original Types:")
print(type(a), type(b), type(c))

x = int(a)
y = float(b)
z = str(c)

print("Converted Values:", x, y, z)
print("Converted Types:", type(x), type(y), type(z))

n = int(c)

s = x + y + n
avg = s / 3

print("Sum:", s)
print("Average:", avg)
print("Maximum:", max(x, y, n))
print("Minimum:", min(x, y, n))
print("Square of First:", x ** 2)
print("Cube of Third:", n ** 3)

print("First > Second:", x > y)
print("Sum divisible by 5:", s % 5 == 0)
print("Average between 10 and 100:", 10 <= avg <= 100)
print("All Positive:", x > 0 and y > 0 and n > 0)