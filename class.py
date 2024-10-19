class University_Management:
    def __init__(self , university_name):
        self.university_name = university_name
    def greetings(self):
        print(f"Hello! Welcome to {self.university_name}.")
class Person(University_Management):
    def __init__(self,name,age,university_name):
        super().__init__(university_name)
        self.name = name
        self.age =  age
    def ask(self):
        print(f"Your Name is {self.name} and your age is {self.age} and your University is {self.university_name}")
        
class Student(Person , University_Management):
    def __init__(self,name,age , university_name):
        super().__init__(name,age,university_name)
        
    def ask_student(self):
            print(f"welcome {self.name} to the {self.university_name} ")
    def input(self):
            self.ask_stu = input(
            '''What is your Department name ? \n 
Computer Science , DVM , Arts and Technology , Engineering \n 
Choose one of the following!''')
            print(f"Welcome to {self.university_name}, {self.ask_stu.upper()} Department")
            self.ask_stu1 = input("Are you a Morning or Evening Student?  ")
            self.morning = "Your Lecture Timing is 9am to 12pm"
            self.evening = "Your Lecture Timing is 1pm to 4pm"
            if (self.ask_stu1.lower() == 'morning student'):
              if self.ask_stu.lower() == 'computer science':
                print(f"{self.name} Your Coordinator is Sir Abdullah and {self.morning}  ")
              elif self.ask_stu.lower() == 'dvm':
                print(f"{self.name} Your Coordinator is Sir Ali and {self.morning} ")
              elif self.ask_stu.lower() == 'arts and technology':
                print(f"{self.name} Your Coordinator is Mam Uzma and {self.morning} ")
              elif self.ask_stu.lower() == 'engineering':
                print(f"{self.name} Your Coordinator is Mam Ammara and {self.morning} ")
              else:
                print("Plz Choose only given Department")
            else:
                if self.ask_stu.lower() == 'Computer Science':
                 print(f"{self.name} Your Coordinator is Sir Ahmad and {self.evening}  ")
                elif self.ask_stu.lower() == 'DVM':
                 print(f"{self.name} Your Coordinator is Sir Awais and {self.evening} ")
                elif self.ask_stu.lower() == 'Arts and Technology':
                 print(f"{self.name} Your Coordinator is Mam Malaika and {self.evening} ")
                elif self.ask_stu.lower() == 'Engineering':
                 print(f"{self.name} Your Coordinator is Mam Sidra and {self.evening} ")
                else:
                 print("Plz Choose only given Department")
                
                       
class Professor(Person , University_Management):
    def __init__(self,name,age , university_name):
        super().__init__(name,age,university_name)
    def ask_Professor(self):
        self.ask_Professor1 = input(
            '''Enter your degree in which you are specialized? \n
Computer Science, DVM, Arts and Technology, Engineering ''')
        print(f"Welcome Prof. {self.name} to the {self.university_name} , specializing in {self.ask_Professor1.upper()}")
        if self.ask_Professor1.lower() == 'Computer Science'.lower():
            print(f"Courses You will teach this week are: Math-305 , CS-409 , SE-401")
        elif self.ask_Professor1.lower() == 'DVM'.lower():
            print(f"Courses You will teach this week are: ANAT-02101 , VET-420 , VM-613")
        elif self.ask_Professor1.lower() == 'Engineering'.lower():
            print(f"Courses You will teach this week are: EE-101 , CS-106")
        elif self.ask_Professor1.lower() == 'Arts and Technology'.lower():
            print(f"Courses You will teach this week are: ATEC-4372 , ART-10")
        else:
                 print("Plz Choose only given Degree")
    
person_name = input("Enter your name? ")   
person_age = input("Enter your age? ")   
person_university = input("Enter your University name? ")   
student = University_Management("UAF")
student.greetings() 
student1 = Person(person_name, person_age ,person_university )
student1.ask()
ask_question = input("Are you a Student or Professor?  ")
if ask_question.lower() == 'student':
    print(f"welcome {person_name} to the {person_university} ")
    student2 = Student("Samra" , person_age , "UAF")
    student2.ask_student()
    student2.input()
elif ask_question.lower() == 'professor':
    print(f"welcome Prof: {person_name} to the {person_university} ")
    student3 = Professor(person_name ,person_age , person_university)
    student3.ask_Professor()
else:
    print("Invalid Answer! Plz enter either 'Student' or 'professor'")

# student2 = Departments()
# print(student2.department())