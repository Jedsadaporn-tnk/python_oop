average = []
innum = int(input('ต้องการป้อนทั้งหมดกี่ตัว: '))
for i in range (1,innum+1):
    num = int(input(f'ใส่ตัวที่ {i}: '))
    average.append(num)
print(f'ค่าเฉลี่ยของ {average} = {sum(average)/len(average)}')