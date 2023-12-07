import os
from collections import Counter

#Part 1

cards=["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
rewards=[[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]]
ranks_per_reward=[[],[],[],[],[],[],[]]
with open(os.path.dirname(__file__)+"/data7.txt") as f:
    lines=f.read().splitlines()
    ranks=[]
    for line in lines:
        hand,bet=line.split(" ")
        hand=[*hand]
        reward_idx=rewards.index(sorted(list(Counter(hand).values()), reverse=True))

        if ranks_per_reward[reward_idx]==[]:
            ranks_per_reward[reward_idx].append([hand,int(bet)])
        else:
            for idx,ranked_hand in enumerate(ranks_per_reward[reward_idx]):
                found=False
                i=0
                while not found and i<len(ranked_hand[0]):
                    if cards.index(hand[i]) < cards.index(ranked_hand[0][i]):
                        ranks_per_reward[reward_idx].insert(idx, [hand,int(bet)])
                        found=True
                    elif cards.index(hand[i]) > cards.index(ranked_hand[0][i]):
                        break
                    i+=1
                if found:
                    break

            if not found:
                ranks_per_reward[reward_idx].append([hand, int(bet)])

    ranks=[hand for row in ranks_per_reward for hand in row]
    prize=0
    for idx, hand in enumerate(ranks):
        prize+=(len(lines)-idx)*hand[1]

    print(prize)

#Part 2
cards=["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
rewards=[[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]]
ranks_per_reward=[[],[],[],[],[],[],[]]
with open(os.path.dirname(__file__)+"/data7.txt") as f:
    lines=f.read().splitlines()
    ranks=[]
    for line in lines:
        hand,bet=line.split(" ")
        hand=[*hand]
        counter=Counter(hand)
        J_number=counter["J"]
        if J_number>0:
            if counter!=Counter(["J"]*5):
                counter.pop("J")
                max_n=max(counter, key=counter.get)
                counter[max_n]+=J_number
                counter["J"]=0
            
        
        reward_type=list(counter.values())
        if 0 in reward_type:
            reward_type.remove(0)
        reward_idx=rewards.index(sorted(reward_type, reverse=True))

        if ranks_per_reward[reward_idx]==[]:
            ranks_per_reward[reward_idx].append([hand,int(bet)])
        else:
            for idx,ranked_hand in enumerate(ranks_per_reward[reward_idx]):
                found=False
                i=0
                while not found and i<len(ranked_hand[0]):
                    if cards.index(hand[i]) < cards.index(ranked_hand[0][i]):
                        ranks_per_reward[reward_idx].insert(idx, [hand,int(bet)])
                        found=True
                    elif cards.index(hand[i]) > cards.index(ranked_hand[0][i]):
                        break
                    i+=1
                if found:
                    break

            if not found:
                ranks_per_reward[reward_idx].append([hand, int(bet)])

    ranks=[hand for row in ranks_per_reward for hand in row]
    prize=0
    for idx, hand in enumerate(ranks):
        prize+=(len(lines)-idx)*hand[1]

    print(prize)