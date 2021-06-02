import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

os.mkdir("hello")
os.rmdir("hello")

with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt","new.txt")

std_list = [[1, "김상건", 50, 60, 70]]
if not os.path.exists("std_list.txt"):
    # if os.path.isfile("std_list.txt"):
    with open("std_list.txt","w", encoding="utf-8")as f:
        for std in std_list:
            format_str = "{},{},{},{},{}".format(std[0],std[1],std[2],std[3],std[4])
            f.write(format_str)

std_list2 = []

with open("std_list  .txt", "r", encoding="utf-8") as f:
    for line in f:
        std = line.strip().split(",")
        print("std : ", std)
        std_list2.append(std)




os.remove("new.txt")

os.system("dir")