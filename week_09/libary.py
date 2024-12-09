class Libary:
        def __init__(self):
            self.bname = []
        def add_book(self):
            while True:   
                choiec = input('กรุณาเลือกฟังชั่นถ้าต้องการเพิ่มพิมคำว่า add ถ้าจะออกพิมคำว่า exit :')
                if choiec == 'add':
                     bookname = str(input('ใส่ชื่อหนังสือ : '))
                     self.bname.append(bookname)
                elif choiec == 'exit':
                 break
        def show_book(self):
                print(self.bname)
        def serch_book(self):
            bookname = str(input('ใส่ชื่อ:'))
            i = 0
            for i in self.name:
                if bookname == i:
                    print(i)

                    
lib1 = Libary()
lib1.add_book()
lib1.show_book()
lib1.serch_book()
            