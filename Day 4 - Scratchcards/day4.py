import os 
from collections import Counter

with open(os.path.dirname(__file__)+"/data4.txt") as f:
    #Part 1
    lines=f.read().splitlines()
    matches=[]
    for line in lines:
        line=line.split(": ")[1]
        line=line.split(" | ")

        winning_numbers=line[0].split(" ")
        winning_numbers=list(filter(None, winning_numbers))

        numbers_obtained=line[1].split(" ")
        numbers_obtained=list(filter(None, numbers_obtained))

        counts=Counter(winning_numbers+numbers_obtained)
        card_matches=len(list(filter(lambda x: x>=2,counts.values())))
        matches.append(card_matches)
    points=list(map(lambda x: 0 if x==0 else 2**(x-1), matches))
    print(sum(points))

    #Part 2
    cards=[1 for line in lines]
    i=0
    while i<len(cards):
        for card in range(cards[i]):
            for match in range(matches[i]):
                if i+match+1<len(cards):
                    cards[i+match+1]+=1
        i+=1
    print(sum(cards))

