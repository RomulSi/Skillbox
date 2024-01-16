L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))

M = [-2, -1, 0, 1, -3, 2, -3]
print(list(filter(lambda x: (x % 2 == 0), M)))


def positive(x): return x > 0
