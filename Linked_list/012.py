# A node can take values 0, 1 or 2
# 2 -> 2 -> 1 -> 2 -> 0 -> 1 -> 0 -> NULL
# should be converted to
# 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> 2 -> Null
# without sorting or using extra linked lists
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
        
        
H = Node(2)
H.next = Node(2)
H.next.next = Node(1)
H.next.next.next = Node(2)
H.next.next.next.next = Node(0)
H.next.next.next.next.next = Node(1)
H.next.next.next.next.next.next = Node(0)


temp = H
zero = 0
one = 0
two = 0

temp = H
while temp != None:
    if temp.data == 0:
        zero += 1
        
    elif temp.data == 1:
        one += 1
    
    else:
        two += 1
        
    temp = temp.next
    
temp2 = H
for i in range(zero):
    temp2.data = 0
    temp2 = temp2.next
    
for i in range(one):
    temp2.data = 1
    temp2 = temp2.next

for i in range(two):
    temp2.data = 2
    temp2 = temp2.next
    
    
# temp1 = H  
# while temp1 != None:
#     if zero != 0:
#         temp1.data = 0
#         zero -= 1
#     elif one != 0:
#         temp1.data = 1
#         one -= 1
#     elif two != 0:
#         temp1.data = 2
#         two -= 1
#     temp1 = temp1.next
    
while H != None:
    print(H.data)
    H = H.next
    
