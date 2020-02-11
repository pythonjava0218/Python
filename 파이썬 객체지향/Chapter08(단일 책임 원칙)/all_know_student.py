class Student:
    def __init__(self, name, id, major):
        self.grades = []
        self.edit = Edit(name, id, major)
        self.grade = Grade(self.grades)
        self.print = Print(self.edit, self.grade)


class Edit:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major


class Grade:
    def __init__(self, grade):
        self.grades = grade

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)


class Print:
    def __init__(self, edit, grade):
        self.edit = edit
        self.grade = grade

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"
              .format(self.edit.name, self.edit.id, self.edit.major, self.grade.get_average_gpa()))


# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.edit.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
younghoon.grade.add_grade(3.0)
younghoon.grade.add_grade(3.33)
younghoon.grade.add_grade(3.67)
younghoon.grade.add_grade(4.3)

# 학생 성적표
younghoon.print.print_report_card()