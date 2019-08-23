from random import randint
r_file = open('vocabulary.txt', 'r')

dic = {}

user = ""

for file in r_file:
    voca = file.strip("\n").split(": ")
    eng = voca[0]
    kor = voca[1]

    dic[kor] = eng  

keys = list(dic.keys())
    
while user != "q":
    num = randint(0, len(keys) - 1)

    kor_word = keys[num]
    eng_word = dic[kor_word]

    user = input(kor_word)

    
    if user == eng_word:
        print("맞았습니다. \n")
    elif user == "q":
        break;
    else:
        print("틀렸습니다. 정답은 %s입니다.\n" % eng_word)


r_file.close()
