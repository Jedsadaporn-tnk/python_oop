resume = {'name':'','no':int,'hobby':'','color':''}
allpe = int(input('จำนวนคนที่จะป้อน: '))
for i in range (allpe):
    name = str(input(f'กรอกชื่อเล่น : '))
    resume['name']=name
    no = int(input(f'กรอกเลขที่ : '))
    resume['no']=no
    hobby = str(input(f'กรอกงานอดิเรก : '))
    resume['hobby']=hobby
    color = str(input(f'กรอกสีที่ชอบ : '))
    resume['color']=color
    print(resume)