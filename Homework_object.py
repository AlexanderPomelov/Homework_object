import statistics

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}
        self.average = []

    def rate_lectur(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_attached and course in lectur.courses_in_progress:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grades_student(self):
        average_list_student = []
        for k,v in self.grades.items():
            result_average_student = average_list_student.extend(v)
            result_average_student = statistics.mean(average_list_student)
        self.average.append(result_average_student)
        return result_average_student

    def __str__(self):
        name_str_student = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                           f'Средняя оценка за домашние задания: {self._average_grades_student()}\n' \
                           f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n' \
                           f'Завершенные курсы: {",".join(self.finished_courses)}'
        return name_str_student

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Оценок нет')
        return self.average < other.average

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        name_str_mentor = f'Имя: {self.name}\nФамилия: {self.surname}'
        return name_str_mentor



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}
        self.average = []


    def _average_grades(self):
        average_list = []
        for k, v in self.grades.items():
            result_average_lectur = average_list.extend(v)
            result_average_lectur = statistics.mean(average_list)
        self.average.append(result_average_lectur)
        return result_average_lectur

    def __str__(self):
        name_str_lectur = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                          f'Средняя оценка за лекции: {self._average_grades()}'
        return name_str_lectur

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Оценок нет')
        return self.average < other.average



class Reviewer(Mentor):
    """Наследование класса Mentor"""
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name_str_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return name_str_reviewer


def average_student(students, course):

    all_grades = []
    for student in student_list:
        all_grades += student.grades.get(course)
    average = sum(all_grades)/len(all_grades)
    return average

def average_lecturer(lecturer, course):
    all_grades = []
    for lecturer in lecturer_list:
        all_grades += lecturer.grades.get(course)
    average = sum(all_grades)/len(all_grades)
    return average

#Экземпляры Student
student_1_Julia_Zaharova = Student('Юлия', 'Захарова', 'Famale')
student_2_Mark_Volokv = Student('Марк', 'Волков', 'Male')
"""Атрибуты Student"""
student_1_Julia_Zaharova.courses_attached += ['Fullstack', 'SQL']
student_1_Julia_Zaharova.courses_in_progress += ['Git', 'Java']
student_1_Julia_Zaharova.finished_courses += ['Компьютерная грамотность']
student_2_Mark_Volokv.courses_attached += ['Fullstack', 'SQL']
student_2_Mark_Volokv.courses_in_progress += ['Git', 'Java']
student_2_Mark_Volokv.finished_courses += ['Английский для IT - специалистов']

#Экземпляры Mentor
mentor_1_Artem_Knyazev = Mentor('Артем', 'Князев')
mentor_2_Arina_Ivanova = Mentor('Арина', 'Иванова')

#Экземпляры Lecturer
lecturer_1_Alia_Petrova = Lecturer('Алия', 'Петрова')
lecturer_2_Sofia_Romanova = Lecturer('София', 'Романова')
"""Атрибуты Lecturer"""
lecturer_1_Alia_Petrova.courses_in_progress += ['Fullstack', 'SQL']
lecturer_2_Sofia_Romanova.courses_in_progress += ['Fullstack','SQL']


#Экземпляры Reviewer
reviewer_1_Vera_Gorelova = Reviewer('Вера', 'Горелова')
reviewer_2_Valeria_Bolshakova = Reviewer('Валерия', 'Большакова')
"""Атрибуты Reviewer"""
reviewer_1_Vera_Gorelova.courses_attached += ['Git', 'Java']
reviewer_2_Valeria_Bolshakova.courses_attached += ['Git', 'Java']

#Вызов методов для Reviewer
"""Оценка ревьюерами студентов"""
reviewer_1_Vera_Gorelova.rate_hw(student_1_Julia_Zaharova, 'Git', 9)
reviewer_2_Valeria_Bolshakova.rate_hw(student_1_Julia_Zaharova,'Git', 7)
reviewer_1_Vera_Gorelova.rate_hw(student_1_Julia_Zaharova, 'Java', 8)
reviewer_1_Vera_Gorelova.rate_hw(student_2_Mark_Volokv, 'Java', 8)
reviewer_2_Valeria_Bolshakova.rate_hw(student_2_Mark_Volokv, 'Java', 7)
reviewer_1_Vera_Gorelova.rate_hw(student_2_Mark_Volokv, 'Git', 10)

#Вызов методов для Student
"""Оценка студентами лекторов"""
student_1_Julia_Zaharova.rate_lectur(lecturer_1_Alia_Petrova, 'Fullstack', 8)
student_1_Julia_Zaharova.rate_lectur(lecturer_1_Alia_Petrova, 'Fullstack', 10)
student_1_Julia_Zaharova.rate_lectur(lecturer_2_Sofia_Romanova, 'SQL', 5)
student_2_Mark_Volokv.rate_lectur(lecturer_1_Alia_Petrova, 'Fullstack', 7)
student_2_Mark_Volokv.rate_lectur(lecturer_2_Sofia_Romanova, 'SQL', 5)
student_2_Mark_Volokv.rate_lectur(lecturer_2_Sofia_Romanova, 'Fullstack', 10 )

#Вызов функций
student_list = [student_1_Julia_Zaharova, student_2_Mark_Volokv]
lecturer_list = [lecturer_1_Alia_Petrova, lecturer_2_Sofia_Romanova]
print(f'Вызов функции средней оценки за курс у студентов\n{average_student(student_list, "Java")}')
print(f'Вызов функции средней оценки за курс у лекторов\n{average_lecturer(lecturer_list, "Fullstack")}')
print()

#Вызов магического метода __str__ для студентов
print(f'Студент №1\n{student_1_Julia_Zaharova}')
print()
print(f'Студент №2\n{student_2_Mark_Volokv}')
print()

#Вызов магического метода __lt__ для студентов и лекторов
print(lecturer_1_Alia_Petrova < student_1_Julia_Zaharova)
print(lecturer_1_Alia_Petrova > student_1_Julia_Zaharova)
print(student_2_Mark_Volokv < lecturer_2_Sofia_Romanova)
print(student_2_Mark_Volokv > lecturer_2_Sofia_Romanova)
print()

#Вызов магического метода __str_ для лекторов
print(f'Лектор №1\n{lecturer_1_Alia_Petrova}')
print()
print(f'Лектор №2\n{lecturer_2_Sofia_Romanova}')
print()

#Вызов магического метода __str_ для ревьеров
print(f'Ревьюер №1\n{reviewer_1_Vera_Gorelova}')
print()
print(f'Ревьюер №2\n{reviewer_2_Valeria_Bolshakova}')
print()

#Вызов магического метода __str_ для менторов
print(f'Ментор №1\n{mentor_1_Artem_Knyazev}')
print()
print(f'Ментор №2\n{mentor_2_Arina_Ivanova}')
print()