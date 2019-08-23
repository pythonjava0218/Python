file = open('chicken.txt', 'r')
for i in file:
    print(i.strip(), end=' ')

file.close()


'''
print(f.read()) = 전체읽기

file.seek(0) = 처음부터읽음
=> 파이썬은 한번 읽으면 끝.

file.read(1) = 한 글자 씩 읽기

'''
