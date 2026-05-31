import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    d, w = list(data), list(weights) if weights else [1] * len(data)
    res = []
    for _ in range(n):
        idx = d.index(random.choices(d, weights=w)[0])
        res.append(d.pop(idx))
        w.pop(idx)
    return res
