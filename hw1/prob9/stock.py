
def find_profit_helper(arr, left, right) -> int: 
    if left == right: 
        return 0
    mid = left + (right - left) // 2 
    left_min = min(arr[left: mid + 1])
    right_max = max(arr[mid+1: ])
    cross_profit = right_max - left_min 

    left_branch = find_profit_helper(arr, left, mid) 
    right_branch = find_profit_helper(arr, mid+1, right)

    return max(left_branch, right_branch, cross_profit) 


def find_max_profit(arr) -> int: 
    return find_profit_helper(arr, 0, len(arr) - 1)

if __name__ == '__main__': 
    arr = [50, 40, 70, 69, 100]
    max_profit = find_max_profit(arr)
    print(max_profit)