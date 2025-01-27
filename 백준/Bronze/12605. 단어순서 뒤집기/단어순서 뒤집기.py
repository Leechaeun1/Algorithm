n = int(input())
case = [input(). split(' ') for _ in range (n)]

for i in range (n) :
    top = ' '.join(case[i][::-1])

    print(f"Case #{i+1}: {top}")