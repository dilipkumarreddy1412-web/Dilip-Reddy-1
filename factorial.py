class B:
    def fact(self,n):
        if n==0:
            return 1
        else:
            return n*self.fact(n-1)
num=int(input("enter any number:"))
ob=B()
print(ob.fact(num))
