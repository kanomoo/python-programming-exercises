#นายปภาวิน ธิติชุณหุล 6806021612037 it sec 3
def report_score(filename):
    data = all_score(filename)
    for i in data:
        head = "| No.|Grade|Point|Credit| Total|"
        line = "=" * len(head)
        print(f"{"Report Grade":^{len(head)}}\nId : {i[0][0]}, Name : {i[0][1]}")
        result = f"{line}\n{head}\n{line}\n" 
        total = 0
        credit = 0
        for n in range(1,len(i)):
            result += f"| {n:2} |  {i[n][0]:2} | {i[n][1]:2.1f} | {i[n][2]:4} | {i[n][3]:4.1f} |\n"
            total += i[n][3]
            credit += i[n][2]
        result += f"{line}\ntotal point : {total}, total credit : {credit}\nGrade Point Average (GPA) : {total/credit:.2f}\n"
        print(result)

def all_score(filename):
    data = []
    with open(filename,"r",encoding="utf-8") as fin:
        for i in fin:
            data.append(i.strip("\n").split(","))
    sub_datas = []
    grades = {"A":4.0,"B+":3.5,"B":3.0,"C+":2.5,"C":2.0,"D+":1.5,"D":1.0,"F":0.0}
    for i,v in enumerate(data):
        sub_data = [[f"{v[0][:3]}-{v[0][3:]}",v[1]]]
        for n in range(2,len(data[0])) :
            s_data = []
            for g in grades:
                if data[i][n] == g: grade = grades[g]
            s_data.extend([data[i][n],grade,3,float(grade*3)])
            sub_data.append(s_data)
        sub_datas.append(sub_data)
    return(sub_datas)