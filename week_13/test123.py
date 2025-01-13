class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f'ชื่อ {self.name} อายุ {self.age} ปี มีสี{self.color}'
#animal1 =Animal('peter',10,'black')
#print(f'สัตว์ตัวหนึ่งมี{animal1.showinfo()}')
class Dog(Animal):
    def speak(self):
        return 'black black'
dog1 =Dog('peter',10,'black')
print(f'หมาชื่อ {dog1.name} ร้อง {dog1.speak()}')
print(f'สัตว์ตัวหนึ่งมี{dog1.showinfo()}')