# a, b, c, d = True, False, True, False
# print( a and b or c or d)

# print( a and b and c or d)

# x = 20
# y = 5
# c = 2
# print(y / c % x //c )
# # 0 , 1 ,  0.0 ,  1.0

# x = 50
# y = 20
# print(y + x - x + y + y + y)

# x = 10
# y = 2
# print(x ** y // y /y % y)

# x = 22
# y = 21
# c = 20
# print("True" if x > y > c else "False")


# t = 0
# for i in range(12):
#     if i %2 == 0:
#         t += i
#     else:
#         t += 1
#     if i == 8: break
# print(t)

# name = "Python"

# print(name[1])
# print(name[-3])

# num = 10
# ac = 2
# if num > 20:
#     ac = num
#     num = ac
# elif ac > 2.5:
#     ac += 20
#     num += 50
# elif num < 11:
#     temp = num
#     ac = num
#     num = temp
# print(num,ac)

# print(bin(10))

# print(oct(55))

# print(hex(131))

# print(chr(67))

# for i in range(5):
#     print(" " * 5," " * (5-i),"*" * i,"*","*" * i,sep="")
# for i in range(5):
#     print(" " * i,"*" * ((5*2) - i),"*" * ((5*2) - i),sep="")
# for i in range(5):
#     print(" " * ((5-1)-i),"*" * ((5)-i),"  " * (i+1),"  " * (i),"*" * ((5)-i),sep="")

# print(chr(67))

# print(ord("A")+ord("E"))
# print(ord("A")+ord("B"))

# for i in range(5):
#     for i in range(3):
#         print(i)

# for i in range(5):
#     print(i)
#     if i == 4: break

# for i in range(5):
#     if i == 3: break
#     print(i)

# for i in "nama":
#     if i < "e": print(":",end="")
#     else: print(i,end="")

# for i in range(1,5):
#     for n in range(1,i+1):
#         print("=",end="")
#     print()

# for i in range(4):
#     for n in range(1,5):
#         print("=",end="")
#     print()

# for i in range(1, 4 + 1):
#     for j in range(1,i+1) :
#         print("=", end="")
#     print()

# for i in range(4):
#     for n in range(5,1,-1):
#         print("=",end="")
#     print()

# from random import randint
# for i in range(50):
#     print(randint(0,100))

# nums = [x for x in range(5) if x % 2 == 0]
# print(nums)

# num, result = int(input("Enter number : ")), ""
# while num >= 1:
#     num2 = num % 2
#     result += str(num2)
#     num = num // 2
# print(result[::-1])

# num,result = int(input("Enter number : ")), 0
# n = 0
# for i in str(num)[::-1]:
#     result += int(i) * (2 ** n)
#     n += 1
# print(result)




# num,result,result2 = int(input("Enter number : ")), "", ""
# while num >= 1:
#     num2 = num % 2
#     result += str(num2)
#     num = num // 2

# print(result[::-1])
# print(result2)




# while True:
#     name = input("Enter text(enter-exit) : ")
#     if name == "exit": break
#     elif name.isalpha(): print("Text is alphabetic")
#     elif name.isdigit(): print("Text is digit")
#     elif name.isalnum(): print("Text is alpha and numeric")
#     elif name.isspace(): print("")
#     elif name == "": print("")
#     elif type(name) == str: print("Text is string")


# from random import randint
# head = "        Main Menu        "
# line = len(head) * "="
# while True:
#     print(line,head,line," 1. Input number of subject (8)\n 2. Start Random Grade\n 3. Exit Program",line,sep="\n")
#     choice,ts = int(input("Select your Choice : ")), 0
#     match choice:
#         case 1:
#             num = int(input("Enter your number of subject : "))
#             input("Press any key to continue . . .")
#         case 2:
#             print("Start Random Score & Grade . . . .")
#             for i in range(num):
#                 score = randint(40,90)
#                 if score >= 80 and score <= 100: grade, point = "A", 4
#                 elif score >= 70: grade, point = "B", 3
#                 elif score >= 60: grade, point = "C", 2
#                 elif score >= 50: grade, point = "D", 1
#                 elif score >= 0: grade, point = "F", 0
#                 ts += point
#                 print(f"Your #{i+1} subject is {grade}")
#             print(f"\nYour Total GPA is : {ts / num}",line,sep="\n")
#             input("Press any key to continue . . . ")
#         case 3:
#             print("Exit Program . . .")
#             break
#     print()



