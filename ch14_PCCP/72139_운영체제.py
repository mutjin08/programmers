# 다시풀기
import heapq
def solution(program):
    answer = [0]*11
    heap = []
    
    #정렬기준 : 시작시간 -> 우선순위
    program.sort(key = lambda x : (x[1], x[0]))
    
    #현재시각
    time = 0
    
    while program or heap:
        # 현재시각 이전 or 현재시각에 수행될 수 있는 모든 프로그램을
        # 힙에 우선순위를 기준으로 저장
        while program and program[0][1] <= time:
            heapq.heappush(heap, program.pop(0))
            
        # 현재시각에 수행될 수 있는 프로그램이 없는 경우
        # 현재시각을 다음 프로그램의 시작시간으로 갱신
        if program and not heap:
            time = program[0][1]
            heapq.heappush(heap, program.pop(0))
            
        # 프로그램 수행
        target = heapq.heappop(heap)
        
        # 타겟 프로그램의 우선순위를 index로 하여 대기시간을 저장한다
        answer[target[0]] += time - target[1]
        # 현재시각을 타겟 프로그램의 종료시간으로 갱신
        time += target[2]
    
    answer[0] = time
    return answer