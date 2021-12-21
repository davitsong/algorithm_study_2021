import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    costs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

    answer = 0
    for i in range(len(costs)-1, -1, -1):
        cost = costs[i]
        answer += (K // cost)
        K -= cost * (K // cost)

    print(answer)