# head = "        Drinks menu      "
# line, result, total, n = len(head) * "=", "", 0, 0
# while True:
#     print(line,head,line,sep="\n")
#     print(f"| {"0. Quit":22}|\n| {"1. Hot Coffee":22}|\n| {"2. Ice Coffee":22}|\n| {"3. Frappe Coffee":22}|\n| {"4. Caculate Cost":22}|",line,sep="\n")
#     choice = int(input("Select Item : "))
#     match choice:
#         case 0:
#             print("Exit Program...")
#             break
#         case 1:
#             hot = int(input("Hot Coffee, how many glasses : "))
#             result += f"{hot} {"Hot Coffee":15}30.00 {30*hot:6.2f}\n"
#             total += 30*hot
#         case 2:
#             ice = int(input("Ice Coffee, how many glasses : "))
#             result += f"{ice} {"Ice Coffee":15}35.00 {35 * ice:6.2f}\n"
#             total += 35 * ice
#         case 3:
#             frappe = int(input("Frappe Coffee, how many glasses : "))
#             result += f"{frappe} {"frappe Coffee":15}50.00 {50 * frappe:6.2f}\n"
#             total += 50 * frappe
#         case 4:
#             n += 1
#             print(f"\nOrder #{n}")
#             h = "Qty Item        Price   Total"
#             l = len(h) * "-"
#             print(l,h,l,result+l,f"Total: {total:.2f} Bath",sep="\n")
#             result = ""
#             total = 0
#         case _: print("No Choice")
#     print()

# num = int(input("num : "))
# print(bin(num)[2:])


# head = "::     Main Menu     ::"
# line, even, odd, Sum = len(head) * "=", 0, 0, 0
# while True:
#     print(line,head,line," A. Get Integer Number\n B. Summation of Digit\n C. Count Digit\n D. Exit",sep="\n")
#     choice = input("Enter choice : ")
#     match choice:
#         case "A" | "a":
#             num = input("\nEnter long number : ")
#         case "B" | "b":
#             for i in num:
#                 i = int(i)
#                 if i % 2 ==0 : even += i
#                 else: odd += i
#                 Sum += i
#             print(f"Your enter number : {num}\nSummation of digit : {Sum}\nSummation odd of digit : {odd}\nSummation even of digit : {even}")
#         case "C" | "c":
#             print(f"\nYour enter number : {num}\nThis number has {len(num)} digits.")
#         case "D" | "d":
#             print("\nExit Program...")
#             break
#     print()



# while True:
#     income = int(input("Enter your income( -1 to exit) : "))
#     if income == -1: break
#     if income > 1000000: tax = 10
#     elif income > 800000: tax = 7.5
#     elif income > 500000: tax = 5.5
#     elif income > 300000: tax = 4
#     elif income > 150000: tax = 2.5
#     else: tax = 0
#     print(f"Net Income : {income:,.2f}\nTax Rate(%) : {tax:.2f}%\nAmount Tax : {income * tax/100:,.2f}\n")
# print("Exit Program ...")


# print(">> Program Change Number to Text <<")
# num,result = input("Enter integer number : "), "Text :"
# for i in num:
#     i = int(i)
#     if i == 0  : result += " Zero"
#     elif i == 1 : result += " One"
#     elif i == 2: result += " Two"
#     elif i == 3: result += " Three"
#     elif i == 4: result += " Four"
#     elif i == 5: result += " Five"
#     elif i == 6: result += " Six"
#     elif i == 7: result += " Seven"
#     elif i == 8: result += " Eight"
#     elif i == 9: result += " Nine"
# print(result+"\nExit Program")


# print(">> Program Palindrom number <<")
# num = input("Enter integer number : ")
# for i in range(len(num)//2):
#     if num[i] == num[len(num)-i-1]: print(f"Digit {num[i]} equal to Digit {num[len(num)-i-1]}")
#     else:
#         print(f"Digit {num[i]} not equal to Digit {num[len(num)-i-1]}")
#         break
# if i != ((len(num)//2)-1) :print(f"Your enter number : {num} not is Palindrome Number.")
# else: print(f"Your enter number : {num} is Palindrome Number.")
# print("Exit Program")


# print(">> Program Find Maximum Value <<")
# value,result, Max = int(input("Enter number of value(>= 1) : ")), "Your enter number : ", 0
# if value >= 1:
#     print(f"\nProgram get value {value} numbers.")
#     for i in range(value):
#         num = int(input(f"Enter value Number #{i+1} :"))
#         if i < (value-1): result += f"{num}, "
#         else: result += f"{num} "
#         if num > Max: Max = num
#     print(result,f"Maximum value number is {Max}\nExit Program",sep="\n")
# else: print("Value input not correct.\nExit Program")



