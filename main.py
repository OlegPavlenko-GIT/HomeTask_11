    # Создать иерархию классов для описания академии.
    # Примерный список классов: Person, Teacher, Student, Subject, Academy и тд.
    # Продумать архитектуру: реализовать принципы ООП
    #
class Academy:
    def __init__(self):
        self.teachers = set()
        self.students = set()
        self.subjects = set()

    print("Academy:")


class Person:
    def __init__(self, name, age, gender, contact_email):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_email = contact_email

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_contact_email(self):
        return self.contact_email


class Teacher(Person):
    def __init__(self, name, age, gender, contact_email):
        super().__init__(name, age, gender, contact_email)
        self.subjects = set()


class Student(Person):
    def __init__(self, name, age, gender, contact_email):
        super().__init__(name, age, gender, contact_email)
        self.subjects = set()


class Subject:
    def __init__(self, name):
        self.name = name
        self.teachers = set()


teacher1 = Teacher("Helen", 35, "Female", "Helen@gmail.com")
student1 = Student("Ivan", 20, "Male", "Ivan@gmail.com")
subject1 = Subject("Python")
subject1.teachers = {teacher1}

print("Teacher name:", teacher1.get_name())
print("Teacher age:", teacher1.get_age())
print("Teacher gender:", teacher1.get_gender())
print("Teacher contact email:", teacher1.get_contact_email())
print("Student name:", student1.get_name())
print("Student age:", student1.get_age())
print("Student gender:", student1.get_gender())
print("Student contact email:", student1.get_contact_email())
print("Subject name:", subject1.name)
print("Subject teachers:", [teacher.get_name() for teacher in subject1.teachers])