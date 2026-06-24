def merge_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    
    mid = len(data_list)//2
    left = merge_sort(data_list[:mid])
    right = merge_sort(data_list[mid:])

    result = []
    i , j = 0 , 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(right[j])
            j = j + 1
        else :
            result.append(left[i])
            i = i + 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([1,3,5,1,1,32,1,1,4]))
    
    

