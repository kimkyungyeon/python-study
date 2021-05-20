for i in range(5):
    print(str(i) + "=반복 변수")
print()

for i in range(5,10):
    print(str(i) +"=반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i) +"=반복 변수")
print()

array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번재 반복: {}".format(i, array[i]))

#역반복분
for i in range(4,0-1,-1):
    print("현재 반복 변수 : {}".format(i))

for i in reversed(range(5)):
    print("현재 반복변수 : {}".format(i))

key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]

character = {}
for i in range(4):
    character[key_list[i]]=value_list[i]

print(character)

limit = 10000

i = 1
sum_value = 0
while sum_value < limit:
    sum_value += i
    i+=1

print("{}를 더할 때 {}을 넘으면 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

max_value = 0
a = 0
b = 0

for i in range(100):
    j = 100 - i

    current = i*j
    #최댓값 구하기
    if max_value < current:
        a = i
        b = j
        max_value = current
print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))