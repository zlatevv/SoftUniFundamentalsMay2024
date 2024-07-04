class Class:
    __students_count = 22
    def __init__(self, name: str) -> None:
        self.name = name
        self.students = []
        self.grades = []
    def add_student(self, name: str, grade: float) -> None:
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)
    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        average_grade = sum(self.grades) / len(self.students)
        return round(average_grade, 2)
    def __repr__(self):
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {', '.join(map(str, self.students))}. Average grade: {average_grade}"
a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)