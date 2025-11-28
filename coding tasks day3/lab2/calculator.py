while True:
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        break
    except:
        print("That is not a number, idiot.")
        continue

while True:

    print("+ Add\n- Subtract\n* Multiply\n/ Divide\ns Square")
    op = input()
    if op == "+":
        print(n1 + n2)
    elif op == "-":
        print(n1 - n2)
    elif op == "*":
        print(n1 * n2)
    elif op == "/":
        print(n1 / n2)
    elif op == "s":
        print(n1**n2)
    else:
        continue
    break
