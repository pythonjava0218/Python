from random import randint

def generate_numbers():
    no = []

    while len(no) < 6:
        add = randint(1, 46)

        while add in no:
             add = randint(1, 46)
        no.append(add)
        
    no.sort()

    return no


def draw_winning_numbers():

    plus_no = []

    no = generate_numbers()

    plus_no = randint(1, 46)

    while plus_no in no:
        plus_no = randint(1, 46)
    no.append(plus_no)
    
    return no
 

def count_matching_numbers(list1, list2):

    num = 0
    
    if len(list1) > len(list2):
        a = list1
    else:
        a = list2

    for i in range(0, len(a)):
        if list1[i] in list2:
            num += 1
        
    return num

print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))


def check(numbers, winning_numbers):

    matching = count_matching_numbers(list1, list2)
    
    numbers = matching

    winning_numbers = 

    count = count_matching_numbers

    if numbers in winning_numbers[6]:
        plus += 1
     
    if count == 6:
        return "1000000000"
    elif count == 5 and plus == 1:
        return "50000000"
    elif count == 5:
        return "1000000"
    elif count == 4:
        return "50000"
    elif count == 3:
        return "5000"
    else:
        return "0"
