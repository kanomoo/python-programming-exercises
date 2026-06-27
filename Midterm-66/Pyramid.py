# name = input("Enter string for Pyramid : ") # RukSomchai
# num = len(name)
# mess = ""
# for i in range(num):
#     mess += (" " * (num - i-1))
#     for n in name[:i+1]:
#         mess += f"{n} "
#     mess += "\n"
# print(mess)

# #show in terminal
# name = "RukSomchai"
# print(f"Enter string for Pyramid : {name}") # RukSomchai
# num = len(name)
# mess = ""
# for i in range(num):
#     mess += (" " * (num - i-1))
#     for n in name[:i+1]:
#         mess += f"{n} "
#     mess += "\n"
# print(mess)

#show in terminal
# num = input("Enter string for pyramid : ")

# num = "RukSomchai"
# num = " ".join(num)
# for i in range(0,len(num),2):
#     print(" " * ((len(num) // 2) - (i // 2)),num[:i+1],sep="")


# name,result = input("Enter string for Pyramid : "), ""
# for i in name:
#     result += i
#     result += " "
# for i in range(2,len(result)+1,2):
#     print(" " * (len(name) - i // 2),result[:i],sep="")

# p = input("Enter string for pyramid : ")
# result = ""
# for i in range(len(p)-1,-1,-1):
#     print("1" * i,end="")
# for i in range(len(p)):
#     print(p[i] + " ",end="")


# num = input("Enter string for Pyramid : ")
# result = ""
# for i in num:
#     result += i
#     result += " "
# for i in range(len(num)):
#     print(" " * (len(num) - i -1) + result[:i * 2+1])


# num, result = input("Enter string for Pyramid : "), ""
# for i in num: result += i + " "
# for i in range(len(num)): print(" " * (len(num) - i -1) + result[:i * 2+1])


name = input("Enter name: ")
for i in range(len(name)):
    print(" " * (len(name) - i - 1), end = "")
    for l in range(i): print(name[l], end = " ")
    print()