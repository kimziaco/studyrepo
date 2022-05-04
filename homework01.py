# 구구단 출력
for x in range(1, 10):
    for y in range(1, 10):
        print(x, "X", y, "=", x * y)

# N을 입력받고 N단 구구단 출력
n = int(input())
for i in range(1, 10):
    print(n, "X", i, "=", n * i)
