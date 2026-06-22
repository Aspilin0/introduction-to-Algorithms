A = [4,3,2,1,44,5,3,3,2]
for i in range(1,len(A)):
    j = i-1 
    key = A[i]
    while j >= 0 and key > A[j]:
        A[j+1] = A[j]
        j = j-1
    A[j+1] = key
print(A)