# print(">> Program Find Maximum Digit <<")
# while True:
#     num = (input("Enter integer number(0-exit) : "))
#     if num == "0":
#         print("Exit Program")
#         break
#     print(f"Maximum Digit of integer number {num} = {max(str(num))}")


# num = int(input("Enter number money withdraw : "))
# print(f"\nCash B1000 : {num // 1000}")
# print(f"\nCash B500 : {num %1000 // 500}")
# print(f"\nCash B100 : {num %500 // 100}")





# head = "| Tax Main Menu |"
# line,salary = len(head) * "=", 0,
# while True:
#     print(line,head,line,f" 0. Exit\n 1. Input Salary({salary:,.2f})\n 2. Display Tax",sep="\n")
#     choice,result, total = int(input("Enter choice : ")), "", 0
#     match choice:
#         case 0:
#             print("\nExit Program ...")
#             break
#         case 1:
#             salary = int(input("Enter salary : "))
#         case 2:
#             net_income = salary * 12 - 100000
#             print(f"\nSalary :  {salary:,.2f}\nIncome :  {salary*12:,.2f}\nDiscount :  {100000:,.2f}\nNet Income :  {net_income:,.2f}\n\nReport Tax:")
#             for i in range(8):
#                 if i == 0:   net, income, tax_rate, tax, show =       1,  150000,  0, "", 0
#                 elif i == 1: net, income, tax_rate, tax, show =  150001,  300000,  5, "", 0
#                 elif i == 2: net, income, tax_rate, tax, show =  300001,  500000, 10, "", 0
#                 elif i == 3: net, income, tax_rate, tax, show =  500001,  750000, 15, "", 0
#                 elif i == 4: net, income, tax_rate, tax, show =  750001, 1000000, 20, "", 0
#                 elif i == 5: net, income, tax_rate, tax, show = 1000001, 2000000, 25, "", 0
#                 elif i == 6: net, income, tax_rate, tax, show = 2000001, 5000000, 30, "", 0
#                 elif i == 7: net, income, tax_rate, tax, show =       0, 5050001, 35, "", 0
#                 if net_income > income - (net+1): show = income - (net-1)
#                 else: show = net_income
#                 if net_income == 0 : break
#                 net_income -= show
#                 total += show * tax_rate/100
#                 if net > 0 : result += f"|{net:13,.2f} -{income:13,.2f} |   {tax_rate:2}%  | {f"{show:,.2f} * {tax_rate/100:.2f}":22}|{show * tax_rate/100:15,.2f} |\n"
#                 else: result += f"|{"":13} >{income:13,.2f} |   {tax_rate:2}%  | {f"{show:,.2f} * {tax_rate/100:.2f}":22}|{show * tax_rate/100:15,.2f} |\n"
#             h = f"|         Net     Income      |Tax Rate|{"Tax":^40}|"
#             l = len(h) * "="
#             print(l,h,l,result+l,f"|{"Total Tax":^62}|{total:15,.2f} |",l,sep="\n")
#         case _ : print("No Choice...")
#     print()






# head = ">>  Program Calculate Grade <<"
# line, result,tc, tp = len(head) * "=", "", 0, 0
# print(head,line,sep="\n")
# print("\nInput Data:")
# for i in range(1,6+1):
#     name = input(f"Enter subject name ({i}) : ")
#     score = int(input(f"Enter subject score ({i}) : "))
#     print()
#     if score >= 80 and score <= 100: grade, point = "A", 4 * 3
#     elif score >= 70: grade, point = "B", 3 * 3
#     elif score >= 60: grade, point = "C", 2 * 3
#     elif score >= 50: grade, point = "D", 1 * 3
#     elif score >=  0: grade, point = "F", 0 * 3
#     tc += 3
#     tp += point
#     result += f":   {i}   : {name:<26}:{score:5.1f} :   {grade}   :   {3}   : {point:4.1f} :\n"
# h = ":Sub No.: Subject Name              : Mark : Grade :Credits:Points:"
# l = len(h) * "="
# print(f"{"Grade Report":>36}",l,h,l,result+l,sep="\n")
# print(f":{"Total":>36}{" "*len(" Mark : Grade ")}:  {tc:2}   : {tp:4.1f} :",l,sep="\n")
# print(f": {f"Grade Point Average(GPA) : {tp / tc:.2f}":64}:",l,sep="\n")
#






