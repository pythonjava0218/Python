class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_param):
        # 코드를 쓰세요
        younghoon_info = string_param.split(",")
        name = younghoon_info[0]
        email = younghoon_info[1]
        password = younghoon_info[2]

        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_param):
        # 코드를 쓰세요
        name = list_param[0]
        email = list_param[1]
        password = list_param[2]

        return cls(name, email, password)

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)