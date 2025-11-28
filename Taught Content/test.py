print("hello world!") 

y = 10
x = y
y = 15

print(x)

# common numbers are loaded to memory 
x = 256 # or any number between -256 and 256
y = 256

print(id(x))
print(id(y))

x = 257123
y = 2571

print(id(x))
print(id(y))

