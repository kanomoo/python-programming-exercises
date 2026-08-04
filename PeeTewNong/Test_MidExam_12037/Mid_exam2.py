# นายปภาวิน ธิติชุณหกุล 6806021612037 sec C
total, line = 0, "=" * 21
for i in range(5):
    num = int(input(f"Enter Number #{i + 1} : "))
    total += num
print(line)
print(f"Total = {total}")
print(line)
print(f"Average = {total / 5:.2f}")
