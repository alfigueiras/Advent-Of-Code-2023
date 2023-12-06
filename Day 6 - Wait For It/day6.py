from math import prod,sqrt,floor

time=[48,93,85,95]
distance=[296,1928,1236,1391]

solutions=[]
for idx,t in enumerate(time):
    solutions_t=0 
    for velocity in range(t):
        if velocity*(t-velocity)>distance[idx]:
            solutions_t+=1
    solutions.append(solutions_t)

print(prod(solutions))

#Part 2
time=int("".join(list(map(str, time))))
distance=int("".join(list(map(str, distance))))

poly_solutions=[(time-sqrt(time**2-4*distance))/2,(time+sqrt(time**2-4*distance))/2]

print(floor(poly_solutions[1])-floor(poly_solutions[0]))
