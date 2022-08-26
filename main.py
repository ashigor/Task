class Student():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Задание № 2
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def description(self):
        ratings = self.grades
        courses_in_progress = ", ".join(self.courses_in_progress)
        return f'Имя: {self.name}, фамилия: {self.surname}, обучается на курсе: ' \
               f'{courses_in_progress}, cпиcок оценок: {ratings};'

    def calculation_mean(self):
        ratings = list(self.grades.values())
        average_rating_student = sum(ratings[0]) / len(ratings[0])
        return average_rating_student

    def __str__(self):
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за домашние задания: {self.calculation_mean()}" \
               f"\nКурсы в процессе изучения: {courses_in_progress}" \
               f"\nЗавершенные курсы: {finished_courses}"

# Задание № 1
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def description(self):
        ratings = self.grades
        courses_in_progress = ", ".join(self.courses_attached)
        return f'Имя: {self.name}, фамилия: {self.surname}, преподает: ' \
               f'{courses_in_progress}, оценки студентов: {ratings};'

    def calculation_mean(self):
        ratings = list(self.grades.values())
        return sum(ratings[0]) / len(ratings[0])

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за лекции: {self.calculation_mean()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Задание № 2
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}"


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)

some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'Git', 9)

# Задание № 3.1
print(some_student)
# print(some_lecturer)
# print(some_reviewer)

# Задание № 3.2
# if some_lecturer.calculation_mean() > some_student.calculation_mean():
#     print("Лекторов по средней оценке за лекции больше, чем студентов по средней оценке за домашние задания")
# elif some_lecturer.calculation_mean() < some_student.calculation_mean():
#     print("Студентов по средней оценке за домашние задания больше, чем лекторов по средней оценке за лекциии")
# else:
#     print("Лекторов по средней оценке за лекции равен студентов по средней оценке за домашние задания")

# Задание № 4
# print(some_student.description())
# print(some_lecturer.description())