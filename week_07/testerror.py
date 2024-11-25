try:   
    num = int(input('maa koon : '))
    if num == 0:
        raise ZeroDivisionError
    for i in range(1,13,1):
        print(f'{num}*{i} = {num*i}')
except ZeroDivisionError:
    print('muneg sai soon')
except ValueError:
    print('sai dai kaa lek')