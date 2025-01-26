n = input().split('.')  # 입력받은 문자열을 '.' 기준으로 나누어 리스트로 저장

a = [x.replace('XXXX', 'AAAA').replace('XX', 'BB') for x in n]  # 리스트의 각 요소에 replace 적용
result = '.'.join(a)

if 'X' in result :
    print(-1)
else:
    print(result)