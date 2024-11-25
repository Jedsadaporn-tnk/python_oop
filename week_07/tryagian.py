sum = 0
while True:
    try:
        price = str(input('ใส่ราคาสินค้าหรือถ้าอยากออกให้พิม exit : '))
        if price =='exit':
            print(f'ราคาสินค้าทั้งหมด {sum}')
            break
        elif int(price) == 0:
            raise ZeroDivisionError
        elif int(price) <0:
            raise Exception
        else:
            sum += int(price) 
            print(sum)
    except ValueError:
        print('ใส่แค่ตัวเลข')
    except ZeroDivisionError:
        print('ห้ามใส่0')
    except:
        print('ห้ามใส่ตัวติดลบ')