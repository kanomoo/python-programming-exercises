from operator import length_hint

from numpy.ma.extras import average
from pandas.core.computation.ops import isnumeric


def s1():
    global i, n
    print("===5===")
    score = 50
    if score >= 50:
        print("Your Pass")

    print("\n===6===")
    score = 1
    if score >=50:
        print("Your Pass")
    else:
        print("Your Fail") # fail

    print("\n===7===")
    score = 60
    if score >= 50:
        print("Pass")

    score = 40
    if score >= 50:
        print("pass")

    name = 'Somchai'
    if name == 'somchai': # s ตัวเล็ก
        print('Your name is somchai')

    if name == 'Somchai': # s ตัวใหญ่
        print('Your name is Somchai')

    print("\n===8===")
    score = 60    # แบบปกติ
    if score >= 50:
        print("You Pass")
    else:
        print("You Fail")

    score = 60   # แบบย่ออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออ
    if score >= 50: print("You Pass")
    else: print("You Fail")

    print("\n===9===")
    print("True") if (10 < 20) else print("False") #ใช้ if-else แบบจบในหนึ่งบรรทัดได้ เรียกเทคนิคนี้ว่า Ternary Operators หรือ Conditional Expressinons ให้พิมพร์คำสั่ง ต่อไปนี้ใน shell
    print("True") if (10 > 20) else print("False")

    a = 30
    b = 30
    print("a == b") if a == b else print("a > b") if a > b else print("a < b") #if-else บรรทัดเดียว Ternary Operators

    print("\n===15===")
    A = 0
    if A == 0:
        print("Zero")
    elif A > 0:
        print("Grater than")
    else:
        print("Less than")

    print("\n===16===")
    value = 4
    if value == 1:
        print("One")
    elif value == 2:
        print("Two")
    elif value == 3:
        print('Three')
    elif value == 4:
        print("Four")
    elif value == 5:
        print("Five")

    print("\n===20===")
    d = 3
    match d: #คือ switch case ของ python
        case 0:
            print('0')
        case 1:
            print('1')
        case 2:
            print('2')
        case _ :        # case _ หมายถึง default case หรือ จับทุกกรณีที่เหลือ (catch-all)
            print('other')

    ch = 'A'

    match ch:
        case 'A':
            print('A')
        case 'B':
            print('B')
        case 'C':
            print('C')
        case _ :
            print('other')

    print("\n===26===")
    for n in range(5): # range = 4 (0 - 4)
        print(n)

    print()

    R = range(5)
    for n in R: # range = 4 (0 - 4) แต่กำหนด R ก่อน
        print(n)

    print("\n===27===")
    for n in range(1,6):  #range = 5 (1 - 5)
        print(n)

    print()

    for n in range(10, 20, 2): # range 18 (10 - 18) เพิ่มค่าทีละ 2 ไม่ถึง 20 เพราะถึง 20 แล้วหยุด
        print(n)

    print()

    for n in range(15, 1, -3): # range 3 (15 - 3) ลบค่าทีละ 3
        print(n)

    print()

    print("\n===28===")
    S = "Python"
    for c in S: # สามารถใช้ for วนรอบข้อมูลแบบลำดับ string tuple list
        print(c)

    print()

    Num = "12345"
    Sum = 0
    for n in Num: # วนรอบ "12345"
        Sum += int(n) # เพิ่มค่า Sum ตามค่า n ในแต่ละรอบ
        print(Sum)

    print("\n===29===")
    # Num = int(input("Enter number : "))                                    ใช้
    #
    # for n in range(1, Num+1): # วนรอบ Num+1 (จะได้วนรอบตามจำนวน  Num ที่กรอกเช่น 17 ถ้าไม่ + 1 จะวนรอบ 16 รอบ)
    #     if n % 2 == 0: # (% หารใช้เศษหรือหารเอาเศษ) ถ้า n %หารเอาเศษจาก 2 ==และเท่ากับ 0 (เป็นการหาจำนนวคู่ คี่)
    #         print(f"{n} is even number") #เลขคู่
    #     else:
    #         print(f"{n} is odd number") #เลขคี่

    #ทำไว้ดูใน terminal ง่ายๆ  ไปดูด้านบน
    for n in range(1, 16):
        if n % 2 == 0:
            print(f"{n} is even number")
        else:
            print(f"{n} is odd number")

    print("\n===31===")
    # total = 0.0
    # Max = 6
    # for n in range(1,Max): # วน 5 รอบ
    #     score = float(input(f"Enter Score #{n} : ")) # เก็บเป็น float ใช้ตอนโชวร์ total จะมีทศนิยม       inputตอนนี้เพื่อเก็บค่าเรื่อยๆ     {n} แสดง รอบ
    #     total = total + score #เก็บค่า score ใน total เพราะ total + socre เมื่อเปลี่นรอบ total จะเก็บรอบที่แล้ว บวกกับ score รอบใหม่ (total += score ย่อดีกว่า)
    # print()
    # print("Total score value : ", total)
    # print("Average score : ", total / 5) # หาร 5 หาค่าเฉลี่ย

    # ทำไว้ดูใน terminal ง่ายๆ  ไปดูด้านบน
    total = 0
    n2 = 0
    f = 0
    t = [80, 23, 67, 49, 77]

    for i in t:
        n2 += 1
        print(f"Enter score #{n2} : {t[f]}")
        total += int(t[f])
        f += 1
    print()
    print("Total score value : ", float(total))
    print("Average score : ", average(t))


    print("\n===33===")
    # total = 0
    # Max = int(input("Enter number of score : ")) #กำหนดรอบ
    # for n in range(1, Max+1):
    #     score = float(input(f"Enter Score #{n} : ")) # กรอก score
    #     total = total + score                        # เก็บค่า score เรื่อยๆ
    # print()
    # print("Total score value : ", total)
    # print("Average score : ", format(total / Max, ".2f")) # total / max หาค่าเฉลี่ย    ใช้ format .2f เพื่อดูง่ายๆ

    # ทำไว้ดูใน terminal ง่ายๆ  ไปดูด้านบน
    n3 = 0
    n4 = 0
    total2 = 0
    t1 = [36, 57, 78, 66, 98, 70, 45, 69]
    print(f"Enter number of score : 8")
    for i in t1:
        n3 += 1
        print(f"Enter Score #{n3} :{t1[n4]}")
        total2 += int(t1[n4])
        n4 += 1
    print("\nTotal Score value : ", float(total2))
    print("Average score : %.2f" %average(t1) )

    print("\n===36===")
    n = 1
    while n < 5: # while เป็นการวนรอบจนกว่าเงื่อนไขจะเป็นจริง
        print(n)
        n = n + 1

    print("\n===37===")

    # s = ""
    # while s != "0": # ในขณะที่ s ไม่เท่ากับ 0 ให้วนไปเรื่อยๆๆ
    #     s = input("Enter number : ")

    # ทำไว้ดูใน terminal ง่ายๆ  ไปดูด้านบน
    l = [349, 2449, 1133, 9373, 0]
    n = 0
    s = ""
    while s != "0":
        s = str(l[n])
        print(f"Enter number : {l[n]}")
        n += 1

    print("\n===38===")

    # Message = "" #สร้างตัวแปร Message
    # Max = 5 # กำหนดรอบ 5
    # Count = 1 #สร้างตัวแปรนับจำนวน
    # while Count <= Max: #ในขณะที่ Count น้อยกว่าหรือเท่ากับ Max
    #     S = input(f"Enter string #{Count}: ") #input string
    #     Message += S + "\n" #เก็บข้อมูล S แบบ string และขึ้นบรรทัดใหม่
    #     Count += 1 # เพิ่มค่า count 1
    # print("\nPrint your string enter : ")
    # print(Message)

    # ทำไว้ดูใน terminal ง่ายๆ  ไปดูด้านบน
    Message = ""
    Max = 5
    Count = 1
    l = ["Phone", "Python", "String", "Date", "Maximum"]
    n = 0
    while Count <= Max:
        print(f"Enter string #{Count}: {l[n]}")
        Count += 1
        Message += f"{l[n]}\n"
        n += 1
    print("\nPrint your string enter : ")
    print(Message)

    print("\n===40===")
    # Total = 0.0
    # Score = ""
    # Count = 0
    # while Score != "-1": #ในขณะที่ -1
    #     Score = input(f"Enter score value #{Count+1}: ")
    #     if Score != "-1": #ถ้า score ไม่เท่ากับ -1
    #         Count += 1
    #         Total += float(Score)
    #
    # print()
    # print("Number of Score : ", Count)
    # print("Total Score value : ", Total)
    # print("Average Score : ", Total / Count)

    # ทำไว้ดูใน terminal ง่ายๆ  ไปดูด้านบน
    count = 0
    total = 0
    l = [45, 78, 50, 38, 58, 78, -1]
    while score != -1:
        print(f"Enter score value #{count+1} : {l[count]}")
        score = l[count]
        if score != -1:
            total += int(l[count])
            count += 1
    print(f"\nNumber of Score : {count}")
    print(f"Total Score value : {total}")
    print(f"Average Score : {total / count}")

    print("\n===42===")
    # Done = True
    # Count = 0
    # while Done:
    #     Score = input(f"Enter score value #{Count+1}: ")
    #     if Score != "-1":
    #         Mark = float(Score)
    #         if Mark >= 0 and Mark <= 100:
    #             Grade = ""
    #             if Mark >= 80:
    #                 Grade = "A"
    #             elif Mark >= 70:
    #                 Grade = "B"
    #             elif Mark >= 60:
    #                 Grade = "C"
    #             elif Mark >= 50:
    #                 Grade = "D"
    #             else:
    #                 Grade = "F"
    #             print(f"Score is {Mark}, get {Grade}")
    #             Count += 1
    #         else:
    #             print("Score out of range, input again.")
    #     elif Score == "-1":
    #         Done = False
    # print("Exit Program")

    #เอาไว้ show ใน terminal เฉยๆ
    score = [56,89,34,66,77,88,45,54,-1]
    count = 0
    while True:
        if score[count] >= 80 and score[count] <= 100:
            grade = "A"
        elif score[count] >= 70:
            grade = "B"
        elif score[count] >= 60:
            grade = "C"
        elif score[count] >= 50:
            grade = "D"
        else:
            grade = "F"
        print(f"Enter score value #{count + 1}: {score[count]}")
        if score[count] != -1:
            print(f"Score is {float(score[count])}, get {grade}")
        if score[count] == -1:
            print("Exit Program")
            break
        count += 1

    print("\n===45===")
    s = 45
    if s >= 50:
        print('You Pass')
    else:
        pass # เป็นคำสั่งให้ผ่านไป ไม่ทำงานอะไรเลย

    print("\n===46===")
    for n in range(1, 10):
        if n == 6:
            break # เป็นคำสั่งเพื่อให้สิ้นสุดการทำงานในลูป
        print(n)

    print("\n===47===")
    for n in range(1, 10):
        if n == 4 or n == 8:
            continue # เป็นคำสั่งเพื่อให้ข้ามการทำงานในรอบนั้นๆ
        print(n)


