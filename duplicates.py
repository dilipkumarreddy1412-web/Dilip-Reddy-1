def remove_Duplicates(n):
    res=[]
    for i in n:
        if i not in res:
            res.append(i)
    return res
print("input comma separeated number:")
inp=list(map(int,input().split(",")))
print(remove_Duplicates(inp))
