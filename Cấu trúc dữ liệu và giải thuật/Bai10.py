def vi_tri_cuoi(a , x):
    vitri = -1
    for i in range(len(a)):
        if a[i] ==x:
            vitri = i
    return vitri
a = [4,1,4,9,5]
print(vi_tri_cuoi(a,5))
            
