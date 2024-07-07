
#21 -> 21 -> 46 -> 52 -> 52 -> 63 -> NULL
#remove the duplicates from the linked list 
#result : 21 -> 46 -> 52 -> 63 -> NULL

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
        
        
H = Node(21)
H.next = Node(21)
H.next.next = Node(46)
H.next.next.next = Node(52)
H.next.next.next.next = Node(52)
H.next.next.next.next.next = Node(63)

temp = H
while temp.next != None:
    if temp.next.data == temp.data:
        temp.next = temp.next.next
        
    temp = temp.next

    
while H != None:
    print(H.data)
    H = H.next
