def dan(num):
    for i in range(1,10):
        print('{} * {} = {:2}'.format(num, i , num*i)  )


# if __name__ == "__main__":
#     dan(3)

def gugudan():
    for i in range(2,10):
        dan(i)

def gugudan2():
    for i in range(1,10):
        for j in range(2,10):
            print('{} * {} = {:2}'.format(j, i , i*j) ,end='\t')
        print()






if __name__=="__main__":
    gugudan()
    gugudan2()
    print()