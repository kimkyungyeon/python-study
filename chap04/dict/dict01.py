ingredient = ["망고", "설탕", "메타중아황산나트륨", "치자황색소"]


# 딕셔너리 선언
dictionary = {
    "name" : "7D 건조망고",
    "type" : "당절임",
    "ingredient" : ingredient,
    "origin" : "필리핀"
}


#출력
print("name : ", dictionary["name"])
print("type : ", dictionary["type"])
for ingredient in dictionary["ingredient"]:
    print("ingredient : ",ingredient)
print("ingredient : ", dictionary["ingredient"][0])
print("origin : ", dictionary["origin"])
print()

#값을 변경합니다.
dictionary["name"] = "8D 건조망고"
print("name : ", dictionary["name"])

dict_key = {
    "name": "7D건조망고",
    "type": "당절임"
}
print(dict_key)

dictionary["price"] = 5000

print(dictionary)

del dictionary["ingredient"]

print(dictionary)
print()
# key = input("> 접근하고자 하는 키 : ")
# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있스빈다.")

#존재하지 않는 키에 접근
value = dictionary.get("origin1")
print("값 : ", value)

#none 확인방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")
print()
for key in dictionary:
    #출력
    print(key, " : ", dictionary[key])

dict_a = {}
print(dict_a)
dict_a["name"] ="구름";
print(dict_a)
del dict_a["name"]
print(dict_a)

pets = [
    {"name":"구름" , "age":5},
    {"name":"초코" , "age":3},
    {"name":"아지" , "age":1},
    {"name":"호랑이" , "age":1}
]

for key in pets:
    print(key.get("name"),":",key.get("age"),"살")

for pet in pets:
    print(pet["name"], str(pet["age"])+"살")
print()
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number]= counter[number]+1
    else:
        counter[number]=1

print(counter)
print()
print()

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기","세게 베기", "아주 세게 베기"]
}

for key in character:

    print(key," : ", character[key])