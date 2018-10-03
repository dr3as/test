def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)

add_numbers(3, 4, 5, 6, 7, 8, 9)