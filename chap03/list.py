array = [273, 32, 103, '문자열', True, False]
print(array)

print(array[0])
print(array[1:3])
array[0] = '변경완료'

print(array)
print(array[-1])
print(array[-6])
print()

print(array[3][-1])
print()

array1 = [[1,2,3],[4,5,6],[7,8,9]]
print(array1[1])
print(array1[0][-1])


number1 = [];
for i in range(100):
    if (i % 2== 0):
        number1.append(i)
print(number1)
#1~100까지의 짝수만 저장
even_list = [i for i in range(101) if i%2 ==0]
print(even_list)

odd_list = [i for i in range(100) if i%2 ==1]
print(odd_list)


list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for sub_list in list_of_list:
    for i in sub_list:
        print(i)