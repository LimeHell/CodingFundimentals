kgsToLbsConversion = 2.205

validWeightGiven = False

while not validWeightGiven:
    try:
        print("Enter the amount of weight to convert: ")
        weight = float(input())
        validWeightGiven = True
    except:
        print("That was an invalid input, try again")

validUnitGiven = False

while not validUnitGiven:
    print("What is the unit of weight you entered? kgs or lbs")
    unit = input().lower()

    if unit == "kgs":
        validUnitGiven = True
        print("Converting from kgs to lbs...")
        newWeight = weight * kgsToLbsConversion
        print(f"{newWeight:.2f}lbs is your converted weight!")

    elif unit == "lbs":
        validUnitGiven = True
        print("Converting from lbs to kgs...")
        newWeight = weight / kgsToLbsConversion
        print(f"{newWeight:.2f}kg is your converted weight!")

    else:
        # Repeats the loop
        print("You entered an invalid unit of weight")
        continue