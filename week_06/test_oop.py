class Man:
    def __init__(self,ชื่อ,อายุ,เพศ,สี):
            self.name = ชื่อ
            self.age = อายุ
            self.gender = เพศ
            self.color = สี
    def old(self):
        self.age += 1
Man1 = Man(ชื่อ='ITUI',อายุ=2,เพศ='MAN',สี='BLACK')
Man2 = Man(ชื่อ='GUITAR',อายุ=20,เพศ='MAN',สี='White')
Man2.old()
print(Man2.age)