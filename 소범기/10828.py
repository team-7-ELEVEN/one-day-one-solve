from sys import stdin,stdout
read = stdin.readline

class stackorder:
    def __init__(self):
        self._list = []
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
        
    def push(self,v):
        self._list.append(v)
        
        
    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            return self._list.pop()
    
    def size(self):
        return len(self._list)
    
        
    def top(self):
        if self.empty() == 1:
            return -1
        else:
            return self._list[-1]
        


def main():
    newstack = stackorder()
    N = int(read())
    for _ in range(N):
        order = list(read().split())
        if order[0] == "push":
            newstack.push(int(order[1]))
        elif order[0] == "pop":
            print(newstack.pop())
        elif order[0] == "size":
            print(newstack.size())
        elif order[0] == "empty":
            print(newstack.empty())
        elif order[0] == "top":
            print(newstack.top())  
            
if __name__=="__main__":
    main()
