def solve(a, b, c):

    d = b ** 2 - 4 * a * c

    if d == 0:
        root = -b / (2 * a)
        return root, root

    sqrt_d = d ** 0.5

    if b >= 0:
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (2 * c) / (-b - sqrt_d)
    else:
        x1 = (2 * c) / (-b + sqrt_d)
        x2 = (-b + sqrt_d) / (2 * a)

    return min(x1, x2), max(x1, x2)

print(solve(1, -4, -5))  # (-1.0, 5.0)
print(solve(-2, 7, -5))  # (1.0, 2.5)
print(solve(1, 2, 1))  # (-1.0, -1.0)