def ex():
    P = 0
    for i in range (1,100+1) :
        P = i + P # บวก I กับบวก P ตัวมันเอง
        print(P, 'x', i, '=', P)
    print((101/2)*100)

def loop():
    m = 5
    for n in range (1,101) :
        print(n, 'x', m, '=', n*m)

def loop2():
    m = 5
    n = 12
    while n != "12":
        print() #print ไปเรื่อยๆ

def Min1():
    num1 = int(input("Enter value number1 : "))
    num2 = int(input("Enter value number2 : "))
    num3 = int(input("Enter value number3 : "))
    Min = 100
    if Min > num1:
        Min = num1
    if Min > num2:
        Min = num2
    if Min > num3:
        Min = num3
    print("\nMinimum number of %d,%d,%d = %d" % (num1, num2, num3, Min))


def w1():
    # s = input("Enter string : ") #string
    # s_len = len(s) #หาความยาว (length) หรือ จำนวนสมาชิก
    #
    # if s_len > 10:
    #     print("Your string length : %d" %s_len) # %d ใช้กับจำนวนเต็ม (int)  ใช้ร่วมกับ %และตัวแปรด้านหลัง %s_len
    #
    # print("Your string enter is %s" %s) # %s ใช้กับข้อความ (string) ใช้ร่วมกับ %และตัวแปรด้านหลัง %s

    s = input("Enter String : ")
    s_len = len(s)
    if s_len >= 10:
        print("Your string length : %d" %s_len)
    print("Your string enter is %s" %s)

