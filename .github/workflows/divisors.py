import sys

number = int(sys.argv[1])

for i in range(1, number + 1):  # 1부터 number까지 반복
    if number % i == 0:         # i가 number의 약수인지 확인
        print(i, end=" ")

print()
