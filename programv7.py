import pandas as pd
import xlsxwriter


class students:
    list_of_students = []



    def __init__(self,id_student,name_student,age_student,password,monthly_payment,teacher):
        self._id = id_student
        self._name_student = name_student
        self._age_student = age_student
        self.__password = password
        self._monthly_payment = monthly_payment
        self.teacher = teacher
        self.list_of_students.append(self)

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name_student

    def get_age(self):
        return self._age_student


    def rate(self):
        return self._monthly_payment * 0.5
    
    @classmethod
    def create_dataframe(cls):
        data = []
        for students_obj in cls.list_of_students:
            students_data = {
                'id':students_obj.get_id(),
                'name':students_obj.get_name(),
                'age':students_obj.get_age(),
                'teacher':students_obj.teacher
                }
            data.append(students_data)

        df = pd.DataFrame(data)
        df.to_excel('data_students.xlsx', index =  False)
        print(df)

            
    
class students_of_it(students):
    def __init__(self,id_student,name_student,age_student,password,monthly_payment,teacher,duration_of_course,name_course,own_equipment):
        super().__init__(id_student,name_student,age_student,password,monthly_payment,teacher)
        self._duration_of_course = duration_of_course
        self._name_course =  name_course
        self._own_equipment =  own_equipment

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name_student
    
    def get_age(self):
        return self._age_student
    
    def get_duration(self):
        return self._duration_of_course
    
    def get_name_of_course(self):
        return self._name_course
    
    def get_own_equipment(self):
        return self._own_equipment

    def rate(self):
        if(self._own_equipment == True):
            return self._monthly_payment * 0.5 
        
        elif(self._own_equipment == False):
            c1 = self._monthly_payment * 0.9
            self._monthly_payment += c1
            return  self._monthly_payment
        
 
class students_of_cooking(students):
    def __init__(self,id_student,name_student,age_student,password,monthly_payment,teacher,works_in_the_kitchen):
        super().__init__(id_student,name_student,age_student,password,monthly_payment,teacher)
        self._works_in_the_kitchen = works_in_the_kitchen
 

    def rate(self):
        
        if(self._works_in_the_kitchen == True):
            self._monthly_payment -=  60
            return self._monthly_payment
        
        elif(self._works_in_the_kitchen == False):
            c2 = self._monthly_payment * 0.1
            self._monthly_payment += c2
            return  self._monthly_payment

class students_of_right(students):
    def __init__(self,id_student,name_student,age_student,password,monthly_payment,teacher,occupation_area):
            super().__init__(id_student,name_student,age_student,password,monthly_payment,teacher)
            self._occupation_area = occupation_area


class rate_control():
    def __init__(self,total_rate = 0 ):
        self._total_rate = total_rate

    def registre(self,students):
        self._total_rate += students.rate()

    @property
    def total_rate(self):
       return self._total_rate


student1 = students_of_it(1, "Alice", 20, 1234, 500, "John Doe", "4 years", "Computer Science", True)
student2 = students_of_it(2, "Bob", 22, 5678, 550, "Jane Smith", "3 years", "Information Technology", False)
student3 = students_of_it(3, "Charlie", 19, 9999, 480, "David Brown", "5 years", "Cybersecurity", True)
student4 = students_of_it(4, "David", 21, 1357, 510, "Emma Johnson", "4 years", "Software Engineering", False)
student5 = students_of_it(5, "Emma", 20, 2468, 520, "Michael Wilson", "3 years", "Data Science", True)
student6 = students_of_it(6, "Fiona", 23, 9876, 530, "Sophia Garcia", "4 years", "Network Administration", False)
student7 = students_of_it(7, "George", 24, 3333, 540, "Olivia Martinez", "5 years", "Web Development", True)
student8 = students_of_it(8, "Hannah", 19, 4444, 550, "Daniel Brown", "3 years", "Information Security", False)
student9 = students_of_it(9, "Isaac", 22, 8888, 560, "Emily Taylor", "4 years", "Database Management", True)
student10 = students_of_it(10, "Jack", 21, 7777, 570, "Natalie Clark", "5 years", "Artificial Intelligence", False)

student11 = students_of_right(11, "Alice", 20, 1234, 500, "John Doe", "Law")
student12 = students_of_right(12, "Bob", 22, 5678, 550, "Jane Smith", "Human Rights")
student13 = students_of_right(13, "Charlie", 19, 9999, 480, "David Brown", "Civil Law")
student14 = students_of_right(14, "David", 21, 1357, 510, "Emma Johnson", "International Law")
student15 = students_of_right(15, "Emma", 20, 2468, 520, "Michael Wilson", "Corporate Law")
student16 = students_of_right(16, "Fiona", 23, 9876, 530, "Sophia Garcia", "Environmental Law")
student17 = students_of_right(17, "George", 24, 3333, 540, "Olivia Martinez", "Tax Law")
student18 = students_of_right(18, "Hannah", 19, 4444, 550, "Daniel Brown", "Criminal Law")
student19 = students_of_right(19, "Isaac", 22, 8888, 560, "Emily Taylor", "Constitutional Law")
student20 = students_of_right(20, "Jack", 21, 7777, 570, "Natalie Clark", "Labor Law")

student21 = students_of_cooking(21, "Alice", 20, 1234, 500, "John Doe", True)
student22 = students_of_cooking(22, "Bob", 22, 5678, 550, "Jane Smith", False)
student23 = students_of_cooking(23, "Charlie", 19, 9999, 480, "David Brown", True)
student24 = students_of_cooking(24, "David", 21, 1357, 510, "Emma Johnson", False)
student25 = students_of_cooking(25, "Emma", 20, 2468, 520, "Michael Wilson", True)
student26 = students_of_cooking(26, "Fiona", 23, 9876, 530, "Sophia Garcia", False)
student27 = students_of_cooking(27, "George", 24, 3333, 540, "Olivia Martinez", True)
student28 = students_of_cooking(28, "Hannah", 19, 4444, 550, "Daniel Brown", False)
student29 = students_of_cooking(29, "Isaac", 22, 8888, 560, "Emily Taylor", True)
student30 = students_of_cooking(30, "Jack", 21, 7777, 570, "Natalie Clark", False)

control = rate_control()
control.registre(student1)
control.registre(student2)
control.registre(student3)
control.registre(student4)
control.registre(student5)
control.registre(student6)
print(control.total_rate)
#saida = 37710







    






    

      
        



