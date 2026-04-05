while True:
    n = int(input("Введіть кількість: "))
    w = int(input("Введіть ширину: "))
    h = int(input("Введіть довжину: "))

    if not (1 <= n <= 10 ** 12):
        print("помилка - 1 <= n <= 10 ** 12")
        continue
    if not (1 <= w <= 10 ** 9):
        print("помилка - 1 <= w <= 10 ** 9")
        continue
    if not (1 <= h <= 10 ** 9):
        print("помилка - 1 <= h <= 10 ** 9")
        continue

    left = 0
    right = n * max(w, h)
    itr = 0

    while right - left > 1:
        itr += 1
        mid = (left + right) // 2

        count = (mid // w) * (mid // h)

        if count >= n:
            right = mid
        else:
            left = mid

    print(f"кількість ітерацій - {itr}")
    print(f"розмір - {right}")