class Welcome:
     
    # A sample method
    def greeting(self):
        print("Hello")
 
# Driver code
obj = Welcome()
obj.greeting()


class Student:
    def __init__(self,name): 
        self.stream = "CSE"
        self.name = name
    def getDetails(self):
        return "Stream : " + self.stream +" Name : "+self.name
Student1 = Student("abc")
print(Student1.getDetails())

class Grades(Student):
    def __init__(self):
        super(Grades,self).__init__("abcd")
        print("Creating grade sheet")
        self.semester = 4
    def setGrade(self,grade):
        self.grade = grade
        print("grade is set")
    def printGradeSheet(self):
        return "Student Name : "+self.name + " Grade : "+self.grade

Grade1 = Grades()
Grade1.setGrade("A")
print(Grade1.printGradeSheet())