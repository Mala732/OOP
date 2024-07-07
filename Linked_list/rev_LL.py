class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    
        
H = Node(11)
H.next = Node(22)
H.next.next = Node(33)
H.next.next.next = Node(44)

prev = None
curr = H

while (curr != None):
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    
H = prev

while H != None:
    print(H.data)
    H = H.next
    
    
