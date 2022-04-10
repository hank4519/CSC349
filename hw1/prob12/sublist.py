import math
from tkinter import RIDGE

def find_sublist(arr, left, right): 
    if left > right: 
        return -math.inf
    mid  = (left + right) // 2 
    curr = left_sum = right_sum = 0 
    for i in range (mid - 1, left - 1, -1): 
        curr += arr[i]
        left_sum = max (curr, left_sum) 
    curr = 0 
    for i in range(mid + 1, right + 1 ): 
        curr += arr[i] 
        right_sum = max (curr, right_sum)
    combined_sum = left_sum + right_sum + arr[mid] 

    left_branch = find_sublist(arr, left, mid - 1) 
    right_branch = find_sublist(arr, mid + 1, right) 
    return max (combined_sum, left_branch, right_branch) 

if __name__ == "__main__": 
    lst = [1, -4, 3, 7, -5, 6, -9, 5] 
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums2 = [1]
    nums3 = [5,4,-1,7,8]
    max_continuous = find_sublist(lst, 0, len(lst) - 1) 
    print (max_continuous)
    m2 = find_sublist(nums, 0, len(nums) - 1)
    print(m2) 
    m3 = find_sublist(nums2, 0, len(nums2)- 1 )
    print(m3)
    m4 = find_sublist(nums3, 0, len(nums3) - 1)
    print(m4)