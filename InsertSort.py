A = [99,3,45,5,6,4,4]
for i in range(len(A)):
    key = A[i]
    j = i-1
    while 0 <= j and A[j] > key :    
        A[j+1] = A[j]
        j = j-1
    A[j+1] = key
 
print(A)

        
            