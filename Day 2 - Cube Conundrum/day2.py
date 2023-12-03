import os
import math

cubes=[(12, "red"), (13, "green"), (14, "blue")]
cubes={
    "red":12,
    "green": 13,
    "blue":14
}

#Part 1
with open(os.path.dirname(__file__)+"/data2.txt") as f:
    lines=f.readlines()
    impossible_idx=[]
    for line in lines:
        line=line=line[:-1]
        clean_line=line.split(": ")
        idx=int(clean_line[0].split("Game ")[1])
        cubes_shown=clean_line[1].split("; ")
        for tries in cubes_shown:
            cubes_color=tries.split(", ")
            for cube_color in cubes_color:
                cube_color=cube_color.split(" ")
                if int(cube_color[0])>cubes[cube_color[1]]:
                    impossible_idx.append(idx)
    print(sum(range(1,101))-sum(set(impossible_idx)))

#Part 2    
with open(os.path.dirname(__file__)+"/data2.txt") as f:
    lines=f.readlines()
    powers=[]
    for line in lines:
        line=line=line[:-1]
        clean_line=line.split(": ")
        cubes_shown=clean_line[1].split("; ")
        min_cubes={"red":0, "green": 0, "blue":0}
        for tries in cubes_shown:
            cubes_color=tries.split(", ")
            for cube_color in cubes_color:
                cube_color=cube_color.split(" ")
                if int(cube_color[0])>min_cubes[cube_color[1]]:
                    min_cubes[cube_color[1]]=int(cube_color[0])
        powers.append(math.prod(min_cubes.values()))
    print(sum(powers))        