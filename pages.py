def ispossible(stu, arr, mid):
    c_stud = 1
    c_sum = 0
    
    for i in arr:
        if c_sum + i > mid:
            c_stud += 1
            c_sum = i
            
        else:
            c_sum += i
            
    return c_stud


def check_binary(arr,stu):
    s = 0
    e = sum(arr)
    mid = (s + e)//2
    
    while s <= e:
        if ispossible(stu, arr, mid) < stu:
            e = mid - 1 
        elif ispossible(stu, arr, mid) > stu:
            s = mid + 1

        else:
            ans = mid
            e = mid - 1
            
        mid = (s + e)//2
        
    return ans
            
    
    
arr = [10,20,30,40]; n = 2

print(check_binary(arr, n))
