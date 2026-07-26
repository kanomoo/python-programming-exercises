print(">> Program Find Maximum Digit <<")
while True:
    Max = 0
    num = input("Enter integer number(0-exit) : ")
    if num == "0":
        print("Exit Program")
        break
    for i in num:
        if int(i) > Max: Max = int(i)
    print(f"Maximum Digit of integer number {num} = {Max}")
    