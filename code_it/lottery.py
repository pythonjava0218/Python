from random import randint

def generate_numbers():
    no = []

    while len(no) < 6:
        add = randint(1, 45)

        while add in no:
             add = randint(1, 45)
        no.append(add)
        
    no.sort()

    return no


def draw_winning_numbers():


    no = generate_numbers()

    plus_no = randint(1, 45)

    while plus_no in no:
        plus_no = randint(1, 45)
    no.append(plus_no)
    
    return no
 

def count_matching_numbers(list1, list2):

    num = 0
    
    for answer in range(0, len(list1)):
        if list1[answer] in list2:
            num += 1
    return num

 
def check(numbers, winning_numbers):

    plus = 0
    
    count = count_matching_numbers(numbers, winning_numbers[:-1])

    if winning_numbers[6] in numbers:
        plus += 1
        
    if count == 6:
        return 1000000000
    elif count == 5 and plus == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
