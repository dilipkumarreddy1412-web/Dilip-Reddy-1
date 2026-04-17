Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
map
<class 'map'>
a=lambda x,y:x+y
a(10,20)
30
f=lambda a,b:3*a**2+5*b+11
f(2,3)
38
f(10,20)
411
a(10,30)
40
f(10,20)
411
g=lambda a,b:3*a**2-5*b-11
g
<function <lambda> at 0x0000019771E0E340>
g(10,20)
189
g=lambda a,b:3*a**2*5*b*11
g(2,3)
1980
g=lambda a,b:3*a**2-5*b-11
h=lambda a,b:3*a**2*5*b*11
h(3,3)
4455
a=(2,2)
a=lambda x,y:x+yf=lambda a,b:3*a**2+5*b+11g=lambda a,b:3*a**2-5*b-11g=lambda a,b:3*a**2*5*b*11
SyntaxError: invalid decimal literal
a=lambda x,y:x+y
f=lambda a,b:3*a**2+5*b+11
g=lambda a,b:3*a**2-5*b-11
g=lambda a,b:3*a**2*5*b*11
h=lambda a,b:3*a**2*5*b*11
a(2,2)
4
f(2,2)
33
g(2,2)
1320
h(2,2)
1320
w=[2,1,0,7,9,4,3,2,1]
#[2,1,0,7,9,4,3,2,1]
map(lambda a:pow(a,2),w)
<map object at 0x0000019771E04D90>
for i in map(lambda a:pow(a,2),w):print(i)

4
1
0
49
81
16
9
4
1
list(map(lambda a:pow(a,2),w))
[4, 1, 0, 49, 81, 16, 9, 4, 1]
def square(a):return a**2

square(10)
100
r=list(map(lambda a:round(a**(1/3),2),w))
r
[1.26, 1.0, 0.0, 1.91, 2.08, 1.59, 1.44, 1.26, 1.0]

input()
venky,likhith,prasad
'venky,likhith,prasad'
input().split(",")
apple,gua,man,papaya
['apple', 'gua', 'man', 'papaya']
'apple,gua,man,papaya '.split('.')
['apple,gua,man,papaya ']
'3,3,2,1,4,'.split(',')
['3', '3', '2', '1', '4', '']
print(list(map(len,input().split(','))))
apple,gua,mango,papaya
[5, 3, 5, 6]
print(*list(map(len,input().split(','))))
apple,gua,mango,papaya
5 3 5 6
n=['5','2','4','7']
w=[2,1,0,7,9,4,3,2,1]
map(lambda a:pow(a,2),w)
<map object at 0x0000019771E050F0>
for i in map(lambda a:pow(a,2),w):print(i)


list(map(lambda a:pow(a,2),w))
[4, 1, 0, 49, 81, 16, 9, 4, 1]
def square(a):return a**2

list(map(lambda a:pow(a,2),w))
[4, 1, 0, 49, 81, 16, 9, 4, 1]
def square(a):return a**2

list(map(a,w))

w=[2,1,0,7,9,4,3,2,1]def square(a):return a**2
SyntaxError: invalid syntax
def square(a):return a**2

square(200)
40000
w=[2,1,0,7,9,4,3,2,1]
map(lambda a:pow(a,2),w)
<map object at 0x0000019771E058A0>
for i in map(lambda a:pow(a,2),w):print(i)

4
1
0
49
81
16
9
4
1
list(map(lambda a:pow(a,2),w))
[4, 1, 0, 49, 81, 16, 9, 4, 1]
def square(a):return a**2

square(10)
100
map(lambda a:pow(a,2),w)
<map object at 0x0000019771E04B50>
list(map(square,w))
[4, 1, 0, 49, 81, 16, 9, 4, 1]
def sr(x):return x**0.5

sr(9)
3.0
w
[2, 1, 0, 7, 9, 4, 3, 2, 1]
r=list(map(sr,w))
r
[1.4142135623730951, 1.0, 0.0, 2.6457513110645907, 3.0, 2.0, 1.7320508075688772, 1.4142135623730951, 1.0]
def sr(x):return round(x**0.5,2)

sr(9)
3.0
r=list(map(sr,w))
>>> r
[1.41, 1.0, 0.0, 2.65, 3.0, 2.0, 1.73, 1.41, 1.0]
>>> w
[2, 1, 0, 7, 9, 4, 3, 2, 1]
>>> r=list(map(lambda a:round(a**(1/3),2),w))
>>> r
[1.26, 1.0, 0.0, 1.91, 2.08, 1.59, 1.44, 1.26, 1.0]
>>> input()
apple,gua,papaya,man
'apple,gua,papaya,man'
>>> 
>>> input().split(',')
apple,gua,papaya,man
['apple', 'gua', 'papaya', 'man']
>>> 'apple,gua,papaya,man'.split(',')
['apple', 'gua', 'papaya', 'man']
>>> '2,3,4,5,6'.split(',')
['2', '3', '4', '5', '6']
>>> print(list(map(len,input().split(","))))
apple,gua,papaya,man
[5, 3, 6, 3]
>>> print(*list(map(len,input().split(","))))
apple,gua,papaya,man
5 3 6 3
>>> n=['5','2','4','7']
>>> list(map(int,n))
[5, 2, 4, 7]
>>> list(map(int,input().split(',')))
5,3,6,3
[5, 3, 6, 3]
>>> sum(list(map(int,input().split(','))))
5,3,6,3
17
>>> print(sum(list(map(int,input().split(',')))))
5,3,6,3
17
