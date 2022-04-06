

def find_first(lst, x, min, max): 
    if min >= max: 
        return min
    mid = int ( (min+max) / 2) 
    if lst[mid] < x: 
        #recurse right 
        return find_first(lst, x, mid + 1, max) 
    elif lst[mid] > x or (lst[mid] == x and lst[mid] == lst[mid-1]): 
        #recurse left
        return find_first (lst, x, min, mid - 1)
    else: 
        return mid

def find_last(lst, x, min, max): 
    if min >= max: 
        return min
    mid = int ( (min + max ) / 2 )
    if lst[mid] < x or (lst[mid] == x and lst[mid] == lst[mid+1]): 
        #recurse right
        return find_last(lst, x, mid + 1, max) 
    elif lst[mid] > x: 
        #recurse left 
        return find_last(lst, x, min, mid - 1) 
    else:
        return mid
    
x = 4
lst = [1, 2, 2, 2, 4, 4, 12, 20, 20, 20]
first = find_first(lst, x, 0, len(lst) - 1) 
last = find_last(lst, x, 0, len(lst) - 1)
ans = last - first + 1
print(ans)