import sys

data=[]
cnt=0
k=0

n,max = map(int,sys.stdin.readline().split())

#print(a,b)

for i in range(n):
    if i<=max:
        data.append(int(sys.stdin.readline().strip()))

#data.sort(reverse=True)
ans = max

for i in data[::-1]:
    if i > ans:
        continue
    else:
        cnt += ans//i
        k+=cnt
        ans = ans-(i*cnt)
        cnt=0
        if ans==0:
            break
        
 
print(k)
