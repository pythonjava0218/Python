w_file = open('vocabulary.txt', 'w')

eng = ""

while eng != "q":
    eng = input("영어를 입력하세요:")
    if eng != "q":
        kor = input("한국어 뜻을 입력하세요:")
        w_file.write("%s: %s\n" % (eng, kor))

w_file.close()
