s=input("enter a string:")

fq={}

for ch in s:
    if ch in fq:
        fq[ch] ++ 1
    else:
        fq[ch] = 1

print("character frequencies:")
print(fq)

