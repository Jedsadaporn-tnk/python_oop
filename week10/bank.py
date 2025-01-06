class Bank:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.balance = balance
    def deposite(self,amount):
        if amount > 100:
            self.balance += amount
        else:
            print('ใส่ยอดเงิน100บาทขึ้นไป')
    def withdraw(self,amount):
        if amount > 100 and amount <= self.balance:
            self.balance -= amount
        else:
            print('ใส่ยอดเงิน100บาทขึ้นไป')

id1 = bank(1,'paint',5000)
id1.deposite(300)
print(f'ฝากเงินไป 300 บาท')
print(f'เงินของ {id1.name}มีอยู่ {id1.balance}')
id1.withdraw(1400)
print(f'ถอนเงินเงินไป 1400 บาท')
print(f'เงินของ {id1.name}มีอยู่ {id1.balance}')