class Krutanongtui:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
        self.grade = {}
    def grade(self):
        self.grade["Math"]=float(input('ใส่คะแนนคณิตศาสตร์'))
        self.grade["Thai"]=float(input('ใส่คะแนนภาษาไทย'))
        self.grade["Eng"]=float(input('ใส่คะแนนอิ้งๆ'))
        self.grade["Sci"]=float(input('ใส่คะแนนวิทพื้น'))
        self.grade["SS"]=float(input('ใส่คะแนนสังฆัง'))
        
    def grading(self,score):
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
        return grade
    
std1 = Krutanongtui('Tui',55578,2)

std1.grade()
