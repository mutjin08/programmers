def total_fee(time, fees):
    if time<=fees[0]:
        return fees[1]
    
    late_time = time-fees[0]
    if late_time%fees[2]==0:
        return fees[1] + (late_time//fees[2])*fees[3]
    return fees[1] + (late_time//fees[2]+1)*fees[3]
    

def to_min(time):
    h, m = map(int, time.split(":"))
    return h*60+m

def total_time(arr):
    if len(arr)%2!=0:
        arr.append("23:59")
    
    total = 0
    for i in range(0, len(arr), 2):
        arr[i], arr[i+1] = to_min(arr[i]), to_min(arr[i+1])
        total += (arr[i+1]-arr[i])
    return total

def solution(fees, records):
    logs = {}
    for r in records:
        time, car, action = r.split()
        if car not in logs:
            logs[car] = []
        logs[car].append(time)
    
    answer = []
    for car in sorted(logs):
        time = total_time(logs[car])
        answer.append(total_fee(time, fees))
    return answer