#w_file = open('vocabulary.txt', 'w')
r_file = open('vocabulary.txt', 'r')

voca = ""
eng = ""
kor = ""

for i in r_file: 
    voca = i.split(":")
    eng = voca[0]
    kor = voca[1]

    user_eng = input(kor.strip() + ": ")
    if eng == user_eng:
        print("맞았습니다.\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % eng)
r_file.close()
 
