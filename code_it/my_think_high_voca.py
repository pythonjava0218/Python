from random import randint

#w_file = open('vocabulary.txt', 'w')
r_file = open('vocabulary.txt', 'r')

count = 0
kor_list = []
    
for i in r_file: 
    voca = i.strip("\n").split(": ")
    eng = voca[0]
    kor = voca[1]
    count += 1

    kor_list.append(kor)    
    #user_eng = input(kor.strip()+ ": ")
while True:       
    num = randint(0, len(kor_list) - 1)
    print(num)
    user_eng = input("%s:" % kor_list[num])
    if eng == user_eng:
        print("맞았습니다.\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % eng)

    
r_file.close()
