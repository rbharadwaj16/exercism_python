class student:
    def __init__(self, name, grades=None):
        self.name = name
        if grades == None:
            self.grades = []
        else:
            self.grades = list(grades)

    def add(self, grade):
        self.grades.append(grade)

    def avg(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

