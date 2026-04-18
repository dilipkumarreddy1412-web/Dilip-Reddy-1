class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return"stack is empty"
    def peek(self):
         if not self.is_empty():
            return self.items[-1]
         return"stack is empty"
    def is_empty(self):
        return len(self.items)==0
    def display(self):
        print(self.items)
s=Stack()
s.push(5)
s.push(15)
s.push(25)
s.push(35)
s.display()
print("Pop:",s.pop())
print("Top:",s.peek())
s.display()
