
def solution(array,commands):
    answer=[]
    for a, b, c in commands:
        answer += [sorted(array[a-1:b])[c-1]]
    return answer;

def solution2(array,commands):
    return [sorted(array[a-1:b])[c-1] for a, b, c in commands]

if __name__ == "__main__":
    array = [1,5,2,6,3,7,4]
    commands = [[2,5,3],[4,4,1],[1,7,3]]

    res= solution(array,commands)
    res2= solution2(array,commands)


    print(type(res),res)
    print(type(res2),res2)