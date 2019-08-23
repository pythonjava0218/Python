
def is_palindrome(word):
    # 코드를 입력하세요.
    for left_index in range(0, int(len(word) / 2)):
        right_index = len(word) - left_index - 1
        if word[left_index] != word[right_index]:
            return False
       
    return True
    
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))







'''
ex = "stars"

for left_index in range(0, int(len(ex) / 2)):
    right_index = len(ex) - left_index - 1
    print("l", ex[left_index])
    print("r", ex[right_index])
    if ex[left_index] != ex[right_index]:
        print(bool(ex))
 
 
'''
 
 
