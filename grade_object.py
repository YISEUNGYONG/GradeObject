class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = english_score + c_score + python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        average = self.average_score
        if average >= 90:
            return 'A'
        elif 80 <= average < 90:
            return 'B'
        elif 70 <= average < 80:
            return 'C'
        elif 60 <= average < 70:
            return 'D'
        else:
            return 'F'

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def sort_students_by_total_score(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)

    def count_students_above_80(self):
        count = 0
        for student in self.students:
            if student.total_score >= 240:  # 80 * 3 = 240
                count += 1
        return count

    def display_student_info(self):
        for student in self.students:
            print("Student ID:", student.student_id)
            print("Name:", student.name)
            print("English Score:", student.english_score)
            print("C Score:", student.c_score)
            print("Python Score:", student.python_score)
            print("Total Score:", student.total_score)
            print("Average Score:", student.average_score)
            print("Grade:", student.grade)
            print()

# Main program
if __name__ == "__main__":
    grade_manager = GradeManager()

    # 입력 함수
    for _ in range(5):
        student_id = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        english_score = int(input("영어 점수를 입력하세요: "))
        c_score = int(input("C 언어 점수를 입력하세요: "))
        python_score = int(input("파이썬 점수를 입력하세요: "))
        student = Student(student_id, name, english_score, c_score, python_score)
        grade_manager.add_student(student)

    # 총점/평균 계산 함수
    # 학점 계산 함수
    for student in grade_manager.students:
        student.grade = student.calculate_grade()

    # 등수 계산 함수
    grade_manager.sort_students_by_total_score()

    # 출력 함수
    grade_manager.display_student_info()

    # 80점 이상 학생 수 카운트 함수
    count_above_80 = grade_manager.count_students_above_80()
    print("80점 이상 학생 수:", count_above_80)
