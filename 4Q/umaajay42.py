#4.2
#UMA AJAY KUMAR REDDY P S           19ETCS002134
class Student:
    def __init__(self, name, roll, s1, s2):
        self.name = name
        self.roll = roll
        self.s1 = s1
        self.s2 = s2
# Function to create and append students
    def accept(self, Name, Roll, score1, score2):
        obj = Student(Name, Roll, score1, score2)
        ls.append(obj)
# Display student details
    def display(self, obj):
        print("Name : ", obj.name)
        print("RollNo : ", obj.roll)
        print("Score1:", obj.s1)
        print("Score2 :", obj.s2)
        print("\n")
# Search Function
    def search(self, rn):
        for i in range(ls.__len__()):
            if (ls[i].roll == rn):
                return i
        print("unfortunately Student Not Found","\n")
        return -1
    def delete(self, rn):
        i = self.search(rn)
    # print(i)
    # if(i != -1)
        del ls[i]
    # Update Function
    def update(self, rn, No):
        i = self.search(rn)
        rolln = No
        ls[i].roll = rolln
ls = []
# Object of class
obj1 = Student('', 0, 0, 0)
print("\nOperations used, ")
print("\n1.Accept Student details\n"
         "2.Display Student Details\n"
          "3.Search Details of a Student\n"
          "4.Delete Details of Student"
         "\n5.Update Student Details\n6.Exit")
obj1.accept("Yadu", 1, 100, 100)
obj1.accept("Ajay", 2, 90, 90)
obj1.accept("harsha", 3, 80, 80)
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj1.display(ls[i])
print("\n")
s = obj1.search(2)
print("Student Found, ")
obj1.display(ls[s])
s = obj1.search(10)
obj1.delete(10)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj1.display(ls[i])
print("Thank You !")





