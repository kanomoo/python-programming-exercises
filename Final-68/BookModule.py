#นายปภาวิน ธิติชุณหุล 6806021612037 it sec 3
def add_book(filename):
    data = []
    with open(filename,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))
    print(f"\n< Add Book >\n\nnow {len(data)} book in data.")
    id = input("Enter id  : ")
    c_id = [i for i in data[0]]
    if id not in c_id:
            name = input("Enter name : ")
            price = input("Enter price : ")
            qty = input("Enter qty : ")
            confirm = input("\nconfirm (Y/N) : ").lower()
            if confirm == "y": 
                with open(filename,"a",encoding="utf-8") as fin:
                    fin.write(",".join((id,name,price,qty))+"\n")
                print("Add data complete")
            elif confirm == "n":
                print("Cancel")
            else : 
                print("No choice")
    else : 
        print("id in data not add again.")
        
    
def edit_book(filename):
    data = []
    with open(filename,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))
    print(f"\n< Edit Book >\n\nnow {len(data)} book in data.")
    id = input("Enter id  : ")
    for i, s_data in enumerate(data):
        if id == s_data[0]:
            name = input("Enter name : ")
            price = input("Enter price : ")
            qty = input("Enter qty : ")
            confirm = input("\nconfirm (Y/N) : ").lower()
            data[i] = [id,name,price,qty]
            if confirm == "y": 
                with open(filename,"w",encoding="utf-8") as fin:
                    for s in data:
                        fin.write(",".join(s)+"\n")
                print("Edit data complete")
                break
            elif confirm == "n":
                print("Cancel")
                break
            else : 
                print("No choice")
    else: print("id not in data")

def del_book(filename):
    data = []
    with open(filename,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))
    print(f"\n< Delete Book >\n\nnow {len(data)} book in data.")
    id = input("Enter id  : ")
    for i, s_data in enumerate(data):
        if id == s_data[0]:
            del data[i]
            confirm = input("\nconfirm (Y/N) : ").lower()
            if confirm == "y": 
                with open(filename,"w",encoding="utf-8") as fin:
                    for s in data:
                        fin.write(",".join(s)+"\n")
                print("Delete data complete")
                break
            elif confirm == "n":
                print("Cancel")
                break
            else : 
                print("No choice")
    else: print("id not in data")

def read_file(filename):
    data = []
    with open(filename,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))
    print(f"\n< Show data >\n\nnow {len(data)} book in data.")
    for s_data in data:
        print(f"id : {s_data[0]}, name : {s_data[1]}, price : {s_data[2]}, qty : {s_data[3]}")

def report_book(filename):
    data = []
    with open(filename,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))
    head = f"|{"id":^11}|{"name":^11}|{"price":^11}|{"qty":^11}|{"total":^11}|"
    line = "=" * len(head)
    result = f"\n{"report grade":^{len(head)}}\n{line}\n{head}\n{line}\n"
    for s_data in data:
        result += f"|{s_data[0]:>10} |{s_data[1]:10} |{int(s_data[2]):10.2f} |{int(s_data[3]):10.2f} |{int(s_data[2]) * int(s_data[3]):10.2f} |\n"
    print(result+line)