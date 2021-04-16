#put your function has_digit() here
def has_digit(a, b):
    aa = str(a)
    bb = str(b)
    return bb in aa
N, D = map(int, input().split())
if has_digit(N, D):
    print("YES")
else:
    print("NO")
