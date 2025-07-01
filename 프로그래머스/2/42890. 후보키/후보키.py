from itertools import combinations

def solution(relation):
    n_col = len(relation[0])
    n_row = len(relation)
    all_keys = []
    
    for i in range(1, n_col + 1):
        for comb in combinations(range(n_col), i):
            temp = [tuple(row[c] for c in comb) for row in relation]
            if len(set(temp)) == n_row:  # 유일성
                if not any(set(x).issubset(comb) for x in all_keys):  # 최소성
                    all_keys.append(comb)
    
    return len(all_keys)