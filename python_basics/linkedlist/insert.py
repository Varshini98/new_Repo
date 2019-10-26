class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist:

    def __init__(self):
        self.head = None
    def insert(self,x):
        y = self.head
        if(y == None):
            self.head = node(x)
        else:
            while(y.next!=None):
                y = y.next
            y.next = node(x)
    def print(self):
        y = self.head
        while(y!=None):
            print(y.val)
            y=y.next
            
def length(l):
    x = l.head
    count=0
    while(x!=None):
        x=x.next
        count+=1
    return count    

l = Linkedlist()
l.insert(1)
l.insert(2)
l.insert(4)
l.insert(0)
l.print()
print(length(l))
