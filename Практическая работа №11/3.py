for a in range(1, 151):
    a5 = a ** 5
    for b in range(a, 151):
        b5 = a5 + b ** 5
        for c in range(b, 151):
            c5 = b5 + c ** 5
            for d in range(c, 151):
                e5 = c5 + d ** 5
                e = int(round(e5 ** 0.2))
                if e ** 5 == e5 and e <= 150:
                    print(a + b + c + d + e)
                    exit()