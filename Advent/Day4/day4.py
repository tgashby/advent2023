import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def winningTicketCalculator(ticket):
    score = 0
    for line in ticket:
        cardScore = 0
        cardNum = re.search(r"Card\s+(\d+):", line).group(1)
        if cardNum is not None:
            temp = line.split(":")[1].split("|")
            winningNumbers = [e.strip() for e in temp[0].split(" ") if e.strip().isnumeric()]
            myNumbers = [e.strip() for e in temp[1].split(" ") if e.strip().isnumeric()]
            
            for number in myNumbers:
                if number in winningNumbers:
                    if cardScore == 0:
                        cardScore = 1
                    else:
                        cardScore = cardScore * 2
            
            score += cardScore

    return score

def winningTicketCalculator2(ticket):
    totalCards = 0
    lines = [l.strip() for l in ticket]
    initialTicketLen = len(lines)

    i = 0
    while i < len(lines):
        line = lines[i]
        nextCardIndex = i + 1
        totalCards += 1

        temp = line.split(":")[1].split("|")
        winningNumbers = [e.strip() for e in temp[0].split(" ") if e.strip().isnumeric()]
        myNumbers = [e.strip() for e in temp[1].split(" ") if e.strip().isnumeric()]
        
        for number in myNumbers:
            if number in winningNumbers and i <= initialTicketLen:
                totalCards += 1
                lines.append(lines[nextCardIndex])
                nextCardIndex += 1
        i += 1

    return totalCards



ticket = open(__location__ + '/puzzle.input2', "r")
print(winningTicketCalculator2(ticket))