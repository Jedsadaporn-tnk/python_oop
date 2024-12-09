class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
        self.grade = {}
    def score(self):
        choiec = input('กรุณาเลือกวิชาที่จะกรอกคะแนน \n มีวิชา \n Math \n Thai \n Eng \n Sci \n Ss \n :')
        score = int(input('ใส่คะแนน : '))
        grade = self.grader(score)
        if choiec == 'Math':
            self.grade['Math'] = grade
        elif choiec == 'Thai':
            self.grade['Thai'] = grade
        elif choiec == 'Eng':
            self.grade['Eng'] = grade
        elif choiec == 'Sci':
            self.grade['Sci'] = grade
        elif choiec == 'Ss':
            self.grade["ss"] == grade
    def grader(self,score):
        if score >= 80:
            return 4
        elif score >= 70:
            return 3
        elif score >= 60:
            return 2
        elif score >= 50:
            return 1
        else:
            return 0
                         
stu1 = Student('paint',3,19)
stu1.score()
print(stu1.grade)