def w2():
    # num1 = int(input("Enter number 1 : "))
    # num2 = int(input("Enter number 2 : "))
    # num3 = int(input("Enter number 3 : "))
    # Max = 0
    # if Max < num1: # Max น้อยกว่า num1
    #     Max = num1   # Max = num1
    # if Max < num2: # Max น้อยกว่า num2
    #     Max = num2   # Max = num2
    # if Max < num3: # Max น้อยกว่า num3
    #     Max = num3   # Max = num3
    #
    # print("\nMaximum number of %d, %d, %d = %d"%(num1,num2,num3,Max)) #%d ใช้กับจำนวนเต็ม (int)  ใช้ร่วมกับ %และตัวแปรด้านหลังใช้ได้หลายตัว

    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    num3 = int(input("Enter number 3 : "))
    Max = 0
    if Max < num1:
        Max = num1
    if Max < num2:
        Max = num2
    if Max < num3:
        Max = num3
    print("\nMaxinum number of %d, %d, %d = %d"%(num1,num2,num3,Max))

def w3():
    # s = input("Enter number : ")
    #
    # if s.isnumeric():  # .isnumeric() ใน Python ใช้สำหรับ ตรวจสอบว่า string(s) นั้นเป็นตัวเลขทั้งหมดหรือไม่ ทั้ง เลขไทย เลขโรมัน
    #     print("Your string is numeric.")
    #     print("Numeric Value is %d" %int(s)) #%d ใช้กับจำนวนเต็ม (int)
    #
    # else:
    #     print("your string is string." )

    s = input("Enter number : ")
    if s.isnumeric():
        print("Your string is numeric.")
        print("Numeric value is %d" %int(s))
    else:
        print("Your string is string")

