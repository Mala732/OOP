def binary_search(arr,target,start,end):
    mid = (start + end)//2
    if start <= end:
        if arr[mid] == target:
            return "Target found in array"
        elif arr[mid] < target:
            start = mid + 1
            binary_search(arr,target,start,end)
            
        elif arr[mid] > target:
            end = mid - 1
    return "Target not found"
    
    
arr = [1,4,8,9,16,24,67,78]
target = 10
print(binary_search(arr,target,0,len(arr)-1))
