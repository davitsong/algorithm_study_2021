import sys

data=[]
n=int(input())

for i in range(n):
    data.append(sys.stdin.readline().strip())

k = set(data)
t = list(k)
t.sort()
t.sort(key=len)

for i in t:
    print(i)
