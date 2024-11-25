try:
    pay = int(input('ใส่ยอดซื้อ : '))
    if pay == 0:
        raise ZeroDivisionError
    if pay == '':
        raise ValueError
    if pay <0:
        raise Exception
    if pay >= 5000:
        print(f'ได้รับส่วนลด20% = {pay-pay*0.2}')
    elif pay >= 2000 and pay <= 4999:
        print(f'ได้รับส่วนลด10% = {pay-pay*0.1}')
    elif pay <2000:
        print(f'คุณไม่ได้รับส่วนลด')
except ValueError:
    print('ใส่แค่ตัวเลข')
except ZeroDivisionError:
    print('ห้ามใส่0')
except:
    print('ห้ามใส่ตัวติดลบ')