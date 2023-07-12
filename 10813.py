N, M = map(int, input().split())
basket = [0] * (N+1)

for i in range(N+1):
    basket[i] = i

for _ in range(M):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]

for i in range(1, N+1):
    print(basket[i], end=' ')