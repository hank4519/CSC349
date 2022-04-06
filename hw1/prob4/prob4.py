
def if_match(lst, min, max): 
    if min > max: 
        return -1 
    mid = int ((max + min) / 2)
    if lst[mid] > (mid + 1): 
        #recurse left 
        return if_match(lst, min, mid - 1)
    elif lst[mid] < (mid + 1): 
        #recurse right
        return if_match(lst, mid+1, max) 
    else: 
        return mid + 1

lst1 =  [-10, -4, 3, 41]
lst2 = [4, 7, 19, 20]
ans = if_match(lst1, 0, len(lst1))
if ans != -1: 
    print(ans)