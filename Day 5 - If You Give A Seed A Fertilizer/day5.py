import os 
#Part 1
with open(os.path.dirname(__file__)+"/data5.txt") as f:
    lines=f.read().splitlines()
    lines=list(filter(None, lines))
    seeds=list(map(int,lines[0].split(" ")[1:]))
    lines=lines[1:]

    maps=[]
    map_i=[]
    for line in lines:
        if line[0] not in list(map(str, range(0,10))):
            maps.append(map_i)
            print(map_i)
            map_i=[]
        else:
            ranges=line.split(" ")
            map_i.append(list(map(int,ranges)))

    maps.append(map_i)
    maps=maps[1:]

    locations=[]
    for seed in seeds:
        for map_i in maps:
            found=False
            j=0
            while j<len(map_i) and not found:
                if map_i[j][1] <= seed < map_i[j][1]+map_i[j][2]:
                    seed=map_i[j][0]+(seed-map_i[j][1])
                    found=True
                else:
                    j+=1
        locations.append(seed)
    print(min(locations))

    def intersect(I1,I2):
        if I2[0]>I1[1] or I1[0]>I2[1]:
            return [-1,-1]
        else:
            return [max(I1[0],I2[0]), min(I1[1],I2[1])]


    #Part 2
"""     seed_ranges=[]
    for i in range(len(seeds)):
        if i%2==0:
            seed_ranges.append([seeds[i],seeds[i]+seeds[i+1]])
    min_results=[]
    for seed_range in seed_ranges:
        transformed_ranges=[]
        j=0
        while j<len(map_i):
            interval_intersect=intersect(seed_range, [map_i[j][1],map_i[j][1]+map_i[j][2]])
            transformed_range=[map_i[j][0]+(interval_intersect[0]-map_i[j][1]),map_i[j][0]+(interval_intersect[1]-map_i[j][1])]
            transformed_ranges.append(transformed_range)
            j+=1

    transformed_ranges=[]
    for map_i in maps:
        for seed_range in seed_ranges:
             """



    