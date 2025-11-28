level = 1
mark = 60
result = "Fail"

if level == 1:
    if mark < 50:
        result = "Fail"
    elif mark >= 50 and mark <= 60:
        result = "Pass"
    elif mark >= 61 and mark <= 70:
        result = "Merit"
    elif mark >= 71 and mark <= 100:
        result = "Distinction"

elif level == 2:
    if mark < 40:
        result = "Fail"
    elif mark >= 40 and mark <= 50:
        result = "Pass"
    elif mark >= 51 and mark <= 65:
        result = "Merit"
    elif mark >= 66 and mark <= 100:
        result = "Distinction"
