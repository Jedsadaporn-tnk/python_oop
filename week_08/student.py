class STUDENT:
    def __init__(self, student_name, student_id, student_age):
        self.name = student_name
        self.id = student_id
        self.age = student_age
        self.grade = {}
    
    def modify(self):
     
        self.grade["MATCH"] = int(input('ใส่คะแนนคณิตศาสตร์ : '))
        self.grade["THAI"] = int(input('ใส่คะแนนภาษาไทย : '))
        self.grade["ENGLISH"] = int(input('ใส่คะแนนภาษาอังกฤษ : '))
        self.grade["SCIENCE"] = int(input('ใส่คะแนนวิชาวิทยาศาสตร์ : '))
        self.grade["SOCIAL STUDIES"] = int(input('ใส่คะแนนวิชาสังคมศึกษา : '))
    
    def Grade(self):
  
        for subject, score in self.grade.items():
            if score >= 80:
                grade = 4
            elif score >= 70:
                grade = 3
            elif score >= 60:
                grade = 2
            elif score >= 50:
                grade = 1
            else:
                grade = 0
            
       
            print(f'{subject}: ได้เกรด {grade}')
            

std1 = STUDENT('jed', 647525, 18)
std2 = STUDENT('MAN', 6475755, 19)

student = [std1, std2]


for i in student:
    i.modify()  
    print(f'Name: {i.name} ID: {i.id} Age: {i.age}')
    i.Grade() 
