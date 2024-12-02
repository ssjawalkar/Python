def stone_piles(n):
    if n <= 0:
        return []
    start = 2 if n % 2 == 0 else 1
    arr = []
    for i in range(n//2):
        arr.append(start + 2 * i)
    return arr

n = 6
result = stone_piles(n)
print(f"Stones in each pile: {result}")
