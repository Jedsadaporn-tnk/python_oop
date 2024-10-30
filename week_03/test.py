class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def showgrade(self):
        score = self.score
        if score >= 50:
            print(f"kun {self.name} pan gan shob")
        else :
            print(f"kun {self.name} mai pan kan shob")
    def showscore(self):
        print(f"kun {self.name} dai ka nan {self.score} ka nan")
student1 = Student("som chai",70)
student2 = Student("Som ying",49)

student1.showgrade()
student2.showgrade()
student2.showscore()