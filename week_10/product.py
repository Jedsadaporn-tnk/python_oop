class Product:
    def __init__(self,name,stock):
        self.name = name
        self.__price = []
        self.__stock = stock
    def add(self):
        self.__stock += instock
    def dis(self):
        self.__stock -= instock
    def edit(self):
        inprice = int(input('กรอกราคาสินค้า'))
        self.__price.append(inprice)
    def detail(self):
        return (f'(มีราคา {self.__price} บาท จำนวน {self.__stock} ชิ้น)')

st1 = Product('dildo',0)

while True:   
    choiec = input('กรุณาเลือกฟังชั่นถ้าต้องการเพิ่มพิมคำว่า add ถ้าจะลดจำนวนให้พิม dis ถ้าจะเช็คสินค้าพิมว่า check ถ้าต้องการแก้ไขราคาพิมว่า edit ออกพิมคำว่า exit :')
    if choiec == 'add':
        instock = int(input('ใส่จำนวนที่ต้องการเพิ่ม : '))
        st1.add()
    elif choiec == 'dis':
        instock = int(input('ใส่จำนวนที่ต้องการเพิ่ม : '))
        st1.dis()
    elif choiec == 'check':
        print(f'รายการสินค้า{st1.name}มีรายละเอียดดังนี้{st1.detail()}')
    elif choiec =='edit':
        st1.edit()
    elif choiec == 'exit':
        break
print(f'รายการสินค้า{st1.name}มีรายละเอียดดังนี้{st1.detail()}')
