
"""
 Def of majority: the occurence of a number > n / 2 
 if n is 7, the count has to be at least 4
 if n is 8, the count has to be at least 5
"""

def count_range(arr, x, low, high): 
    count = 0
    for i in range(low, high + 1): 
        if arr[i] == x: 
            count += 1 
    return count

def find_majority(arr, low, high): 
    if low == high: 
        return arr[low] 
    mid = (high+low) // 2
    left = find_majority(arr, low, mid) 
    right = find_majority(arr, mid + 1, high)
    if left == right: 
        return left
    left_count = count_range(arr, left, low, high) 
    right_count = count_range(arr, right, low, high) 
    if left_count > right_count:
        return left
    else: 
        return right

def check_half(majority, arr): 
    half = len(arr) // 2 
    count = 0
    for i in range (len(arr)): 
        if arr[i] == majority: 
            count+= 1
    if count > half: 
        return majority
    return -1 

if __name__ == '__main__': 
    arr = [5, 4, 5, 4, 3, 4, 4] 
    arr2 = [2, 4,6, 2, 2, 2, 9, 3] 
    majority = find_majority(arr, 0, len(arr) - 1)
    majority = check_half(majority, arr)
    print(majority)
    major2 = find_majority(arr2, 0, len(arr2) - 1) 
    major2 = check_half(major2, arr2 )
    print(major2)
