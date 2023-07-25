from School import School, Classroom , Subject
from Person import Student , Teacher


def main():
    school = School('Adam jee', 'Uttara')

    eight = Classroom('eight')
    school.add_classroom(eight)
    nine = Classroom('nine')
    school.add_classroom(nine)
    ten = Classroom('ten')
    school.add_classroom(ten)

    abul = Student('Abul Khan', eight)
    school.student_admission(abul)
    babul = Student('Babul Khan', eight)
    school.student_admission(babul)
    mokbul = Student('Mokbul Khan', eight)
    school.student_admission(mokbul)

    #subjects:
    physics_teacher = Teacher('Shahjahan Topon')
    physics = Subject('Physics',physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Hajari Nag')
    chemistry = Subject('Chemistry',chemistry_teacher)
    eight.add_subject(chemistry)

    biology_teacher = Teacher('Gaji Azmol')
    biology = Subject('Biology',biology_teacher)
    eight.add_subject(biology)

    eight.take_semester_final()

    print(school)
    

if __name__ == '__main__':
    main()