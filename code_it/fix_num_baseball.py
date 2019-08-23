from random import randint
auto_numbers = []
user_numbers = []
count = 1
answer = 0
strike = 0
ball = 0
end = 1

while len(auto_numbers) < 3:
    new_number = randint(0, 9)

    while new_number in auto_numbers:
        new_number = randint(0, 9)
    auto_numbers.append(new_number)
print(auto_numbers)
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다. \n")
print("세 수를 하나씩 차례대로 입력하세요.")

while len(user_numbers) < 3:
    enter = int(input("%d번째 수를 입력하세요." % count))
    if enter in user_numbers:
        print("중복되는 수 입니다. 다시 입력해주세요.")
    elif enter > 9:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
    else:
        user_numbers.append(enter)
        count += 1
        
        if auto_numbers[answer] == user_numbers[answer]:
            strike += 1
        elif user_numbers[answer] in auto_numbers:
            ball += 1
        answer += 1

        if count == 4 and strike != 3:
            print("%dS %dB\n" % (strike, ball)) 
            user_numbers = []
            count = 1
            answer = 0
            strike = 0
            ball = 0
            end += 1
            print("세 수를 하나씩 차례대로 입력하세요.")
        elif strike == 3:
            print("%dS %dB\n" % (strike, ball)) 
            print("축하합니다 %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % end)
       

    
