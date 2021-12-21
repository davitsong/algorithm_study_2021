import sys
from functools import cmp_to_key

def compare(s1, s2):
    if len(s1) == len(s2):
        return -1 if s1 < s2 else 1
    else:
        return len(s1) - len(s2)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    words = [sys.stdin.readline().rstrip() for i in range(N)]

    words.sort(key=cmp_to_key(compare))

    print(words[0])
    i = 1
    for i in range(1, len(words)):
        if words[i] != words[i-1]:
            print(words[i])
