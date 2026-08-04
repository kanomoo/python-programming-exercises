title = "| No. |       Name Subject        | Score | Grade | Level | Credit | Point |"
result, line, total_credit, total_point = "", "=" * len(title), 0, 0
result += f"{"Report Grade":^{len(title)}}\n{line}\n{title}\n{line}\n"
for i in range(5):
    name, score, credit = input("\nEnter name : "), int(input("Enter score : ")), int(input("Enter credit : "))
    if score >= 80: grade, level = "A", 4.0
    elif score >= 75: grade, level = "B+", 3.5
    elif score >= 70: grade, level = "B", 3.0
    elif score >= 65: grade, level = "C+", 2.5
    elif score >= 60: grade, level = "C", 2.0
    elif score >= 55: grade, level = "D+", 1.5
    elif score >= 50: grade, level = "D", 1.0
    else: grade, level = "F", 0
    total_point, total_credit = total_credit + level * credit, total_credit + credit
    result += f"|{i + 1:^5}| {name:<25} |{score:^7}|   {grade:<3} |{level:^7.1f}|{credit:^8}|{level * credit:^7.1f}|\n"
result += f"{line}\n|{"Total":^57}|{total_credit:^8}|{total_point:^7.1f}|\n{line}\n"
result += f"|{f"Grade Point Average (GPA) : {total_point / total_credit:.2f}":^{len(title) - 2}}|\n{line}\n"
print(result)