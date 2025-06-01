class Student:
    schoolName = "Bright Future Academy"
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def display_info(self):
        return f"Student: {self.name}, Roll No: {self.roll_no},School: {Student.schoolName}"
    
    @classmethod
    def change_school_name(cls,new_name):
        cls.change_school_name = new_name
        return f"School name changed to {cls.change_school_name}"
    
    @staticmethod
    def calculate_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        else:
            return 'D'
        


student1 =  Student("Naveen",123)
print(student1.change_school_name("GLA"))
print(student1.display_info())