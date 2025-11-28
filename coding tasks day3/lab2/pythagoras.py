from math import sqrt

print("Pythagoras Calculator")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

option = 1

while True:
    try:
        option = int(input("Select number 1-3: "))
        break
    except:
        print("Error code III: invalid input idiot")

# C^2 = A^2 + B^2
# A^2 = C^2 - B^2
# B^2 = C^2 - A^2

result = 0
if option == 1:
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    result = sqrt(c**2 - b**2)
elif option == 2:
    a = float(input("Enter a: "))
    c = float(input("Enter c: "))
    result = sqrt(c**2 - a**2)
elif option == 3:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    result = sqrt(a**2 + b**2)

print(f"result: {result}")
