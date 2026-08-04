# นายปภาวิน ธิติชุณหกุล 6806021612037
num = int(input(" กรอกแม่สูตรคูณ (2-12) : "))
if num >= 2 and num <= 12:
    print(f"    ตารางแม่สูตรคูณ {num}")
    print("-" * 23)
    for i in range(1, 13):
        print(" " * 5, f"{num} x {i} = {num * i}")
else:
    print("กรุณากรอกเลขระหว่าง 2 ถึง 12")