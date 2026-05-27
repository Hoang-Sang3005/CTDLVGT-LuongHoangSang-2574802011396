danh_ba = []


while True:

    print("1. Them lien he")
    print("2. Tim theo ten")
    print("3. Tim theo so dien thoai")
    print("4. Liet ke so bat dau bang 090")
    print("0. Thoat")

    chon = int(input("Nhap lua chon: "))

    if chon == 1:

        ten = input("Nhap ten: ")
        sdt = input("Nhap so dien thoai: ")

        danh_ba.append([ten, sdt])

    elif chon == 2:

        ten_tim = input("Nhap ten can tim: ")

        tim_thay = False

        for i in range(len(danh_ba)):

            if danh_ba[i][0] == ten_tim:

                print("So dien thoai:", danh_ba[i][1])
                tim_thay = True

        if tim_thay == False:
            print("Khong tim thay")

    elif chon == 3:

        sdt_tim = input("Nhap so dien thoai can tim: ")

        tim_thay = False

        for i in range(len(danh_ba)):

            if danh_ba[i][1] == sdt_tim:

                print("Ten:", danh_ba[i][0])
                tim_thay = True

        if tim_thay == False:
            print("Khong tim thay")

    elif chon == 4:

        for i in range(len(danh_ba)):

            if danh_ba[i][1].startswith("090"):

                print(danh_ba[i])

    elif chon == 0:
        break