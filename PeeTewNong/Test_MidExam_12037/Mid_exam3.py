result = ""
title = "| No. |       Name Subject        | Score | Grade | Level | Credit | Point |"
line = "=" * len(title)
result += f"{"Report Grade":^{len(title)}}\n"
result += line + "\n"
result += title + "\n"
result += line + "\n"
total_credit = 0
total_point = 0
for i in range(5):
    name = input("Enter name : ")
    score = int(input("Enter score : "))
    credit = int(input("Enter credit : "))
    print()
    if score >= 80: grade, level = "A", 4.0
    elif score >= 75: grade, level = "B+", 3.5
    elif score >= 70: grade, level = "B", 3.0
    elif score >= 65: grade, level = "C+", 2.5
    elif score >= 60: grade, level = "C", 2.0
    elif score >= 55: grade, level = "D+", 1.5
    elif score >= 50: grade, level = "D", 1.0
    else: grade, level = "F", 0
    total_point += level * credit
    total_credit += credit
    result += f"|{i + 1:^5}| {name:<25} |{score:^7}|   {grade:<3} |{level:^7.1f}|{"3":^8}|{level * credit:^7.1f}|\n"
result += line + "\n"
result += f"|{"Total":^57}|{total_credit:^8}|{total_point:^7.1f}|\n"
result += line + "\n"
result += f"|{f"Grade Point Average (GPA) : {total_point / total_credit:.2f}":^{len(title) - 2}}|\n"
result += line + "\n"
print(result)