
"""
카카오톡 사용자 n명의 구매 기준을 담은 2차원 정수 배열 users, 이모티콘 m개의 정가를 담은 1차원 정수 배열 emoticons가 주어집니다. 이때, 행사 목적을 최대한으로 달성했을 때의 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액을 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해주세요.
"""
from itertools import product

def case_result(users, emoticons, discounts):
    answer = [0, 0]
    for wantRate, joinPrice in users:
        userPay = 0
        for originalPrice, discountRate in zip(emoticons, discounts):
            if discountRate < wantRate:
                continue
            
            saledPrice = originalPrice * (100-discountRate) / 100
            userPay += saledPrice
            
            if userPay >= joinPrice:
                answer[0] += 1
                userPay = 0
                break
            
        answer[1] += userPay
            
    return answer

def solution(users, emoticons):
    answer = []
    n, m = len(users), len(emoticons)
    for discount_case in product([10, 20, 30, 40], repeat = m):
        answer.append(case_result(users, emoticons, discount_case))
    answer.sort(key = lambda x : (x[0], x[1]))
    return answer[-1]
        