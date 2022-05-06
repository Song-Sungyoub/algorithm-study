# 실패한 코드 결과가 안 맞음

def solution(food_times, k):
    answer = 0
    cnt = 0
    while k!=cnt:
    	if sum(food_times) == 0:
    		answer=-2
    		break 
    	if food_times[answer] != 0:
    		print(answer)
    		food_times[answer] -= 1
    		cnt+=1
    	answer = (answer+1)%3
    	
    return answer+1
    
print(solution([1,0,1],5))
