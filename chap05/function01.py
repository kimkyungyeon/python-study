def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()
print()
def print_n_times(value,n):
    for i in range(n):
        print(value)

print_n_times("안농하세욤",5)

def print_n_times(n, *values):
    #n번 반복
    for i in range(n):
        #values는 리스트처럼 활용
        for value in values:
            print(value)
        print()
        
#함수를 호출합니다.
print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

print("-----------------------------------------")

def print_n_times(value, n=2):
    #n번 반복
    for i in range(n):
        print(value)

print_n_times("안녕하세요")

print("-----------------------------------------")

def print_n_times(*values, n=2):
    #n번 반복
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요","즐거운","파이썬프로그래밍",n=3)

print("-----------------------------------------")

def test(a,b=10,c=100):
    print(a+b+c)

test(10, 20, 30)

test(a=10,b=100,c=200)

test(c=10, a=100, b=200)

test(10,c=200)

def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")

return_test()


def mul(*values):
    a=1
    for value in values:
       a *= value
    return a

print(mul(5,7,9,10))
