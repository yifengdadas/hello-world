
class Student:
    
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.__id = id
    def zwjs(self):
        print(f"姓名{self.name},年龄:{self.age}")
    def __printId(self):
        print(f"学号:{self.__id}")
    def printId(self):
        self.__printId()


class PrimarySchoolStudent(Student):
    def zwjs(self):
        print("我是小学生")
        super().zwjs()
class HighSchoolStudent(Student):
    def zwjs(self):
        print("我是高中生")
        super().zwjs()


student1 = Student("张三",20,"S12345")
student2 = PrimarySchoolStudent("李四",10,"P67890")
student3 = HighSchoolStudent("王五",16,"H54321")

student1.zwjs()
student1.printId()

student2.zwjs()
student2.printId()

student3.zwjs()                                    
student3.printId()