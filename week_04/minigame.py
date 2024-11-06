import random 
win = 0
lose = 0
draw = 0
while True:
    answer = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print('โปรแกรมเป่ายิ่งฉุบ')
    print(answer)
    print('เลือก ค้อน กรรไกร กระดาษ ออกเกม')
    
    playeranswer = str(input('คุณเลือก : '))
    if answer == playeranswer:
        draw+=1
        print('ผลลัพธ์คือ เสมอ')
        print(("---------------"))
    elif playeranswer == 'ค้อน' and answer == 'กระดาษ':
        lose+=1
        print("ผลลัพธ์คือ แพ้")
        print(("---------------"))
    elif playeranswer == 'กระดาษ' and answer == 'กรรไกร':
        lose+=1
        print("ผลลัพธ์คือ แพ้")
        print(("---------------"))
    elif playeranswer == 'กรรไกร' and answer == 'ค้อน':
        lose+=1
        print("ผลลัพธ์คือ แพ้")
        print(("---------------"))
    elif playeranswer == 'ออกเกม':
        break
    else:
        win +=1
        print("ผลลัพธ์คือ ชนะ")
        print(("---------------"))

print(f'ชนะทั้งหมด : {win}')
print(f'แพ้ทั้งหมด : {lose}')
print(f'เสมอทั้งหมด : {draw}')
print(f'สถิติทั้งหมด : {win+lose+draw}')     