first = int(input("원하는 단 수를 입력해주세요"))

for i in range(first, first + 1):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j)
