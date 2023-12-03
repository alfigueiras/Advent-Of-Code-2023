import os

with open(os.path.dirname(__file__)+"/data1.txt") as f:
    lines=f.readlines()
    numbers=list(map(lambda x: str(x), range(1,10))) + ["one", "two", "three", "four" , "five", "six", "seven", "eight", "nine"]
    numbers_int=list(map(lambda x: str(x), range(1,10)))*2
    calibrations=[]
    for line in lines:
        firstIdx=[len(line), 0]
        lastIdx=[-1,0]
        for num in numbers:
            fidx=line.find(num)
            lidx=line.rfind(num)
            if fidx!=-1 and fidx<firstIdx[0]:
                firstIdx[0]=fidx
                firstIdx[1]=num
            if lidx!=-1 and lidx>lastIdx[0]:
                lastIdx[0]=lidx
                lastIdx[1]=num
        fn_idx=numbers.index(firstIdx[1])
        ln_idx=numbers.index(lastIdx[1])
        calibrations.append(int(numbers_int[fn_idx]+numbers_int[ln_idx]))
    print(sum(calibrations))
        