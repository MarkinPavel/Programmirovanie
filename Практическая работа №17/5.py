def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_valid_password(password):
    parts = password.split(':')
    if len(parts) != 3:
        return False

    a_str, b_str, c_str = parts

    if not (a_str.isdigit() and b_str.isdigit() and c_str.isdigit()):
        return False

    a, b, c = int(a_str), int(b_str), int(c_str)

    if a <= 0 or b <= 0 or c <= 0:
        return False

    return is_palindrome(a) and is_prime(b) and (c % 2 == 0)

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))