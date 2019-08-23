def search(stu_no, stu_name, number):
    n = len(stu_no)
    for i in range(n):
        if number == stu_no[i]:
            return stu_name[i]
     
    return"?"
        

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike","Summer"]

print(search(stu_no, stu_name, 39))
print(search(stu_no, stu_name, 14))
print(search(stu_no, stu_name, 108))
print(search(stu_no, stu_name, 67))
print(search(stu_no, stu_name, 10))
