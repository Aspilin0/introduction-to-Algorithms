# Input a list {a1,a2,a3,a4.......}
# Output the list in sorted order
a = [2,3,5,6,1,3,1,2,10,10]
res = [0] * len(a)
for i in range(len(a)) :
    num_e,num_b,num_s=0,0,0
    for m in range(len(a)):
        
        if a[i] > a[m]:
            num_b = num_b + 1
        elif a[i] == a[m]:
            num_e = num_e + 1
        else :
            num_s = num_s + 1
        
    res[num_b:num_b+num_e] = [a[i]]*num_e
print(res)
    
    
