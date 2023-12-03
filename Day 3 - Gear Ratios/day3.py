import os
from collections import Counter

def is_valid(l,c):
    if  0 <= l < 140 and 0 <= c < 140:
        return True
    else:
        return False
    
#Part 1

def adjacent_positions(matrix, num_list):
    found=False
    i=0
    while not found and i<len(num_list):
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if not x==y==0 and is_valid(num_list[i][0][0]+x, num_list[i][0][1]+y):
                    if matrix[num_list[i][0][0]+x][num_list[i][0][1]+y] not in list(map(lambda x: str(x), range(0,10))) + ["."]:
                        found=True
                        break
            if found:
                break
        i+=1
    if found:
        number=""
        for num in num_list:
            number += num[1]
        number=int(number)
        return number
    else:
        return -1

with open(os.path.dirname(__file__)+"/data3.txt") as f:
    matrix=f.read().splitlines()
    nums=[]
    visited=[]
    for l_idx, line in enumerate(matrix):
        for c_idx, char in enumerate(line):
            idxs=[]
            if char in list(map(lambda x: str(x), range(0,10))) and (l_idx, c_idx) not in visited:
                next=c_idx
                while  is_valid(l_idx,next) and line[next] in list(map(lambda x: str(x), range(0,10))):
                    idxs.append([(l_idx, next), line[next]])
                    next+=1
                number=adjacent_positions(matrix,idxs)
                if number!=-1:
                    nums.append(number)
            visited+=list(map(lambda x: x[0], idxs))
    print(sum(nums))

#Part 2    

def adjacent_positions_2(matrix, num_list):
    found=False
    i=0
    while not found and i<len(num_list):
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if not x==y==0 and is_valid(num_list[i][0][0]+x, num_list[i][0][1]+y):
                    if matrix[num_list[i][0][0]+x][num_list[i][0][1]+y] == "*":
                        gear_pos=(num_list[i][0][0]+x,num_list[i][0][1]+y)
                        found=True
                        break
            if found:
                break
        i+=1
    if found:
        number=""
        for num in num_list:
            number += num[1]
        number=int(number)
        return number, gear_pos
    else:
        return -1, (-1,-1)

with open(os.path.dirname(__file__)+"/data3.txt") as f:
    matrix=f.read().splitlines()
    nums=[]
    visited=[]
    gear_total_pos=[]
    for l_idx, line in enumerate(matrix):
        for c_idx, char in enumerate(line):
            idxs=[]
            if char in list(map(lambda x: str(x), range(0,10))) and (l_idx, c_idx) not in visited:
                next=c_idx
                while  is_valid(l_idx,next) and line[next] in list(map(lambda x: str(x), range(0,10))):
                    idxs.append([(l_idx, next), line[next]])
                    next+=1
                number, gear_pos=adjacent_positions_2(matrix,idxs)
                if number!=-1:
                    nums.append((number, gear_pos))
                    gear_total_pos.append(gear_pos)
            visited+=list(map(lambda x: x[0], idxs))

    gear_total_pos2=[]
    for gear in Counter(gear_total_pos).items():
        if gear[1]==2:
            gear_total_pos2.append(gear[0])

    gear_ratios=[]
    visited=[]
    for num1 in nums:
        for num2 in nums:
            if num2[1]==num1[1] and num1!=num2 and num1 not in visited and num2 not in visited:
                gear_ratios.append(num1[0]*num2[0])
                visited+=[num1,num2]
                break
    print(gear_ratios)
    print(sum(gear_ratios))


        
