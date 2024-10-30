print("โปรแกรมตัดเกรด")
score = int(input("กรุณาใส่คะแนน: "))
if score > 100:
    print("ไชย์นรงอย่ากวนตีน")
elif score >= 80:
    print("คุณได้เกรด 4 ")
elif score >=70:
    print("คุณได้เกรด 3")
elif score >= 60:
    print("คุณได้เกรด 2")
elif score >= 50:
    print("คุณได้เกรด 1")
elif score < 0:
    print("ไชย์นรงอย่ากวนตีน")
elif score < 50:
    print("คุณได้เกรด 0")
    print("อีแก้ 0 บ่")
    choice = str(input("แก้พิม Y ไม่พิม N   "))
    if choice == "Y":
        print(f"สอบแก้ต้องใช้อีก {50-score} ถึงจะผ่าน")
    elif choice == "N":
        print("ตกเหมือนเดิมไอ้โบ๋")
else :
    print("ไชย์นรงอย่ากวนตีน")