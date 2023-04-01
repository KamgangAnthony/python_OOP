class MusicSchool:

    students = {"Gino": [15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": [28, "555-765-452", ["Chello"]],
                "Eric": [12, "583-356-223", ["Singing"]]}

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue

    def print_student(self, name):
        if name in MusicSchool.students.keys():
            print(f"Student: {name} who is {MusicSchool.students[name][0]} years old and is taking {MusicSchool.students[name][2]}")

    def print_students_data(self):
        for key in MusicSchool.students:
            self.print_student(key)

    def add_student(self, name, data):
        if isinstance(data, list):
            MusicSchool.students[name] = data
        else:
            print("Add a student in the correct format")

high_school_musical = MusicSchool(8, 15000)
high_school_musical.print_students_data()
high_school_musical.print_student("Gino")
high_school_musical.add_student("Jack", [60, "562-234-234", ["Piano"]])
high_school_musical.print_students_data()