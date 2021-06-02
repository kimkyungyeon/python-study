list_a = [[10,20],[30,40,70,110],[50,60],[80,90,100]]
dict_a = {'k': {'a':10,'b':20}, 'l':{'a':10,'b':20,'c':40}, 'm':{'a':10}}



def printList(list):
    for item in range(0,len(list)):
        for i in range(0,len(list[item])):
            print(list[item][i],end='\t')
        print()
printList(list_a)


def printDict(dict):
    for key in dict:
        print(key, "=>", end="  ")
        for key1 in dict[key]:
            print( key1 ,":", dict[key][key1], end="\t")
        print()

printDict(dict_a)