def w4():
    # num1 = int(input("Enter number 1 : "))
    # num2 = int(input("Enter number 2 : "))
    # num3 = int(input("Enter number 3 : "))
    # Max = 0
    # if num1 > num2:       # ถ้า num1 มากกว่า num2
    #     if num1 > num3:       # ถ้า num1 มากกว่า num3
    #         Max = num1            # Max = num1
    #     else:
    #         Max = num3            # Max = num3
    #
    # else:
    #     if num2 > num3:   # ถ้า num2 มากกว่า num3
    #         Max = num2        #Max = num2
    #     else:
    #         Max = num3        #Max = num3
    # print(f"Maximum number of {num1}, {num2}, {num3} = {Max}")

    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    num3 = int(input("Enter number 3 : "))
    Max = 0
    if num1 > num2:
        if num2 > num3:
            Max = num1
        else:
            Max = num3
    else:
        if num2 > num3:
            Max = num2
        else:
            Max = num3
    print(f"Maximum number of {num1}, {num2}, {num3} = {Max}")

def w5():
    # num = int(input("Enter your score : "))
    # if num > 101:
    #     print("Score not in range.")
    # elif num > 79:
    #     print("Score value "+ str(int(num)) + " , " + "got grade A" )
    # elif num > 69:
    #     print("Score value "+ str(int(num)) + " , " + "got grade B" )
    # elif num > 59:
    #     print("Score value "+ str(int(num)) + " , " + "got grade C" )
    # elif num > 49:
    #     print("Score value "+ str(int(num)) + " , " + "got grade D" )
    # elif num < 50:
    #     print("Score value "+ str(int(num)) + " , " + "got grade F" )

    num = int(input("Enter score : "))
    if num > 100:
        print("Score not in range.")
    elif num >= 80:
        print(f"Score value {num}, got grade A")
    elif num >= 70:
        print(f"Score value {num}, got grade B")
    elif num >= 60:
        print(f"Score value {num}, got grade C")
    elif num >= 50:
        print(f"Score value {num}, got grade D")
    elif num >= 0:
        print(f"Score value {num}, got grade F")
    else:
        print("Score not in range.")

def w6():
    print("Show Menu\n============")
    print("1. Menu 1\n2. Menu 2\n3. Menu 3\n4. Exit")
    choice = input("Enter choice : ")
    match choice:
        case '1':
            print("Choose 1")
        case '2':
            print("Choose 2")
        case '3':
            print("Choose 3")
        case '4':
            print("Choose Exit")
        case _ :    # case _ หมายถึง default case หรือ จับทุกกรณีที่เหลือ (catch-all)
            print("Error no choice")

