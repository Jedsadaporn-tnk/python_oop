class STUDeNT:
    def __init__(self,std_id,std_name,std_age):
        self.id = std_id
        self.name = std_name
        self.age = std_age
        self.grade ={}
    def edit(self):
        self.grade['match']=int(input('ใส่เกรดคณิต'))
        self.grade['thai']=int(input('ใส่เกรดไทย'))
        self.grade['eng']=int(input('ใส่เกรดอัง'))
        self.grade['sci']=int(input('ใส่เกรดวิท'))
        self.grade['ss']=int(input('ใส่เกรดสังคม'))
        print(self.grade)
    def avg(self):
        return sum(self.grade.values())/len(self.grade)
std1 = STUDeNT('jed',7547,18)
std1.edit()
print(std1.name,std1.id,std1.age)
print(std1.avg())