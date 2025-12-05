from enum import Enum

z














































































def log_decorator(func):
    def wrapper(*args):
        # print(f"Calling function '{func.__name__}' with args: {args}")
        result = func(*args)
        # print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper


class Student:
#
#перевірки на додатні оцінки
#нове поле студента яке відповідає за систему оцінювання   5pointsys bool якщо при set більше 0 то видавати exception
#Поле id


    ######################################
    #                                    #
    #           Class variables          #
    #           with get, set            #
    #                                    #
    ######################################

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value != "" and value is not None and type(value) == str:
            self._name = value
        else :
            self._name = "Unknown"


    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if value != "" and value is not None and type(value) == str:
            self._surname = value
        else :
            self._surname = "Unknown"


    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        if value != "" and value is not None and type(value) == str:
            self._middle_name = value
        else:
            self._middle_name = "Unknown"

    @property
    def is5pointsys(self):
        return self._is5pointsys

    @is5pointsys.setter
    def is5pointsys(self, value):
        self._is5pointsys = value


    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, value):
        filtered_grades = []
        for grade in value:
            if type(grade) is not int and type(grade) is not float:
                continue

            if grade < 0 :
                grade = 0
                print("Scipped grade because smaller then 0")

            if self.is5pointsys and grade > 5:
                raise ValueError("Trying to assign grade bigger then 5 when there is 5 point system")


            filtered_grades.append(grade)

        self._grades = filtered_grades
        del filtered_grades

    @grades.deleter
    def grades(self):
        del self._grades


    ######################################
    #                                    #
    #           Class functions          #
    #                                    #
    ######################################

    def __init__(self, id, name, surname, middle_name, grades, is5pointsys):
        self.id = id
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.is5pointsys = is5pointsys
        self.grades = grades.copy()


    @classmethod
    def create_empty(cls):
        return cls(
            id=-1,
            name="",
            surname="",
            middle_name="",
            grades=[],
            is5pointsys=True
        )


    def __str__(self):
        return f"Student {self._surname} {self._name}"


    def __repr__(self):
        return f'class \'Student\' with \"{self._name}\" name'


    def __del__(self):
        del self.grades
        print(f"Deleting student {self._surname} {self._name}")


    @log_decorator
    def get_average_score(self):
        result = 0.0

        if len(self.grades) == 0:
            return 0

        for grade in self.grades:
            result += grade

        result /= len(self.grades)
        result = round(result, 2)

        return result


class Group:

    ######################################
    #                                    #
    #           Class variables          #
    #           with get, set            #
    #                                    #
    ######################################

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value != "" and value is not None and type(value) == str:
            self._name = value
        else:
            self._name = "Unknown"


    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, students):
        filtered_students = []
        for student in students:
            if type(student) is Student:
                filtered_students.append(student)

        self._students = filtered_students
        del filtered_students

    @students.deleter
    def students(self):
        del self._students

    ######################################
    #                                    #
    #           Class functions          #
    #                                    #
    ######################################

    def __init__(self, name, students):
        self.name = name
        self.students = students.copy()


    @classmethod
    def create_empty(cls):
        return cls (
            name="",
            students=[],
        )


    def __str__(self):
        return f"{self._name}"


    def __repr__(self):
        return f'class \'Group\' with \"{self.name}\" name'


    def __del__(self):
        del self.students
        print(f"Deleting group {self.name}")


    @log_decorator
    def get_average_score(self):
        result = 0.0

        if len(self.students) == 0:
            return 0

        for student in self.students:
            result += student.get_average_score()

        result /= len(self.students)
        result = round(result, 2)

        return result


    @log_decorator
    def add_student(self, student):
        self.students.append(student)


    @log_decorator
    def remove_student_by_name(self, student_name, student_surname):
        for student in self.students:
            if student.name == student_name and student.surname == student_surname:
                self.students.remove(student)
                return

        print(f"Student {student_surname} {student_name} doesn't exist 1")


    @log_decorator
    def remove_student_by_class(self, student_class):
        for student in self.students:
            if student.name == student_class.name and student.surname == student_class.surname:
                self.students.remove(student)
                return

        print(f"Student {student_class.surname} {student_class.name} doesn't exist 2")




if __name__ == '__main__':
    oleg = Student(0, "Oleg", "Bobr", "Petrov", [1, 0, 4], True)
    masha = Student(0, "Masha", "Tygr", "Mihailivna", [2, 4, 0], True)
    misha = Student(0, "Misha", "Werboviy", "Oleksandrovich", [5, 4, 5], True)
    empty_student = Student.create_empty()

    print(f"{oleg}\'s average score is {oleg.get_average_score()}")

    group = Group("IR-11", [oleg, masha])
    group.add_student(misha)
    group.add_student(empty_student)

    print(f"{group}\'s average score is {group.get_average_score()}\n")

    print("Removing student Oleg and empty student")
    group.remove_student_by_name("Oleg", "Bobr")
    group.remove_student_by_class(empty_student)
    print(f"{group}\'s average score is {group.get_average_score()}\n")
