from ArrayStack import ArrayStack
class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        max = 0
    def is_empty(self):
        self.data.is_empty()
    def pop(self):
        self.data.pop()
        max = self.data.top()[1]
    def top(self):
        self.data.top()
    def __len__(self):
        self.data.len()
    def push(self,elem):
        if (elem > max):
            max = elem
        self.data.push((elem,max))
    def max(self):
        return max
def main():
    maxS = MaxStack()
    maxS.push(3)
    maxS.push(1)
    maxS.push(6)
    maxS.push(4)
    print(maxS.max())
    maxS.pop()
    print(maxS.max())
