def tim_ten(ds, ten):

    for i in range(len(ds)):

        if ds[i].lower() == ten.lower():
            return i

    return -1


ds = ["An", "Bình", "Châu"]

ten_can_tim = input("Nhap ten can tim: ")

ket_qua = tim_ten(ds, ten_can_tim)

if ket_qua != -1:
    print("Tim thay o vi tri:", ket_qua)
else:
    print("Khong tim thay")