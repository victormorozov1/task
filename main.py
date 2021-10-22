dp = {}

for f in range(300, 0, -1):
    for s in range(300, 0, -1):
        dp[f, s] = [False, 0, 0]
        if f + s >= 69:
            continue

        steps = [(f + 1, s), (f, s + 1), (f * 2, s), (f, s * 3)]

        win_steps = []
        for step in steps:
            if not dp[step][0]:
                win_steps.append(step)

        if not win_steps:
            dp[f, s][1] = min([dp[step][1] for step in steps]) + 1
            dp[f, s][2] = max([dp[step][2] for step in steps]) + 1
            continue

        dp[f, s][0] = True
        dp[f, s][1] = min([dp[step][1] for step in win_steps]) + 1
        dp[f, s][2] = min([dp[step][2] for step in win_steps]) + 1

for i in range(1, 80):
    print(i, end=' ' * (4 - len(str(i))))
print()
for s in range(1, 80):
    print(int(dp[10, s][0]), end=' ' * 3)
print()
for s in range(1, 80):
    print(dp[10, s][1], end=' ' * (4 - len(str(dp[10, s][1]))))
print()
for s in range(1, 80):
    print(dp[10, s][2], end=' ' * (4 - len(str(dp[10, s][2]))))
