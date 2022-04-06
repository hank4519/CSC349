
import sys 

def find_singleton(nums, min, max): 
    mid = int ((min + max) / 2 )
    if min >= max or (nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]): 
        return nums[mid] 
    if mid + 1 <= max and nums[mid] == nums[mid+1]: 
        choice = max - mid - 1
        if choice % 2 == 1: 
            return find_singleton(nums, mid + 2, max) 
        else: 
            return find_singleton(nums, min, mid - 1) 
    elif mid - 1 >= min and nums[mid] == nums[mid - 1]: 
        choice = mid - min - 1 
        if choice % 2 == 1: 
            return find_singleton(nums, min, mid - 2) 
        else: 
            return find_singleton(nums, mid + 1, max) 


#file = open('in3.txt', 'r') 
if len (sys.argv) != 2: 
    print("Usage: python3 singleton.py *.txt")
    quit() 
file = open(sys.argv[1], 'r') 
lines = file.readlines() 
if len(lines) == 0: 
    quit()
if len(lines) != 1: 
    print('Input contains too many lines')
    quit() 

line = lines[0] 
line = line.strip() 
line = line.split(',') 
for i in range(len(line)): 
    line[i] = int(line[i])

odd_number = len(line) 
if odd_number % 2 == 1: 
    ans = find_singleton(line, 0, len(line) - 1 )
    print(ans)


file.close()