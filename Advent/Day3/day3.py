import os
import numbers

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def engineSchematicDecode(schematic):
    def buildNum(row, initialIndex):
        i = initialIndex
        num = row[i]

        i += 1
        while (i < len(row) and row[i].isnumeric()):
            num += row[i]
            i += 1

        i = initialIndex - 1
        while (i > -1 and row[i].isnumeric()):
            num = row[i] + num
            i -= 1
        return int(num)

    schematicArray = []
    total = 0

    for line in schematic:
        temp = []
        for i in range(len(line)):
            if line[i] != '\n':
                temp.append(line[i])
        schematicArray.append(temp)

    # Part 1
    # for i in range(len(schematicArray)):
    #     currentRow = schematicArray[i];
    #     for j in range(len(currentRow)):
    #         e = currentRow[j]
    #         if e != '.' and not e.isnumeric():
    #             # Check above
    #             if i > 0:
    #                 rowAbove = schematicArray[i - 1];
    #                 if j > 0 and rowAbove[j - 1].isnumeric():
    #                     total += buildNum(rowAbove, j - 1)
    #                 if rowAbove[j].isnumeric() and not rowAbove[j - 1].isnumeric():
    #                     total += buildNum(rowAbove, j)
    #                 if j + 1 < len(rowAbove) and rowAbove[j + 1].isnumeric() and not rowAbove[j].isnumeric():
    #                     total += buildNum(rowAbove, j + 1)
    #             # Check Left and right
    #             if j > 0 and currentRow[j - 1].isnumeric():
    #                 total += buildNum(currentRow, j - 1)
    #             if j + 1 < len(currentRow) and currentRow[j + 1].isnumeric():
    #                 total += buildNum(currentRow, j + 1)
    #             # Check below
    #             if i + 1 < len(schematicArray):
    #                 rowBelow = schematicArray[i + 1]
    #                 if j > 0 and rowBelow[j - 1].isnumeric():
    #                     total += buildNum(rowBelow, j - 1)
    #                 if rowBelow[j].isnumeric() and not rowBelow[j - 1].isnumeric():
    #                     total += buildNum(rowBelow, j)
    #                 if j + 1 < len(rowBelow) and rowBelow[j + 1].isnumeric() and not rowBelow[j].isnumeric():
    #                     total += buildNum(rowBelow, j + 1)
    
    def updateVars(totalNumbers, num1, num2, value):
        totalNumbers[0] += 1

        if totalNumbers[0] < 3:
            if totalNumbers[0] == 1:
                num1[0] = value
            else:
                num2[0] = value

    for i in range(len(schematicArray)):
        currentRow = schematicArray[i];
        for j in range(len(currentRow)):
            e = currentRow[j]
            if e == '*':
                totalNumbers = [0]
                number1 = [0]
                number2 = [1]
                # Check above
                if i > 0:
                    rowAbove = schematicArray[i - 1];
                    if j > 0 and rowAbove[j - 1].isnumeric():
                        updateVars(totalNumbers, number1, number2, buildNum(rowAbove, j - 1))
                    if rowAbove[j].isnumeric() and not rowAbove[j - 1].isnumeric():
                        updateVars(totalNumbers, number1, number2, buildNum(rowAbove, j))
                    if j + 1 < len(rowAbove) and rowAbove[j + 1].isnumeric() and not rowAbove[j].isnumeric():
                        updateVars(totalNumbers, number1, number2, buildNum(rowAbove, j + 1))
                # Check Left and right
                if j > 0 and currentRow[j - 1].isnumeric():
                    updateVars(totalNumbers, number1, number2, buildNum(currentRow, j - 1))
                if j + 1 < len(currentRow) and currentRow[j + 1].isnumeric():
                    updateVars(totalNumbers, number1, number2, buildNum(currentRow, j + 1))
                # Check below
                if i + 1 < len(schematicArray):
                    rowBelow = schematicArray[i + 1]
                    if j > 0 and rowBelow[j - 1].isnumeric():
                        updateVars(totalNumbers, number1, number2, buildNum(rowBelow, j - 1))
                    if rowBelow[j].isnumeric() and not rowBelow[j - 1].isnumeric():
                        updateVars(totalNumbers, number1, number2, buildNum(rowBelow, j))
                    if j + 1 < len(rowBelow) and rowBelow[j + 1].isnumeric() and not rowBelow[j].isnumeric():
                        updateVars(totalNumbers, number1, number2, buildNum(rowBelow, j + 1))
                if totalNumbers[0] == 2:
                    total += number1[0] * number2[0]

    return total

schematic = open(__location__ + '/puzzle.input', "r")
print(engineSchematicDecode(schematic))