from functools import reduce

numbers=list(map(int,input().split(',')))

total_sum=reduce(lambda x,y:x+y,numbers)

print("sum of the list:",total_sum)