def ex1():
    # print(">> Program Find Maximum Digit <<")
    # max = 0
    # done = True
    #
    # while done:
    #     num = input("Enter integer number (0-exit) : ")
    #     if int(num) == 0:
    #         print("Exit Program")
    #         done = False
    #
    #     elif int(num) > 0:
    #         for i in num:
    #             if int(i) > int(max):
    #                 max = i
    #         print("Maximum Digit of integer number", num, "= ", max)
    #         max = 0

    # while True:
    #     Max = 0
    #     num = input("Enter integer number (0-exit) : ")  # รับค่าเป็น str
    #     if int(num) == 0: #ถ้า int(num) == 0
    #         print("Exit Program")
    #         exit()
    #     elif int(num) > Max:            # ถ้า int(num) > Max(0)            1231 > 0
    #         for i in num:               # loop สำหรับ str(i) ใน str(num)   "1" in "1231"   "2" in "1231"  "3" in "1231"  "1" in "1231"
    #             if int(i) > int(Max):   # ถ้า int(i) > int( max 0 )        1 > 0           2 > 1          3 > 2          1 !> ไม่มากกว่า 3
    #                 Max = i             # max = i                         1 = 1           2 = 2          3 = 3          ไม่เกิดอะไรขึ้น
    #         print("Maximum Digit of integer number ", num, " = ", Max)

    # while True:
    #     num = input("Enter integer number (0-exit) : ")
    #     if int(num) == 0:
    #         print("Exit Program")
    #         exit()
    #     m = max(str(num))     #ใช้ max หาค่าเลขมากสุดจาก string ได้
    #     print(f"Maximum Digit of integer number {m}")

    # while True:
    #     m = 0
    #     num = input("Enter integer number (0-exit) : ")
    #     if int(num) > m:
    #         for i in num:
    #             if int(num) >= int(m):
    #                 m = i
    #     elif int(num) == 0:
    #         print("Exit Program")
    #         break
    #     print(f"Maximum Digit of integer number {num} = {m}")
    
    # print(">> Program Find Maximum Digit <<")
    # while True:
    #     integer = input("Enter integer number(0-exit) : ")
    #     Max = max(str(integer))
    #     print(f"Maximum Digit of integer number {integer} = {Max}")
    #     if integer == "0":
    #         print("Exit Program")
    #         exit()

    # print(">> Program Find Maximum Digit <<")
    # while True:
    #     Max = 0
    #     num = input(f"Enter integer number(0-exit)  : ")
    #     for i in str(num):
    #         if int(i) >= int(Max):
    #             Max = i
    #     if num == "0":
    #         print("Exit Program")
    #         break
    #     print(f"Maximum Digit of integer number {num} = {Max}")


    #ทำไว้ show ใน terminal เฉยๆ
    num = [893, 901, 72830, 13426882, 90642, 56190222644, 51234722431, 0]
    count = 0
    print(">> Program Find Maximum Digit <<")
    while True:
        print(f"Enter integer number(0-exit) : {num[count]}")
        Max = max(str(num[count]))
        if num[count] == 0:
            print("Exit Program")
            break
        print(f"Maximum Digit of integer number {num[count]} = {Max}")
        count += 1

def ex2():
    # en = ""
    # Max = 0
    # print(">> Program Find Maximum Value <<")
    # value = int(input("Enter number of value(>= 1) : "))
    # print(f"\nProgram get value {value} numbers.")
    # if value >= 1: # ถ้ามากกว่าเท่ากับ 1
    #     for i in range(1,value+1):
    #         num = input(f"Enter value Number #{i} : ")
    #         if int(num) >= Max: #ใช้หาค่าที่มากที่สุด
    #             Max = int(num)
    #         en += str(num) #สร้างตัวแปรที่ใช้เก็บค่าnumแต่เปลี่ยนเป็น str จะได้ต่อกันได้เลื่อยๆ
    #         if i != value: # ถ้า i ไม่เท่ากับ value หรือ รอบสุดท้าย
    #             en += "," # เพื่ม , ที่แยกเพื่อความสวยงาน
    #     print(f"Your enter number : {en}")
    #     print(f"Maximum value number is {Max}")
    #     print("Exit Program")
    # else:
    #     print("Value input not correct.\nExit Program") #ถ้าค่าไม่ถูกต้อง

    #ทำไว้ show ใน terminal
    value = 6
    num = [34, 22, 66, 22, 78, 33]
    Max = 0
    List = ""
    print(">> Program Find Maximum Value <<")
    print(f"Enter number of value (>= 1 : {value}")
    print(f"\nProgram get value {value} numbers.")
    if value >= 1:
        for i in range(1, value+1):
            print(f"Enter value Number #{i} : {num[i-1]}")
            if num[i-1] >= Max:
                Max = num[i-1]
            List += str(num[i-1])
            if i != value:
                List += ", "
        print(f"Your enter number : {List}")
        print(f"Maximum value number is {Max}")
        print("Exit Program")
    else:
        print("Value input not correct.\nValue input not correct.")

