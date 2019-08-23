#w_file = open('vocabulary.txt', 'w')
r_file = open('vocabulary.txt', 'r')


for file in r_file: 
    voca = file.split(":")
    eng = voca[0]
    kor = voca[1]

    user_eng = input("%s: " % kor.strip())
    if eng == user_eng:
        print("맞았습니다.\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % eng)
r_file.close()
 
