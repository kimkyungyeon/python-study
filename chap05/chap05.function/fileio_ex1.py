file = open("basic.txt","w")

file.write("Hello Python Programming..")
file.close()

with open("basic2.txt","w") as f:
    f.write("Hello Python Programming...")


def fopen2(filename):
    with open(filename, "w") as f:
        f.write("Hello Python Programming...")


#read
def f_read(filename):
    with open(filename,"r") as f:
        contents = f.read()
    return contents

c = f_read("basic2.txt")
print(c)