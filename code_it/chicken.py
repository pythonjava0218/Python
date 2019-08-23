# 매출 파일 열기
# 파일 경로는 "data/chicken.txt" 입니다.
file = open('chicken.txt', 'r')

total = 0
day = 0

for i in file:
    data = i.strip().split("일:")
    total += int(data[1])
    day += 1
print(total / day)

 

# 파일 닫기

file.close()
