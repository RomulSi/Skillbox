import time
def find_e():
    n = 1
    while True:
        yield (1 + 1 / n) ** n
        n += 1


gen = find_e()
while True:
    print(next(gen))
    time.sleep(0.3)

print(type(range(5)))
