a=list()
b=[]
c=list('apple')
d=[10,20.9,'apple','c']
type(a)

type(b)

type(c)

type(d)

e=list([10,20,30])
e

f=list((10,20,30))
f

temp=[10,20,30,40,]
print(temp)

temp.append(50)
print(temp)

temp.append(6.1)
print(temp)

temp.append([60,70,80])
print(temp)

temp[0]

temp[1]

temp[2]

print(temp)

temp.clear()
print(temp)

a=[10, 20, 30, 40, 50, 6.1, [60, 70, 80]]
a[6]

a[6][0]

a[6][1]

del a[-1]

b=a
b

id(a)

id(b)

b.append('likith')
b

c=a.copy()
id(c)

del a[-1]
a

a.append(89)
a.append(89)
a.append('cr')
a

print(a)

a.count('cr')

a.count('mca')

d=[10,20,30]
d.extend(['gua','papaya'])
d

d.extend(['crt'])
d

d.extend('class')
d

d.insert(3,'game')
d

d.insert(-1,'MCA')
d

x=d.pop()
x

d

x=d.pop(3)
x

x=d.remove('papaya')

d

x=d.remove('gua')
d

x=d.remove('crt')
d

d.reverse()
d

x=a.reverse()
a

c=[10, 20, 30, 40, 50]
c

c.sort(reverse=True)
c

cs=input()

cs

a=list(cs)
a

a.sort()
a

"".join(a)

"#".join(a)

' '.join(a)

'   '.join(a)

data=[['likith',30,20],['venky',50,40],['prasad',70,60]]
data

data.sort(key=lambda x:x[1])
data

data.sort(key=lambda x:x[2])
data

data.sort(key=lambda x:x[1],reverse=True)
data

data.sort(key=lambda x:(x[2]+x[2])/2)
data

student={"alice":10, "bob":20, "charlic":30, "david":40}
student.keys()

student.values()

student.items()

a=[10,20,30,40,50]
res=[]
for i in a:
    res.append(i/2)

 res

 
x=[10,20,30,40,50]
y=[1,2,3,4,5]
res=[]
for i,j in zip(x,y):
    res.append(i+j)

res

for i,j in zip(x,y):
               print("i=",i,"j=",j)

[i+j for i,j in zip(x,y)]

  
