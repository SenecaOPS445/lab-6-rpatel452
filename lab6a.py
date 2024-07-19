#!/usr/bin/env python3
# Author ID: rpatel452

class Student:

    
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  
        self.courses = {}

    
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\nStudent Number: ' + self.number

    # Add a new course and grade to student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

   
    def displayGPA(self):
        try:
            gpa = sum(self.courses.values()) / len(self.courses)
        except ZeroDivisionError:
            gpa = 0.0
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses

if __name__ == '__main__':
    
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

   
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

  
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

  
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
