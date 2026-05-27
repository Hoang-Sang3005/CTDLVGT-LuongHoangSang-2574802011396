def tim_ma_tran(a, x):

    for i in range(len(a)):

        for j in range(len(a[i])):

            if a[i][j] == x:
                return (i, j)

    return (-1, -1)


a = [
    [5,8,1],
    [3,9,7],
    [2,6,4]
]

x = int(input("Nhap x can tim: "))

print(tim_ma_tran(a, x))