def is_palindrome(word):
    # 코드를 입력하세요.
    length = len(word)

    j = 0
    for i in range(length-1, 0, -1):
       if word[i] == word[j]:
           j += 1
       else:
           return False
    return True
# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))