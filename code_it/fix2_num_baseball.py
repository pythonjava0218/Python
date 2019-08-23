from random import randint
auto_numbers = []
user_numbers = []
count = 1
strike = 0
ball = 0
end = 0

while len(auto_numbers) < 3:
    
    new_number = randint(0, 9)

    while new_number in auto_numbers:
        new_number = randint(0, 9)
    auto_numbers.append(new_number)
print(auto_numbers)
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다. \n")

while strike != 3:
    user_numbers = []
    count = 1
    strike = 0
    ball = 0

    while len(user_numbers) < 3:
        enter = int(input("%d번째 수를 입력하세요." % count))
        if enter in user_numbers:
            print("중복되는 수입니다. 다시 입력해주세요.")
        elif enter > 9:
            print("범위를 벗어난 수 입니다. 다시 입력해주세요.")
        else:    
            user_numbers.append(enter)
            count += 1

    for i in range(0, len(user_numbers)):
        if user_numbers[i] == auto_numbers[i]:
            strike += 1
        elif user_numbers[i] in auto_numbers:
            ball += 1
    print("%dS %dB\n" % (strike, ball))
    end += 1
        
print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % end)
