def cheack_armstrong(n):
    n=str(n)
    len_n=len(n)
    s=0
    for i in range(len_n):
        s=s+int(n[i])**len_n
    return int(n)==s

for i in range(1000000):
    if cheack_armstrong(i):
        print(i)
