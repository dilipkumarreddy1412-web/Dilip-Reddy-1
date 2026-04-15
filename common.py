#common elemnts in two sets
set1={1,2,3,4,5,6,7,8,9,}
set2={3,4,5,6,7,8,9,10}
common=set1&set2
print("common elements:",common)

#find union of two sets
set1={1,2,3,4}
set2={3,4,5,6}
print("union:",set1|set2)

#difference between two sets
#elements in set1 but not in set2
set1={1,2,3,4}
set2={3,4}
print("difference:",set1-set2)

#cheack if a set is a sub set of another set
set1={1,2}
set2={1,2,3,4}
print("Is a subset(true or false):",set1.issubset(set2))
