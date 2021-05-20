import datetime

#현재 날짜
now = datetime.datetime.now()

print(now)

#출력1
print(now.year, '년')
print(now.month, '월')
print(now.day, '일')
print(now.hour, '시')
print(now.minute, '분')
print(now.second, '초')

print("{0}년 {1}월 {2}일 {3}시 {4}분 {5}초 ".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

#오전구분
if now.hour<12:
    print("현재 시각은 {}시로 오전입니다.!".format(now.hour))
#오후구분
if now.hour>=12:
    print("현재 시각은 {}시로 오후입니다.!".format(now.hour))
