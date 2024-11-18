money = []
#money.append(20)
#money.insert(3,70)
#money.remove(100)
#money.pop(1)
#del money[1:3]
#print(sum(money))
#print(min(money))
#print(max(money))
#print(len(money))
while True:
        num = int(input('your money '))
        money.append(num)
        print(money)
        if num == 0:
            print(f"all money = {sum(money)}")
            break