def ex3():
    count = 0
    print(">> Program Palindrome Number <<")
    num = input("Enter integer number : ")
    m = len(num)
    while count < m:
        if num[count] == num[m - 1]:
            print(f"Digit {num[count]} equal to Digit {num[m - 1]}")
        if num[count] != num[m - 1]:
            print(f"Digit {num[count]} not equal to Digit {num[m - 1]}")
            print(f"Your enter number : {num} is not Palindrome Number.\nExit Program")
            exit()
        count += 1
        m -= 1
    print(f"Your enter number : {num} is Palindrome Number.\nExit Program")

def ex4():
    # import random
    # rd = random.randint(1, 99)
    # num = 0
    # # print(rd)
    # print("=" * 20)
    # print("โปรแกรมเกมทายตัวเลข")
    # print("=" * 20)
    # while num != rd:
    #     num = int(input("ใส่ตัวเลขที่ต้องทาย : "))
    #     if num == rd:
    #         print(f"\nถูกต้องครับ, เลขที่สุ่มไว้คือ {rd}")
    #     elif num > rd:
    #         print(f"!  เลข  {num} มากเกินไป")
    #     elif num < rd:
    #         print(f"!  เลข  {num} น้อยเกินไป")

    # ทำไว้ show ใน terminal
    import random
    rd = random.randint(1, 99)
    rd = 94 ########
    count = 0
    num = [56, 78, 89, 95, 93, 94]
    print("=" * 20)
    print("โปรแกรมเกมทายตัวเลข")
    print("=" * 20)
    while True:
        print(f"ใส่ตัวเลขที่ต้องทาย {num[count]}")
        if num[count] == rd:
            print(f"\nถูกต้องครับ, เลขที่สุ่มไว้คือ {num[count]}")
            break
        elif num[count] > rd:
            print(f"!  เลข {num[count]} มากเกินไป")
        elif num[count] < rd:
            print(f"!  เลข {num[count]} น้อยเกินไป")
        count += 1

def ex5():
    # text = ""
    # print(">> Program Change Number to Text <<")
    # num = input("Enter integer number : ")
    # for i in str(num):
    #     if i == "1":
    #         text += "One "
    #     elif i == "2":
    #         text += "Two "
    #     elif i == "3":
    #         text += "Three "
    #     elif i == "4":
    #         text += "Four "
    #     elif i == "5":
    #         text += "Five "
    #     elif i == "6":
    #         text += "Six "
    #     elif i == "7":
    #         text += "Seven "
    #     elif i == "8":
    #         text += "Eight "
    #     elif i == "9":
    #         text += "Nine "
    #     elif i == "0":
    #         text += "Zero "
    # print(f"Number : {num}")
    # print(f"Text : {text}")
    # print("Exit Program")

    #ทำไว้ show ใน terminal
    text = ""
    num = 9753100
    print(">> Program Change Number to Text <<")
    print(f"Enter integer number : {num}")
    for i in str(num):
        if i == "1":
            text += "One "
        elif i == "2":
            text += "Two "
        elif i == "3":
            text += "Three "
        elif i == "4":
            text += "Four "
        elif i == "5":
            text += "Five "
        elif i == "6":
            text += "Six "
        elif i == "7":
            text += "Seven "
        elif i == "8":
            text += "Eight "
        elif i == "9":
            text += "Nine "
        elif i == "0":
            text += "Zero "
    print(f"Number : {num}")
    print(f"Text : {text}")
    print("Exit Program")

s1()
ex4()