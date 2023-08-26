def get_millions(s: str) -> float:
    right = len(s) - 1
    while not s[right].isdigit() and right > 0:
        right -= 1

    if 'млн' in s:
        return float(s[:right + 1])
    elif 'млрд' in s:
        return float(s[:right + 1]) * 1000

    return float(s[:right + 1]) / 1000
