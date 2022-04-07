
#iterative approach
def merge2( nums1, nums2 ): 
    l1 = len(nums1) 
    l2 = len(nums2) 
    i = j = 0 
    arr = list()
    while (i < l1 and j < l2): 
        if nums1[i] < nums2[j]: 
            arr.append(nums1[i]) 
            i+=1 
        elif nums1[i] > nums2[j]: 
            arr.append(nums2[j]) 
            j+=1 
        else: 
            arr.append(nums1[i]) 
            i +=1 
            j+= 1 
    while(i < l1): 
        arr.append(nums1[i]) 
        i+=1 
    while (j < l2): 
        arr.append(nums2[j]) 
        j+=1
    return arr 


#recursive approach
def merge(lst1, lst2): 
    if not lst1: 
        return lst2 
    if not lst2: 
        return lst1
    if lst1[0] < lst2[0]: 
        return [lst1[0]] + merge(lst1[1:], lst2) 
    elif lst2[0] < lst1[0]: 
        return [lst2[0]] + merge(lst1, lst2[1:]) 
    else: 
        return [lst1[0]] + merge(lst1[1:], lst2[1:])

def mergeSort(lst): 
    if len(lst) <= 1: 
        return lst; 
    else: 
        mid = len(lst) // 2
        return merge(mergeSort(lst[0:mid]), mergeSort(lst[mid:]))


if __name__ == '__main__': 
    lst = [3,5, 9, 1, 2, 3, 3, 7, 2]
    lst = mergeSort(lst) 
    print (lst)


#This is another modi 