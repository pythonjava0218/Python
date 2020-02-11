from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:
        pass

class Sendable(ABC):
    @abstractmethod
    def send(self) -> None:
        pass


class Email(Message, Sendable):
    def __init__(self, name, content, email):
        self.name = name
        self.content = content
        self.email = email

    def print_message(self) -> None:
        print(self.content)

    def send(self) -> None:
        print(self.email + "로 보냈습니다.")

user_email = Email("이민진", "추상클래스 연습중입니다.", "codeit@naver.com")

user_email.print_message()
user_email.send()