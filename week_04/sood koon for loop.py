num = int(input("กรอกแม่สูตรคูณ : "))
for i in range(1,24+1,1):
    sum = i*num
    if sum/2 %2 != 0:
       print(f"{num} * {i} = {sum}")     