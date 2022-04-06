


def scale(num1, num2): 
    if isinstance(num1, int): 
        if num1 == num2:
            return 0 
        else: 
            return num1 if num1 > num2 else num2 
    else: 
        sum1 = sum(num1) 
        sum2 = sum(num2) 
        if sum1 == sum2: 
            return 0
        else: 
            return 1 if sum1 > sum2 else -1

def find_marble(lst, min, max): 
    if(max - min == 3): 
        heavy = scale(lst[0], lst[2])
        if heavy == 0:
            return lst[1]
        else: 
            return heavy 

    else: 
        length = len(lst) 
        length = int (length/3)
        #print ('length', length)
        lst1 = lst[min: length] 
        lst2 = lst[length: 2* length] 
        lst3 = lst[2*length: 3 * length] 
        heavy = scale(lst1, lst2)
        if heavy == 0: 
            return find_marble(lst3, min + 2 * length, min + 3*length)
        else: 
            if heavy == 1: 
                return find_marble(lst1, min, min + length)
            else:
                return find_marble(lst2, min + length, min + length * 2) 


file =  open('input.txt', 'r') 
line = file.readline() 
file.close() 
line = line.strip()
lst =  line.split(' ') 
for i in range (len(lst)): 
    lst[i] = int(lst[i]) 

length = len (lst) 
if length == 1: 
    ans = lst[0] 
elif length % 3 != 0: 
    print('Must be 3^n') 
    quit() 
else: 
    ans = find_marble(lst, 0, len(lst))

print(ans) 