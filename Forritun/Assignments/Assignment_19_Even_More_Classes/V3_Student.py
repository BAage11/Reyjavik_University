# Write the class "Student". The class has the attributes student_id which is an integer and a list of 4 grades. The class has the following methods:
# A constructor that takes two parameters: the student‘s ID (an integer), the student's grades (as a list of strings). The constructor uses the parameters to initializes the attributes and convert the grades to a list of floats.
# You need to implement functionality so that a Student instance can be printed using the print() function. When printed the Student shoud be printed as follows:
#                Student ID: 173
#                Grades: [5.37, 4.65, 9.85, 10.00]
# you should override the < operator which checks whether an instance of the class is less than another instance of the class. The comparison is made using the average grade of the instances.

class Student():
  def __init__(self, student_id, the_list):
    self.student_id = int(student_id)
    self.list = [float(i) for i in the_list]  
    
  def __lt__(self, other):
    total_average_1 = (sum(self.list)) / (len(self.list)) 
    total_average_2 = (sum(other.list)) / (len(other.list)) 
    if total_average_1 < total_average_2:
      return True
    else:
      return False

  def __str__(self):
    return "Student ID: {}\nGrades: {}".format(self.student_id, self.list)



def main():
    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    john = Student(student_id, grades)

    student_id = input("Enter student ID: ")
    grades = input("Enter 4 grades seperated by a comma").split(",")
    alice = Student(student_id, grades)

    print("John's info")
    print(john)

    if (john < alice):
        print("John has a lower average grade than Alice")
    else:
        print("Alice has a lower average grade than John")

main()