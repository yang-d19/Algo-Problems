def solution(a):
    # special case
    if len(a) == 1:
        return True
        
    l = 0
    r = len(a) - 1
    ascend = True
    while l < r :
        if l == r - 1:
            if a[l] < a[r]:
                break
            else:
                ascend = False
                break
                
        if not a[l] < a[r]:
            ascend = False
            break
        
        if not a[r] < a[l + 1]:
            ascend = False
            break
        l += 1
        r -= 1
    
    return ascend

res = solution([1, 4, 5, 6, 3])

print(res)