x, k = map(int, input().split())
ans = x
for keta in range(1, k + 1):
    # round関数の仕様で5が繰り上げされないので、1を足す
    ans = round(ans + 1, -keta)
print(ans)
