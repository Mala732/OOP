a = 1010000
n = 1
m = 1000
res = 0

while a >= m:
    if a > m*1000:
        res = res + (m*1000 - m)*n +1
        print
    else:
        res = res + (a - m)*n + 1
        
    m = m*1000
    n = n + 1
        
print(res)
