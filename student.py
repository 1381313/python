class daneshjo:
    def __init__(self, name, age, national_number, student_number):
        self.name = name
        self.age = age
        self.national_number = national_number
        self.student_number = student_number
    
    def get_first_name(self):
        return "Name: " + self.name
    
    def get_age(self):
        return self.name + " is " + str(self.age) + " years old"
    
    
    def get_national_number(self):  
        return self.name + "'s national number is " + str(self.national_number)


student_1 = daneshjo('amiri', 22, 2121040709020, 187070115 )
student_2 = daneshjo('shms', 23, 2121040709035, 3750621802)
student_3 = daneshjo('parsa', 22, 2121040709029, 375061140)


print(student_1.get_first_name())
print(student_1.get_age())
print(student_1.get_national_number())