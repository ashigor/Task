import statistics

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

    # def calculation_mean(self):
    #     ratings = list(self.grades.values())
    #     average_rating_student = sum(ratings[0]) / len(ratings[0])
    #     return average_rating_student

    def __lt__(self, other):
        # module_1 = calculation_mean(self.grades)
        # module_2 = calculation_mean(other.grades)
        # return module_1 < module_2
        if isinstance(self, Student) and isinstance(other, Student):
            return calculation_mean(self.grades) < calculation_mean(other.grades)
        else:
            return 'Ошибка!'

    def __gt__(self, other):
        # module_1 = calculation_mean(self.grades)
        # module_2 = calculation_mean(other.grades)
        # return module_1 > module_2
        if isinstance(self, Student) and isinstance(other, Student):
            return calculation_mean(self.grades) > calculation_mean(other.grades)
        else:
            return 'Ошибка!'

    def __eq__(self, other):
        # module_1 = calculation_mean(self.grades)
        # module_2 = calculation_mean(other.grades)
        # return module_1 == module_2
        if isinstance(self, Student) and isinstance(other, Student):
            return calculation_mean(self.grades) == calculation_mean(other.grades)
        else:
            return 'Ошибка!'

    def __str__(self):
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за домашние задания: {calculation_mean(self.grades)}" \
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

    # def calculation_mean(self):
    #     ratings = list(self.grades.values())
    #     return sum(ratings[0]) / len(ratings[0])

    def __lt__(self, other):
        # module_1 = calculation_mean(self.grades)
        # module_2 = other.calculation_mean()
        # return module_1 < module_2
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return calculation_mean(self.grades) < calculation_mean(other.grades)
        else:
            return 'Ошибка!'

    def __gt__(self, other):
        # module_1 = calculation_mean(self.grades)
        # module_2 = other.calculation_mean()
        # return module_1 > module_2
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return calculation_mean(self.grades) > calculation_mean(other.grades)
        else:
            return 'Ошибка!'

    def __eq__(self, other):
        # module_1 = calculation_mean(self.grades)
        # module_2 = other.calculation_mean()
        # return module_1 == module_2
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return calculation_mean(self.grades) == calculation_mean(other.grades)
        else:
            return 'Ошибка!'

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за лекции: {calculation_mean(self.grades)}"


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

# Студент 1
student_1 = Student('Ruoy', 'Eman', 'woman')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

# Студент 2
student_2 = Student('Adam', 'Stander', 'male')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

# Студент 3
student_3 = Student('Riki', 'Misumi', 'women')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

# Эксперт
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'Git']

# Лектор 1
lecturer_1 = Lecturer('Robert', 'Steffen')
lecturer_1.courses_attached += ['Python', 'Git']

# Лектор 2
lecturer_2 = Lecturer('David', 'Miller')
lecturer_2.courses_attached += ['Python', 'Git']

# Лектор 3
lecturer_3 = Lecturer('Some', 'Buddy')
lecturer_3.courses_attached += ['Python', 'Git']

# Эксперт ставит оценку к студенту 1
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)

# Эксперт ставит оценку к студенту 2
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Git', 10)

# Эксперт ставит оценку к студенту 3
reviewer_1.rate_hw(student_3, 'Python', 8)
reviewer_1.rate_hw(student_3, 'Python', 9)
reviewer_1.rate_hw(student_3, 'Git', 10)

# Студент 1 ставит оценку к лектору 1-3
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_2, 'Python', 8)
student_1.rate_hw(lecturer_3, 'Git', 7)

# Студент 2 ставит оценку к лектору 1-3
student_2.rate_hw(lecturer_1, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Python', 10)
student_2.rate_hw(lecturer_3, 'Git', 9)

# Студент 3 ставит оценку к лектору 1-3
student_3.rate_hw(lecturer_1, 'Python', 8)
student_3.rate_hw(lecturer_2, 'Python', 9)
student_3.rate_hw(lecturer_3, 'Git', 9)


# Задание № 4
def calculation_mean(grades):
    ratings = list(grades.values())
    average_rating_student = sum(ratings[0]) / len(ratings[0])
    return average_rating_student


# Задание № 3.1
# print(student_1)
# print(lecturer_1)
# print(reviewer_1)


# Задание № 3.2
print(student_1 > student_2)
# print(lecturer_1 > lecturer_2)