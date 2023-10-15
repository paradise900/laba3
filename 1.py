def sol(n):
    score = 15
    items = ['в', 'п', 'б', 'а', 'и', 'н', 'т', 'о', 'ф', 'д', 'к', 'р']
    values = [25, 15, 15, 20, 5, 15, 20, 25, 15, 20, 20]
    weights = [3, 2, 2, 2, 1, 1, 3, 1, 1, 2, 2]
    capacity = n
    prod = []
    liters = []

    for i in range(len(values)):
        prod.append((values[i] / weights[i], i))
    prod.sort()

    for i in reversed(range(len(prod))):
        weight = weights[prod[i][1]]
        if capacity - weight >= 0:
            score += weight * prod[i][0]
            capacity -= weight
            for _ in range(weight):
                liters.append([items[prod[i][1]]])
        else:
            score -= weight * prod[i][0]
    return liters, score


ans, score = sol(9)
for i in range(3):
    print(*ans[3 * i:3 * i + 3])
print(f'Итоговые очки выживания - {int(score)}\n')

# extra task
ans, score = sol(7)
print(*ans)
print(f'Итоговые очки выживания - {int(score)}')