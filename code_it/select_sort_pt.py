
my_list = [11, 3, 6, 4, 12, 1, 2]

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

    print(my_list)
