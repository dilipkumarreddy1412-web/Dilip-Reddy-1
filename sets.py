#unique elemnts from a list using a set
first=[1,2,2,3,4,4,5]
unique=set(first)
print("unique elemnts:",unique)

#add an elemnt in set
s={1,2,3}
s.add(4)
print("update set:",s)

#remove an element in a set
s={1,2,3,4}
s.remove(3)
print("after removing:",s)

#cheack if an element exists in a set
s={10,20,30}
if 10 in s:
    print("element found")
else:
    print("element not found")

#symmetric difference of two sets
set1={1,2,3}
set2={3,4,5}
print("symmetric difference:",set1^set2)

#create an empty set and add an elements
s=set()
s.add(10)
s.add(20)
s.add(30)
print(s)

#find yhe length of the set
s={1,2,3,4,5}
print("length of set:",len(s))

#remove all elements to the set
s={1,2,3}
s.clear()
print("set after clearing:",s)

#cheack weather two elements are equal
set1={1,2,3}
set2={3,2,1}
print("sets are equal:",set1==set2)

#convert a string into a set of characters
s="hello"
char_set=set(s)
print("set of character :",char_set)


