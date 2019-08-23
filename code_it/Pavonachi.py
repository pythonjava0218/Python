first = 1
second = 0
result = 0
count = 0

while count < 5:
    print(first)
    second = first
    print(second)
    result = first + second
    print(result)
    second += first
    count += 1