# from random import  randint
# while True:
#     print("Main Menu\n============\n 1. Play Game\n 2. Exit")
#     choice = int(input("Enter Choice : "))
#     match choice:
#         case 1:
#             score = randint(1,99)
#             score = 55
#             print("Now Play game")
#             for i in range(1,6+1):
#                 value = int(input(f"Enter guess number(#{i}) : "))
#                 if value > score: print("Your value is more than")
#                 elif value < score: print("You value is less than")
#                 elif value == score:
#                     print(f"\nYou win, use guess {i} times.\nNumber guess is {score}.")
#                     break
#             else: print(f"\nYou lose, random nuber is {score}")
#         case 2:
#             print("Exit Program...")
#             break
#         case _:
#             print("No Choice, enter again.")
#     print()
# print("\nPress any key to continue . . .")






# head = ">>>   Main Menu   <<<"
# line = len(head) * "="
# price, payment, peryear, month = 0, 0, 0, 0
# while True:
#     print(head,line,f" 0. Exit Program\n 1. Input Car Price ({price:,.2f})\n 2. Input Down Payment ({payment:,.2f}%)\n 3. Input Interest [Per Year] ({peryear:,.2f}%)\n 4. Input Month Number({month})\n 5. Display Installment\n 6. Clear All Data",sep="\n")
#     choice = int(input("Enter choice : "))
#     match choice:
#         case 0:
#             print("Exit Program...")
#             break
#         case 1: price = int(input("Enter car price : "))
#         case 2: payment = int(input("Enter down payment(%) : "))
#         case 3: peryear = float(input("Enter interest( %) per year : "))
#         case 4: month = int(input("Enter month : "))
#         case 5:
#             finance = price - price * payment/100
#             interest = finance * peryear/12/100 * 60
#             print(f"\nPrice car : {price:,.2f}\n"
#                   f"Amount down payment({payment:,.2f}%) : {price * payment/100:,.2f}\n"
#                   f"Amount finance : {finance:,.2f}\n"
#                   f"Amount interest({peryear:,.2f}%) : {interest:,.2f}\n"
#                   f"Amount net finance : {finance + interest:,.2f}\n"
#                   f"Amount installment(per month) : {(finance + interest) / 60:,.2f}")
#         case 6:
#             price = payment = peryear = month = 0
#         case _:
#             print("No choice ...")
#     print()

# from random import randint
# head = "Main  Menu"
# line = len(head) * "="
# while True:
#     print(head,line," 1. Input Number of Score\n 2. Random Score and  Check Grade\n 3. Exit",sep="\n")
#     choice = int(input("Enter Choice : "))
#     match choice:
#         case 1:
#             score = int(input("Enter number of score : "))
#         case 2:
#             print("\nStart Random Score ...\nCheck Grade ...\n")
#             a, b, c, d, f, result, total = 0, 0, 0, 0, 0, "", 0
#             for i in range(score):
#                 point = randint(40,90)
#                 if point >= 80 : a += 1
#                 elif point >= 70: b += 1
#                 elif point >= 60: c += 1
#                 elif point >= 50: d += 1
#                 else: f += 1
#             for i in range(5):
#                 if i == 0: grade, show = "A", a
#                 elif i == 1: grade, show = "B", b
#                 elif i == 2: grade, show = "C", c
#                 elif i == 3: grade, show = "D", d
#                 elif i == 4: grade, show = "F", f
#                 result += f"|  {grade}  |  {show:3} |\n"
#                 total += show
#             h = "|Grade| Total|"
#             l = len(h) * "-"
#             print(l,h,l,result+l,f"|Total|  {total:3} |",l,sep="\n")
#         case 3:
#             print("Exit Program")
#             break
#         case _:
#             print("Choice not correct.")
#     print()

# head = "| Main  Menu |"
# line = len(head) * "="
# while True:
#     print(line,head,line," 1. Triangle 1\n 2. Triangle 2\n 3. Triangle 3\n 4. Triangle 4\n 5. Exit",sep="\n")
#     choice = int(input("Enter Choice : "))
#     match choice:
#         case 1:
#             num = int(input("\nEnter number of character : "))
#             print()
#             for i in range(1,num+1):
#                 print("*" * i)
#         case 2:
#             num = int(input("\nEnter number of character : "))
#             print()
#             for i in range(num):
#                 print("*" * (num-i))
#         case 3:
#             num = int(input("\nEnter number of character : "))
#             print()
#             for i in range(1,num+1):
#                 print(" " * (num-i),"*" * i,sep="")
#         case 4:
#             num = int(input("\nEnter number of character : "))
#             print()
#             for i in range(num):
#                 print(" " * i,"*" * (num-i),sep="")
#         case 5:
#             print("\nExit Program ...")
#             break
#         case _:
#             print("\nInput error choice.")
#     print()


