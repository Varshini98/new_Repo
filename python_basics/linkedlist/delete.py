class node:
    def __init__(self,val):
        self.val =val
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None
    
    def insert(self,val):
        x = self.head
        if(x==None):
            self.head = node(val)
        else:
            while(x.next!=None):
                x = x.next
            x.next = node(val)
    
    def remove(self,val):
        x = self.head
        if(x.val == val):
            self.head = x.next
        else:
            while(x.next!=None and x.next.val!=val):
                x=x.next
            if(x.next==None):
                print("no such value")
            else:
                x.next = x.next.next
                print("deleted")
                
    def print(self):
        x= self.head
        while(x!=None):
            print(x.val)
            x=x.next

l = Linkedlist()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.print()
l.remove(2)
l.remove(4)
l.remove(10)
l.print()
        
