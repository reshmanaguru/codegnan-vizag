class person:
    university_name = "codegnan university"
    def __init__(self,name,age,dept,dept_id,mobile,education,gender):
        self.name = name
        self.age = age
        self.dept = dept
        self.dept_id = dept_id
        self.mobile = mobile
        self.education = education
        self.gender = gender
        
    def display_info(self):
        pass
    
class student(person):
    student_count = 0
    def __init__(self,name,age,student_id,dept,dept_id,mobile,education,year,gender,course):
        super().__init__(name,age,dept,dept_id,mobile,education,gender)
        self.student_id = student_id
        self.year = year
        self.course = course
        student.student_count +=1
    def display(self):
        print(f"Name:{self.name} \nage:{self.age} \nstudent_ID:{self.student_id} \ndept:{self.dept} \ndept_id:{self.dept_id} \nmobile:{self.mobile} \neducation:{self.education} \nyear:{self.year} \ngender:{self.gender}\ncourse:{self.course}")

class faculty(person):
    faculty_count = 0
    def __init__(self,name,age,exp,dept,dept_id,mobile,education,fac_id,sub,gender):
        super().__init__(name,age,dept,dept_id,mobile,education,gender)
        self.exp = exp
        self.fac_id = fac_id
        self.sub = sub
    def display(self):
        print(f"Name:{self.name} \nage:{self.age} \nexp:{self.exp} \ndept:{self.dept} \ndept_id:{self.dept_id} \nmobile:{self.mobile} \neducation:{self.education} \nfac_id:{self.fac_id} \nsub:{self.sub} \ngender:{self.gender}")
obj=student("Reshma",21,22610447,"ece",3,6305758224,"btech",2022,"female","ece")
("Student Details")
obj.display()
obj1=faculty("Nitya",30,7,"ece",390920090,5678907899,"ph.d",3509,"PYTHON","Female")
obj1.display()











        
