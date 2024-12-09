class Libary:
    def __init__(self):
        self.bookinfo = []
    def add_book(self):
        while True:
            option = str(input('เลือกoption เพิ่มพิมadd ออกพิม exit : '))
            if option == 'add':
                bookinfo={}
                bookinfo['name'] = str(input('ใส่ชื่อหนังสือ : '))
                bookinfo['writer'] = str(input('ใส่ชื่อคนแต่ง : '))
                bookinfo['page'] = str(input('ใส่จำนวนหน้า : '))
                bookinfo['price'] = str(input('ใส่ราคาหนังสือ : '))
                self.bookinfo.append(bookinfo)
            elif option == 'exit':
                break
    def show_book(self):
        i = 0
        for i in self.bookinfo:
            print(i)
    def find_book(self):
        bookinfo = str(input('ใส่ชื่อ:'))
        for i in self.bookinfo:
            if i['name'] == bookinfo:
                print(i)
bookinfo1 = Libary()
bookinfo1.add_book()
bookinfo1.show_book()
bookinfo1.find_book()