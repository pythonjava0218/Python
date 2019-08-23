from random import randint

count = 4
c_count = 1
num = randint(1, 20)
end = 0
        
while count != 0:

    enter = int(input("기회가 %d번 남았습니다. 1 ~ 20 사이의 숫자를 맞춰보세요:" % (count)))
    print(num)
    
    if enter > num:
        print("Down")
        count -= 1
        c_count += 1
        
    elif enter < num:
        print("Up")
        count -= 1
        c_count += 1
    
    else:
        print("축하합니다 %d번만에 숫자를 맞추셨습니다." % c_count)
        count = 0
        end = 1

if end == 0:
    print("아쉽습니다. 정답은 %d였습니다." % (num))
    
    
