
H = Node(1)
H.next = Node(2)
H.next.next = Node(4)
H.next.next.next = Node(5)
H.next.next.next.next = Node(6)

temp1 = H
n = 0
while temp1 != None:
    temp1 = temp1.next
    n += 1

temp2 = H
mid = n//2
i = 0
while i < mid :
    temp2 = temp2.next
    i = i+1
    
print(temp2.data)

temp3 = H

i = 0
while i < mid-1:
    #print("Data:",temp3.data)
    temp3 = temp3.next
    i += 1
    
    
temp3.next = temp3.next.next
    

while H != None:
    print(H.data)
    H = H.next
    
     
