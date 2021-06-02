tuple_test1 = (10,20,30)
# tuple_test2 = tuple(10,20,30)
tuple_test2 = 10,20,30
list_test1=[1,2,3]

print("tuple_test1",tuple_test1, type(tuple_test1), end='\n\n')
print("tuple_test2",tuple_test2, type(tuple_test2), end='\n\n')
print("list_test1",list_test1,type(list_test1),end='\n\n')

# 튜플은 수정불가능, 리스트는 수정가능
list_test1[1]=10
print("list_test1",list_test1,type(list_test1),end='\n\n')

[a,b] = [10,20]
(c,d) = (10,20)
print("a: ", a, " b: ", b ,  end="\n\n")
print("c: ", c, " d: ", d ,  end="\n\n")
