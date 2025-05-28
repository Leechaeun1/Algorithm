from collections import deque

def solution(begin, target, words):
    visited=[False]*len(words)
    
    queue = deque([(begin,0)])
    
    answer = 0
    
    while queue:
        current_word, steps = queue.popleft()
        
        if current_word==target:
            answer = steps
            break
        
        for i, word in enumerate(words):
            if not visited[i]:
                diff_count=sum(1 for c1, c2 in zip(current_word, word) if c1 != c2)
                if diff_count==1:
                    visited[i]=True
                    queue.append((word, steps+1))
    
    return answer