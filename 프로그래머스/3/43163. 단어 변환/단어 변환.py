from collections import deque

def solution(begin, target, words):
    # 단어 방문 여부를 기록하는 리스트, 초기에는 모두 False (방문 안 함)
    visited = [False] * len(words)
    
    # BFS 탐색을 위한 큐 생성, 시작 단어와 변환 단계 0을 넣음
    queue = deque([(begin, 0)])
    
    # 최종 답안을 저장할 변수, 기본값은 0 (변환 불가능한 경우)
    answer = 0

    # 큐가 빌 때까지 반복 (BFS 진행)
    while queue:
        # 큐에서 현재 단어와 지금까지 변환한 단계 수를 꺼냄
        current_word, steps = queue.popleft()
        
        # 현재 단어가 목표 단어(target)와 같다면
        if current_word == target:
            # 정답을 steps로 저장하고 탐색 종료
            answer = steps
            break  # 더 이상 탐색할 필요 없음
        
        # words 리스트의 모든 단어에 대해 검사
        for i, word in enumerate(words):
            # 아직 방문하지 않은 단어에 한해서만 탐색
            if not visited[i]:
                # 현재 단어와 비교 단어 간에 서로 다른 글자 개수를 셈
                diff_count = sum(1 for c1, c2 in zip(current_word, word) if c1 != c2)
                
                # 글자 차이가 정확히 1개일 때만 변환 가능
                if diff_count == 1:
                    # 방문 처리해서 중복 탐색 방지
                    visited[i] = True
                    # 큐에 변환한 단어와 단계 수 + 1을 넣음
                    queue.append((word, steps + 1))

    # 변환 가능하면 단계 수가, 불가능하면 0이 담긴 answer 반환
    return answer