# head = ">>>  Main Menu  <<<"
# line = len(head) * "="
# price, payment, peryear, month = 0, 0, 0, 0
# while True:
#     print("",line,head,line,f" 0. Exit Program\n 1. Input Car Price ({price:,.2f})\n 2. Input Down Payment ({payment:,.2f}%)\n 3. Input Interest [Per Year] ({peryear:,.2f}%)\n 4. Input Month Number({month})\n 5. Display Installment\n 6. Clear All Data",sep="\n")
#     choice = int(input("Select choice : "))
#     match choice:
#         case 0:
#             print("Exit Program...")
#             break
#         case 1: price = int(input("Enter car price : "))
#         case 2: payment = int(input("Enter down payment(%) : "))
#         case 3: peryear = float(input("Enter interest( %) per year : "))
#         case 4: month = int(input("Enter month : "))
#         case 5:
#             finance = price - price * (payment / 100)
#             interest = finance * ((peryear/12)/100) * 60
#             print(f"\nPrice car : {price:,.2f}\n"
#                   f"Amount down payment({payment:,.2f}%) : {price * (payment / 100):,.2f}\n"
#                   f"Amount finance : {finance:,.2f}\n"
#                   f"Amount interest({peryear:,.2f}%) : {interest:,.2f}\n"
#                   f"Amount net finance : {finance + interest:,.2f}\n"
#                   f"Amount installment(per month) : {(finance + interest) / 60:,.2f}")
#         case 6: price = payment = peryear = month = 0
#
#
# # from random import randint
# # head = "Main  Menu"
# # line = len(head) * "="
# # while True:
# #     print("",head,line," 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Exit",sep="\n")
# #     choice = int(input("Enter Choice : "))
# #     match choice:
# #         case 1: score = int(input("Enter number of score : "))
# #         case 2:
# #             print("\nStart Random Score ...\nCheck Grade ...\n")
# #             h = "|Grade| Total|"
# #             l = len(h) * "-"
# #             result, total = "", 0
# #             a, b, c, d, f = 0, 0, 0, 0, 0
# #             print(l,h,l,sep="\n")
# #             for i in range(score):
# #                 point = randint(40,90)
# #                 if point >= 80 and point <= 100: a += 1
# #                 elif point >=70 : b += 1
# #                 elif point >=60 : c += 1
# #                 elif point >=50 : d += 1
# #                 else:f += 1
# #             for i in range(5):
# #                 if i == 0: grade, show = "A", a
# #                 elif i == 1: grade, show = "B", b
# #                 elif i == 2: grade, show = "C", c
# #                 elif i == 3: grade, show = "D", d
# #                 elif i == 4: grade, show = "F", f
# #                 result += f"|  {grade}  |  {show:3} |\n"
# #                 total += show
# #             print(result+l,f"|Total|  {total:3} |",l,sep="\n")
# #         case 3:
# #             print("Exit Program")
# #             break
# #         case _: print("Choice not correct.")
#
#
#
#
#
#
#
#
#
# # #นายปวินภา ธิติชุณหกุล
# # head = "| Main  Menu |"
# # line = len(head) * "="
# # while True:
# #     print("",line,head,line," 1. Triangle 1\n 2. Triangle 2\n 3. Triangle 3\n 4. Triangle 4\n 5. Exit",sep="\n")
# #     choice = int(input("Enter Choice : "))
# #     match choice:
# #         case 1:
# #             num = int(input("\nEnter number of character : "))
# #             print()
# #             for i in range(1,num+1):
# #                 print("*" * i)
# #         case 2:
# #             num = int(input("\nEnter number of character : "))
# #             print()
# #             for i in range(num+1):
# #                 print("*" * (num-i))
# #         case 3:
# #             num = int(input("\nEnter number of character : "))
# #             print()
# #             for i in range(1,num+1):
# #                 print(" " * (num - i),"*" * i,sep="")
# #         case 4:
# #             num = int(input("\nEnter number of character : "))
# #             print()
# #             for i in range(num+1):
# #                 print(" " * i, "*" * (num-i),sep="")
# #         case 5:
# #             print("\nExit Program ...")
# #             break
# #         case _:
# #             print("\nInput error choice.")
