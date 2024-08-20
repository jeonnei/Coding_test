def solution(chicken):
    if chicken<10:
        return 0
    else:       # 재귀함수로 구현
        #print(chicken)
        # 치킨 1마리 주문당 치킨쿠폰 1개 지급
        # 쿠폰 10개당 치킨 1마리 (남은 쿠폰갯수는 다음 계산에 사용 = chicken%10)
        return (chicken//10)+solution(chicken//10+chicken%10) 

# 예시
a = solution(1081)
print(a)
a = solution(100)
print(a)