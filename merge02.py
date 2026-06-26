def merge_sort(data_list):
    if len(data_list) <= 1:
        return data_list

    mid = len(data_list)//2
    left = merge_sort(data_list[:mid])
    right = merge_sort(data_list[mid:])
    result = []
    i, j = 0, 0
    left1 = left + [float("inf")]
    right1 = right + [float("inf")]
    for _ in range(len(left) + len(right)):
        
        if left1[i] < right1[j]:
            result.append(left1[i])
            i += 1
        else:
            result.append(right1[j])
            j += 1
        
    return result

A = [1,2,54,6,4,3,4,1,2,4,2]
print(merge_sort(A))                   

    