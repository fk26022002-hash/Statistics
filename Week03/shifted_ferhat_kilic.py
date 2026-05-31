def shifted(sample):
    s = sorted(abs(x) for x in sample)
    n = len(s)
    mean = sum(s) / n
    median = (s[n // 2] + s[~(n // 2)]) / 2
    mae = sum(abs(x - mean) for x in s) / n
    return abs(mean - median) / mae * 100 if mae else 0
