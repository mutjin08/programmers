#product vs. combinations_with_replacement

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
        