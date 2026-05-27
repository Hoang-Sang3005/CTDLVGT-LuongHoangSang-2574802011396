def max_list(a):
    max_numbers = a[0]
    for i in range(len(a)):
        if a[i] > max_numbers:
            max_numbers = a[i]
    return max_numbers
a = [ 5 ,5 ,7 ,7 ,8, 98 ,87 ,887, 54 ,7777]
print(max_list(a))