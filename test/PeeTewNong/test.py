# print(">> Program Find Maximum Digit <<")
# while True:
#     Max = 0
#     num = input("Enter integer number(0-exit) : ")
#     if num == "0":
#         print("Exit Program")
#         break
#     for i in num:
#         if int(i) > Max: Max = int(i)
#     print(f"Maximum Digit of integer number {num} = {Max}")

# code ที่ไม่มีการ comment ใช้เฉพาะ while ทำไมไม่รู้
# print(">> Program Find Maximum Digit <<")
# while True:
#     Max = 0
#     number = int(input("Enter integer number(0-exit) : "))
#     num = number
#     if number == 0:
#         print("Exit Program")
#         break
#     while num > 0:
#         digit = num % 10
#         num //= 10
#         if digit > Max: Max = digit
#     print(f"Maximum Digit of integer number {number} = {Max}")


# print(">> Program Find Maximum Digit <<")
# while True: # วน loop เงื่อนไขคือ True คือไม่มีการหยุดถ้าไม่ใส่เงื่อนไข if ด้านใน
#     Max = 0 # สร้างตัวแปร Max เก็บค่าสูงสุด
#     number = int(input("Enter integer number(0-exit) : ")) # รับค่าเป็น int
#     num = number # สร้างตัวแปร num คือค่าเดียวกับ number แต่ num เป็นตัวแปรที่ถูกคำนวณการลดหลักไปเรื่อยๆเพื่อสะดวกในการแก้ไข ไม่งั้นจะไม่มีตัวแปรใช้ในการเช็คเงื่อนไขในการออก
#     if number == 0: # if เงือนไขในการออก loop while True คือถ้า number == 0 จะออก while
#         print("Exit Program")
#         break # คำสั่ง break คือการหยุด loop
#     while num > 0: # while นี้คือการหาค่าหลักหรือ digit (num % 10) และลดค่าทีละหลัก (num //= 10 หรือ num = num // 10)
#         digit = num % 10 # digit คือค่าหลักหน่วยของ num โดยใช้ % 10 คือการหารเอาเศษของ 10
#         num //= 10 # num //= 10 หรือ num = num // 10 คือการลดค่าทีละหลักของ num โดยใช้ // 10 คือการหาร 10 และตัดเศษทิ้ง หรือการตัดค่าหลักหน่วยออกไป
#         if digit > Max: Max = digit # if เช็ค5hk digit มากกว่าตัวแปร Max ให้ digit ใน loop นั้นเป็นตัวแปร Max แทน หรือ ค่าสูงสุด
#     print(f"Maximum Digit of integer number {number} = {Max}") # โชว์การแสดงผม


print(">> Program Find Maximum Value <<")
while True:
    output = "Your enter number : "
    numVal = int(input("Enter number of value(>= 1) : "))
    Max = 0
    if numVal <= 1:
        print("Value input not correct.\nExit Program")
        break
    print(f"\nProgram get value {numVal} numbers.")
    for i in range(1, numVal + 1):
        num = int(input(f"Enter value Number #{i} :"))
        if num > Max: Max = num
        output += f"{num}, " if i < numVal else f"{num}"
    print(output)
    print(f"Maximum value number is {Max}")
    print("Exit Program")
    break
    

