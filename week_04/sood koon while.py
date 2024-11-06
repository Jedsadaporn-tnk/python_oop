num1 = int(input('กรอกแม่สูตรคูณ : '))
num2 = 1
while num1 <= 24:
    sum = num1*num2
    if sum/2 %2 != 0:
        print(f"{num1}*{num2}={sum}")     
    num2 +=1     