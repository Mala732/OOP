class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    
        
H = Node(11)
H.next = Node(22)
H.next.next = Node(33)
H.next.next.next = Node(47)
H.next.next.next.next = Node(55)
H.next.next.next.next.next = Node(66)

n = 3  #n-th node from the end

c = 0
temp = H
while temp != None:
    c += 1
    temp = temp.next
    
k = c - n 
temp2 = H
i = 0
while i < k-1:
    temp2 = temp2.next
    i += 1
    
# print(temp2.data)

temp2.next = temp2.next.next

while H != None:
    print(H.data)
    H = H.next
