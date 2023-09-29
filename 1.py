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
        w = weights[prod[i][1]]
        if capacity - w == 0:
            score += w * prod[i][0]
            capacity -= w
            for _ in range(w):
                liters.append([items[prod[i][1]]])
        elif capacity - w < 0:
            score -= w * prod[i][0]
        else:
            score += w * prod[i][0]
            capacity -= w
            for _ in range(w):
                liters.append([items[prod[i][1]]])
    return liters, score


ans, score = sol(9)
for i in range(3):
    print(*ans[3 * i:3 * i + 3])
print('Итоговые очки выживания - ', int(score))
print()

# extra task
ans, score = sol(7)
print(*ans)
print('Итоговые очки выживания - ', int(score))