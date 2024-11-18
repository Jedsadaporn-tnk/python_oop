import ex2funtion
sumplus = 0
summinus = 0
while True:
    INPUT = int(input('ใส่ตัวเลข : '))
    result  = ex2funtion.irainee(INPUT,sumplus,summinus)
    if INPUT > 0:
        result   = sumplus
        INPUT+=sumplus
        print(sumplus)
    elif INPUT < 0:
        result   = summinus
        INPUT+=summinus
        print(summinus)
    else:
       break

print(f'ผลลัพธ์ของผลบวก {sumplus}ผลลัพธ์ของผลลบ {summinus}')
##ผิดครับทำไม่ถูกแล้ว