#Arrays: Left Rotation


def array_left_rotation(a, n, k):
    for i in range(k):
        temp = a.pop(0)
        a.append(temp)
    return a

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
