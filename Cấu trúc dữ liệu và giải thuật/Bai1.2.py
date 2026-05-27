def tuyen_tinh(array,n,x):
    for i in range(0,n):
        if (array[i] == x):
            return i
    return -1
array = [15, 25, 80, 30, 60, 50,110, 100, 130, 180]
x = 110
n = len(array)
ketqua = tuyen_tinh(array, n, x)
print("Phần tử tìm được tại vị trí là: ", ketqua)

def tuyen_tinh(array,n,x):
    for i in range(0,n):
        if (array[i] == x):
            return i
        return -1
array = [15, 25, 80, 30, 60, 50, 15, 25, 80, 30, 60, 50,]
x = 185
n = len(array)
ketqua = tuyen_tinh(array,n,x)
print("Phần tử tìm được tại vị trí là: ",ketqua)