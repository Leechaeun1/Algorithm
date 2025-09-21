def solution(my_string, overwrite_string, s):
    o=len(overwrite_string)
    answer = my_string[:s]+overwrite_string+my_string[s+o:]
    
    
    return answer
