'''
class User:
    pass

user1 = User()

user1.name = "Lee Min Jin"
user1.age = "20"

print(user1.name, user1.age)
'''

'''
class User:
    def introduce(some_user, n):
        for i in range(n):
            print("%s is %d years old." % (some_user.name, some_user.age))

user1 = User()

user1.name = "Lee Min Jin"
user1.age = 20
user1.email = "alswls0578@naver.com"


user1.introduce(2)
User.introduce(user1, 3)
'''

#메소드의 첫 번째 파라미터 이름은 self => 파이썬 커뮤니티의 약속

class User:
    def introduce(self, n):
        for i in range(n):
            print("%s is %d." % (self.name, self.age))

user1 = User()

user1.name = "LMJ"
user1.age = 20

 
user1.introduce(5)
User.introduce(user1, 1)

