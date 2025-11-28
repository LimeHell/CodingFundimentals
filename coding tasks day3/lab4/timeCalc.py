def mainMenu():
    while True:
        print("Time Calculator")
        print("1 - Add 2 times")
        print("2 - Find the difference between 2 times")
        print("3 - Convert to Hours")
        print("4 - Convert to Minutes")
        print("5 - Convert Minutes to Time")
        print("6 - Convert Hours to Time")
        print("7 - Convert Days to Time")
        print("8 - Exit")
        try:
            selection = int(input("Enter an option:"))

            if selection == 1:
                time1, time2 = twoTimeInputs()
                timeDict = addTimes(time1, time2)
                printTimeDict(timeDict)

            elif selection == 2:
                time1, time2 = twoTimeInputs()
                timeDict = calculateDifference(time1, time2)
                printTimeDict(timeDict)

            elif selection == 3:
                time = getTimeInput("Enter time (DD:HH:MM): ")
                hours = convertToHours(time)
                print(hours)

            elif selection == 4:
                time = getTimeInput("Enter time (DD:HH:MM): ")
                minutes = convertToMinutes(time)
                print(minutes)

            elif selection == 5:
                minutes = getIntInput("Enter minutes: ")
                timeDict = {"days": 0, "hours": 0, "minutes": minutes}
                timeDict = cleanUpTimeDict(timeDict)
                printTimeDict(timeDict)

            elif selection == 6:
                hours = getIntInput("Enter hours: ")
                timeDict = {"days": 0, "hours": hours, "minutes": 0}
                timeDict = cleanUpTimeDict(timeDict)
                printTimeDict(timeDict)

            elif selection == 7:
                days = getIntInput("Enter days: ")
                print("sss", days)
                timeDict = {"days": days, "hours": 0, "minutes": 0}
                print(timeDict)
                timeDict = cleanUpTimeDict(timeDict)
                printTimeDict(timeDict)

            elif selection == 8:
                break

            else:
                print("That is not one of the options, try again")
                continue

        except:
            print("Invalid selection")
            continue


def printTimeDict(timeDict):
    print(
        f"{timeDict['days']} days, {timeDict['hours']} hours and {timeDict['minutes']} minutes"
    )


def getIntInput(message):
    num = 0

    while True:
        try:
            num = int(input(message))
            break
        except:
            print("Try again")
            continue

    return num


def cleanUpTimeDict(timeDict):
    daysOG = timeDict["days"]
    hoursOG = timeDict["hours"]
    minutesOG = timeDict["minutes"]

    hoursToAdd = minutesOG // 60
    minutes = minutesOG % 60

    hoursOG += hoursToAdd

    daysToAdd = hoursOG // 24
    hours = hoursOG % 24

    days = daysOG + daysToAdd

    return {"days": days, "hours": hours, "minutes": minutes}


def getTimeInput(message):
    timeDict = None
    while timeDict == None:
        time = input(message)
        try:
            split = time.split(":")
            if len(split) != 3:
                raise Exception

            nums = [int(string) for string in split]

            timeDict = {"days": nums[0], "hours": nums[1], "minutes": nums[2]}
            break

        except:
            print("Invalid input. Must be in format DD:HH:MM")
            continue

    return cleanUpTimeDict(timeDict)


def twoTimeInputs():
    time1 = getTimeInput("Enter first time (DD:HH:MM): ")
    time2 = getTimeInput("Enter second time (DD:HH:MM): ")

    return time1, time2


def addTimes(time1, time2):
    combinedTime = {
        "days": time1["days"] + time2["days"],
        "hours": time1["hours"] + time2["hours"],
        "minutes": time1["minutes"] + time2["minutes"],
    }

    return cleanUpTimeDict(combinedTime)


def calculateDifference(time1, time2):
    combinedTime = {
        "days": time1["days"] - time2["days"],
        "hours": time1["hours"] - time2["hours"],
        "minutes": time1["minutes"] - time2["minutes"],
    }

    return cleanUpTimeDict(combinedTime)


def convertToHours(time):
    dayHours = time["days"] * 24
    minuteHours = time["minutes"] / 60

    return dayHours + minuteHours + time["hours"]


def convertToMinutes(time):
    dayMinutes = time["days"] * 24 * 60
    hourMinutes = time["hours"] * 60

    return dayMinutes + hourMinutes + time["minutes"]


mainMenu()
