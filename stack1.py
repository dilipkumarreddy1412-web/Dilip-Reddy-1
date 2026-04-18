class stack:
    def __init__(self,size):
        self.size=size
        self.stack=[None]*size
        self.top=-1
    def push(self,value):
        if self.top==self.size-1:
            print("stack overflow! cannot push",value)
        else:
            self.top+=1
            self.stack[self.top]=value
            print(value,"pushed")
    def pop(self):
        if self.top==-1:
            print("stack underflow! stack is empty")
        else:
            print(self.stack[self.top],"popped")
            self.top-=1
    def display(self):
        if self.top==-1:
            print("stack is empty")
        else:
            print("stack elements:",self.stack[:self.top+1])
s=stack(3)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
s.pop()
s.pop()
s.pop()
s.pop()
