class User: # 클래스 이름 첫글자는 항상 대문자
    # 클래스 내용을 비워두면 에러 발생
    # pass
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def check_name(self, name):
        return self.name == name

# User 인스턴스 생성
user1 = User()
user2 = User()
user3 = User()

# 인스턴스 변수 정의하기
# 인스턴스이름.속성이름(인스턴스 변수) = 속성에 넣을 값

user1.name = "이민진"
user1.email = "alswls@naver.com"
user1.password = "12345"


user2.name = "김서진"
user2.email = "tjwls@naver.com"
user2.password = "52432"

user3.name = "박지진"
user3.email = "wlwls@naver.com"
user3.password = "11255"

'''
User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)
'''

user1.say_hello();
print(user1.check_name("이킨진"))
# 인스턴스 변수 사용하기
#인스턴스이름.인스턴스 변수이름
