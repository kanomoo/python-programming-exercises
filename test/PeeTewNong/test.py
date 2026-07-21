result = ""
for i in range(3):
    name = input(f"Enter Name {i + 1} : ")
    score = int(input(f"Enter Score {i + 1} :"))
    if score >= 80 and score <= 100:grade = "A"
    elif score >= 75:grade = "B+"
    elif score >= 70:grade = "B"
    elif score >= 65:grade = "C+"
    elif score >= 60:grade = "C"
    elif score >= 55:grade = "D+"
    elif score >= 50:grade = "D"
    else:grade = "F"
    result += (f"Name {name} | Score {score} | Grade{grade}\n")

print(result)