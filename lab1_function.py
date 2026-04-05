def arr(a):
    n = len(a)
    if n < 2:
        return (-1,-1)

    l = 0
    while l < n - 1 and a[l] <= a[l + 1]:
        l += 1
    if l == n - 1:
        return (-1,-1)

    r = n - 1
    while r > 0 and a[r] >= a[r - 1]:
        r -= 1

    windowmin = min(a[l:r + 1])
    windowmax = max(a[l:r + 1])

    while l > 0 and a[l - 1] > windowmin:
        l -= 1
    while r < n - 1 and a[r + 1] < windowmax:
        r += 1

    return (l, r)

