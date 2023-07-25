class Student:
    def __init__ (self, name , currentClass , id):
        self.name = name
        self.id = id
        self.currentClass = currentClass

    def __repr__ (self) -> str:
        return f'student name : {self.name} , class:{self.currentClass} , id:{self.id}'

class Teacher:
    def __init__(self , name , subject , id):
        self.name = name
        self.subject=subject
        self.id=id
    def __repr__ (self) -> str:
        return f'Teacher name : {self.name} , subject:{self.subject} , id:{self.id}'

class school:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name , subject):
        id = len(self.teachers) +101
        teacher = Teacher(name , subject , id)
        self.teachers.append(teacher)

    def enroll(self,name , fee ):
        if fee <6500:
            return 'not enough fee'
        else:
            id = len(self.students) +1
            student = Student(name, 'C' , id)
            self.students.append(student)
            return f'{name} is enrolled with id : {id} , extra money {fee - 6500}'
        
    def __repr__(self) -> str:
        print('welcome to ', self.name)
        print('------ OUR TEACHERS----- ')
        for teacher in self.teachers:
            print(teacher)

        print('----- our student------')
        for student in self.students:
            print(student)

        print('completed for now') 
       
# alia = Student('alia',9,32)
# print(alia)

# modhu = Teacher('modhu','math',452)
# print(modhu)

phitron = school('Phitron')
phitron.enroll('alia ', 5200)
phitron.enroll('rani ', 8000)
phitron.enroll('Oishi ', 7000)
phitron.enroll('vaijan ', 70000)

phitron.add_teacher('Tom Cruise ', ' algo')
phitron.add_teacher('Decap ', ' DSA')
phitron.add_teacher('Aj ', ' Database')

print(phitron)