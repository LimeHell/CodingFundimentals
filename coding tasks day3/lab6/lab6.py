"""
Band 	Taxable income 	Tax rate
Personal Allowance 	Up to £12,570 	0%
Basic rate 	£12,571 to £50,270 	20%
Higher rate 	£50,271 to £125,140 	40%
Additional rate 	over £125,140 	45%
"""

# p.s. i dont know if this is accurate or not but it seems fine idrk i havent tested much - love josh


def getIncomeTax(income):
    takeHomePay = 0

    personalAllowanceMoney = min(income, 12570)
    takeHomePay += personalAllowanceMoney

    remaining = income - 12570

    if remaining <= 0:
        return takeHomePay

    basicRateMoney = min(remaining, 50270 - 12571)
    takeHomePay += basicRateMoney * 0.8

    remaining -= 50270 - 12571

    if remaining <= 0:
        return takeHomePay

    higherRateMoney = min(remaining, 125140 - 50271)
    takeHomePay += higherRateMoney * 0.6

    remaining -= 125140 - 50271

    if remaining <= 0:
        return takeHomePay

    additionalRateMoney = remaining

    takeHomePay += additionalRateMoney * 0.55

    return takeHomePay


inp = int(input("Enter money: "))
print(getIncomeTax(inp))
