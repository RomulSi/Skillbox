a = 600
if all([type(a) == int,
        100 < a < 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Number is correct")

squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(squares)

L = [i for i in range(10)]
M = [i for i in range(10,0,-1)]
new_one = [a*b for a, b in zip(L, M)]
print(new_one)

f_str = 'aaabbccccdaa'
out_dict = {}

for ch in f_str:
    if ch in out_dict:
        out_dict[ch] += 1
    else:
        out_dict[ch] = 1

out_string = ''.join([f'{key}{value}' for key, value in out_dict.items()])
print(out_string)

