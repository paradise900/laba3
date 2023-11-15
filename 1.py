def sol(n):
    ITEMS = ['в', 'п', 'б', 'а', 'и', 'н', 'т', 'о', 'ф', 'д', 'к', 'р']
    VALUES = [25, 15, 15, 20, 5, 15, 20, 25, 15, 20, 20]
    WEIGHTS = [3, 2, 2, 2, 1, 1, 3, 1, 1, 2, 2]
    score = 15
    capacity = n
    prod = []
    liters = []

    for i in range(len(VALUES)):
        prod.append((VALUES[i] / WEIGHTS[i], i))
    prod.sort()

    for i in reversed(range(len(prod))):
        weight = WEIGHTS[prod[i][1]]
        if capacity - weight >= 0:
            score += weight * prod[i][0]
            capacity -= weight
            for _ in range(weight):
                liters.append([ITEMS[prod[i][1]]])
        else:
            score -= weight * prod[i][0]
    return liters, score


TASK_NUM = 9
ROWS = 3
ans, score = sol(TASK_NUM)
for i in range(ROWS):
    print(*ans[ROWS * i:ROWS * i + ROWS])
print(f'Итоговые очки выживания - {int(score)}\n')

# extra task
EXTRA_TASK_NUM = 7
ans, score = sol(EXTRA_TASK_NUM)
print(*ans)
print(f'Итоговые очки выживания - {int(score)}')