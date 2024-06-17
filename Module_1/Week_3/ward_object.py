"""
Một Ward (phường) gồm có name (string) và danh sách của mọi người trong Ward.
Một người person có thể là student, doctor, hoặc teacher. Một student gồm có name,
yob (int) (năm sinh), và grade (string). Một teacher gồm có name, yob, và subject
(string). Một doctor gồm có name, yob, và specialist (string). Lưu ý cần sử dụng a
list để chứa danh sách của mọi người trong Ward.
    (a) Cài đặt các class Student, Doctor, và Teacher theo mô tả trên. Thực hiện phương thức
describe() method để in ra tất cả thông tin của các object.
    (b) Viết add_person(person) method trong Ward class để add thêm một người mới với nghề
nghiệp bất kỳ (student, teacher, doctor) vào danh sách người của ward. Tạo ra một ward
object, và thêm vào 1 student, 2 teacher, và 2 doctor. Thực hiện describe() method để in ra
tên ward (name) và toàn bộ thông tin của từng người trong ward.
    (c) Viết count_doctor() method để đếm số lượng doctor trong ward.
    (d) Viết sort_age() method để sort mọi người trong ward theo tuổi của họ với thứ tự tăng dần.
(hint: Có thể sử dụng sort của list hoặc viết thêm function đều được)
    (e) Viết compute_average() method để tính trung bình năm sinh của các teachers trong ward.
"""


class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade})")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject})")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist})")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self.people)

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        teachers = [
            person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        total_yob = sum(teacher.yob for teacher in teachers)
        return int(total_yob / len(teachers))


ward1 = Ward("Ward 1")

student1 = Student(name="studentA", yob=2010, grade="7")

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1982, subject="Physics")

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1979, specialist="Cardiologists")

ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)


if __name__ == "__main__":
    print("--------------------------------------------------------------")
    student1.describe()
    teacher1.describe()
    doctor1.describe()
    print("--------------------------------------------------------------")
    ward1.describe()
    print("--------------------------------------------------------------")
    print(f"\nNumber of doctors : { ward1 . count_doctor ()}")
    print("--------------------------------------------------------------")
    print("\nAfter sorting Age of Ward1 people")
    ward1.sort_age()
    ward1.describe()
    print("--------------------------------------------------------------")
    print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
