def processInstruction(currentRowIndex, currentColIndex, nextTwoInstructionsStr):
    keypad = [[0], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    try:
        instructions = nextTwoInstructionsStr
        # Get the current instruction step
        firstStep = instructions[0]

        rowIndex = currentRowIndex
        colIndex = currentColIndex

        # Change the row or col indexes appropriately
        if firstStep == "↓":
            rowIndex -= 1
        elif firstStep == "↑":
            rowIndex += 1
        elif firstStep == "→":
            colIndex += 1
        elif firstStep == "←":
            colIndex -= 1
            
        # If * instruction, get the number of times to repeat the Num, and create a list of that many nums
        elif firstStep == "*" and len(instructions) == 2:
            secondStep = instructions[1]
            num = keypad[rowIndex][colIndex]
            numTimesToRepeat = int(secondStep)
            returnVal = [num for i in range(numTimesToRepeat-1)]
            return {'rowIndex': rowIndex, 'colIndex': colIndex, 'data': returnVal}

        # If we go out of bounds, return None, which will make the program return []
        if rowIndex < 0 or colIndex < 0:
            return None
        num = keypad[rowIndex][colIndex]
        returnVal = [num]
        
        # Return the updated indexes too so the outer code can continue where we left off        
        return {'rowIndex': rowIndex, 'colIndex': colIndex, 'data': returnVal}
    except Exception as e:
        (e)
        return None
    
def dec_arrow_pin_code(arrow_str):
    # Key pad
    keypad = [[0], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Turn each character into a list
    instructions = list(arrow_str)
    
    startNum = instructions[0]
    
    # Use indexes to track where we are currently looking
    currentRowIndex = 0
    currentColIndex = 0
    
    # This flag indicates that we have a valid number as the start point and not an arrow or anything else
    validStartNum = False
    
    # Get the start coordinates
    try:
        for r in range(len(keypad)):
            row = keypad[r]
            for c in range(len(row)):
                cell = row[c]
                print(cell, startNum)
                if str(cell) == startNum:
                    # If the cell is the same as the startNum, select these row/col values
                    currentRowIndex = r
                    currentColIndex = c
                    validStartNum = True
                    break
            if validStartNum == True:
                break
        if validStartNum == False:
            raise Exception;
    except:
        # If invalid startNum, return empty []
        return []
    
    # Start our PIN Code    
    codeSoFar = [int(startNum)]
    
    # Remove the startNum so we can programatically process rest of instructions
    instructions.pop(0)
    
    for i in range(len(instructions)):
        isLastElement = i == len(instructions) - 1
        
        # Instr string contains the next 2 instructions, or just the next 1 if its the last one.
        instr = ""
        if isLastElement:
            instr = instructions[i]
        else:
            instr = instructions[i:i+2]
        
        # store helper function results
        info = processInstruction(currentRowIndex, currentColIndex, instr)
        if info == None:
            return []
        
        for num in info['data']:
            codeSoFar.append(num)
        
        currentRowIndex = info['rowIndex']
        currentColIndex = info['colIndex']
                
    
    return codeSoFar