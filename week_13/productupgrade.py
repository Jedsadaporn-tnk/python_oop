class Product:
    def __init__(self,name,stock,price):
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    def add (self):
        add = int(input('กรุณาเพิ่มจำนวนสินค้าที่ต้องการ : '))
        self.__stock += add
    def dis (self):
        dis = int(input('กรุณาลดจำนวนสินค้าที่ต้องการ : '))
        self.__stock -= dis
    def editpi(self):
        editpi = int(input('กรุณาแก้ไขราคาสินค้าที่ต้องการ : '))
        self.__price = editpi
    def editname(self):
        editname = str(input('กรุณาแก้ไขชื่อสินค้าที่คุณต้องการ : '))
        self.__name = editname
    def mairuu(self):
        while True:   
            choiec = input('กรุณาเลือกฟังชั่นถ้าต้องการเพิ่มพิม add ถ้าจะลดจำนวนให้พิม dis ถ้าจะเช็คสินค้าพิม check ถ้าต้องการแก้ไขราคาพิม editpi ถ้าต้องการแก้ไขชื่อพิม editname  ออกพิมคำว่า exit :')
            if choiec == 'add':
                self.add()
            elif choiec == 'dis':
                self.dis()
            elif choiec == 'check':
                print( f'ชื่อสินค้า {self.__name} มีสินค้าในกต็อค {self.__stock} ชิ้น ราคา {self.__price} บาท')
            elif choiec =='editpi':
                self.editpi()
            elif choiec =='editname':
                self.editname()
            elif choiec == 'exit':
                return f'ชื่อสินค้า {self.__name} มีสินค้าในกต็อค {self.__stock} ชิ้น ราคา {self.__price} บาท'
                
    def show(self):
        return f'ชื่อสินค้า {self.__name} มีสินค้าในกต็อค {self.__stock} ชิ้น ราคา {self.__price} บาท'
    
class Phone(Product):
    def __init__(self, name, stock, price,storage):
        super().__init__(name, stock, price)
        self.storage = storage
    def showphone(self):
        return f'{super().show()} ความจุ {self.storage}'
class Notebook(Product):
    def __init__(self, name, stock, price,screensize):
        super().__init__(name, stock, price)
        self.screensize = screensize
    def shownotebook(self):
        return f'{super().show()} ขนาดจอ {self.screensize}'
class Cloth(Product):
    def __init__(self, name, stock, price,size):
        super().__init__(name, stock, price)
        self.size = size
    def showcloth(self):
        return f'{super().show()} ขนาดชุด {self.size}'

product1 =Phone('iphone 15',8,56000,'512 GB')
product2 =Notebook('ROG Strix G17',4,10600,'16.5"')
product3 =Cloth('T-Shirt',14,360,'L')
print(product1.mairuu())
print(product2.mairuu())
print(product3.mairuu())