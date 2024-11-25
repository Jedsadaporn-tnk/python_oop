import random as r
class Student:
    def __init__(self,Name,Nickname,Score):
            self.name = Name
            self.nickname = Nickname
            self.score = Score
    def ex_score(self):
        a = r.randint(1,10)
        self.score += a
        
    def grade(self):
        if self.score >= 5:
            print('สอบผ่าน')
        else:
            print('สอบตก')

student1 = Student('jedsadaporn sutthiwatanakumjorn','paint',0)
student2 = Student('peerapat lukwhlan','tar',0)
student3 = Student('peerapat puttasaro','peem',0)
student4 = Student('karn yodsanit','ake',0)
student5 = Student('preede panomyong','preede',0)
student = [student1,student2,student3,student4,student5]
for i in student:
    i.ex_score()
    print(f'ชื่อจริง-นามสกุล : {i.name}ชื่อเล่น : {i.nickname}คะแนน : {i.score}')
    i.grade()