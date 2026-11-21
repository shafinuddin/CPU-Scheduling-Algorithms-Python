
def srtf(processes):
    n = len(processes)
    remaining = [p[2] for p in processes]
    completion = [0] * n
    time = 0
    completed = 0

    while completed < n:
        available = [
            i for i in range(n)
            if processes[i][1] <= time and remaining[i] > 0
        ]

        if not available:
            time += 1
            continue

        shortest = min(available, key=lambda i: remaining[i])
        remaining[shortest] -= 1
        time += 1

        if remaining[shortest] == 0:
            completion[shortest] = time
            completed += 1

    print("PID\tAT\tBT\tCT\tTAT\tWT")

    for i, (pid, at, bt) in enumerate(processes):
        tat = completion[i] - at
        wt = tat - bt
        print(f"{pid}\t{at}\t{bt}\t{completion[i]}\t{tat}\t{wt}")


processes = [
    ("P1", 0, 7),
    ("P2", 2, 4),
    ("P3", 4, 1),
    ("P4", 5, 4)
]

srtf(processes)
