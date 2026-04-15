#hard method

string = (input("enter a string:"))
char = (input("enter a character:"))

count = 0
for c in string:
    if c == char:
        count += 1
        
print("frequency of '{character}' is:",count)

#simple method

a=input("Enter a string:")
char=input("enter a character:")

print("frequency:",a.count(char))

--------------------------------------------------------
#other method

string = (input("enter a string:"))

frequency={}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("character frequencies:")
print(frequency)
        
