def min_max(a):

    min = a[0]
    max = a[0]

    vt_min = 0
    vt_max = 0

    for i in range(len(a)):

        if a[i] < min:
            min = a[i]
            vt_min = i

        if a[i] > max:
            max = a[i]
            vt_max = i

    print("Min =", min, "vi tri =", vt_min)
    print("Max =", max, "vi tri =", vt_max)


a = [4,1,7,9,5]

min_max(a)