import sys
input = sys.stdin.readline
n = int(input())
x = 0
y = 0
for _ in range(n):
    d, dist = input().split()
    if d == "N":
        y += int(dist)
    elif d =="E":
        x += int(dist)
    elif d == "S":
        y -= int(dist)
    else:
        x -= int(dist)
print(x, y)