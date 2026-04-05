with open('input.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0].split('#')[0])
sx, sy = map(int, lines[1].split('#')[0].split(','))
tx, ty = map(int, lines[2].split('#')[0].split(','))

q = [(sx, sy, 0)]
vis = set()
vis.add((sx, sy))

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, 1, -1, 2, -2, 2, -2]

ans = -1

while len(q) > 0:
    x, y, d = q.pop(0)

    if x == tx and y == ty:
        ans = d
        break

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in vis:
            vis.add((nx, ny))
            q.append((nx, ny, d + 1))

with open('output.txt', 'w') as f:
    f.write(str(ans))