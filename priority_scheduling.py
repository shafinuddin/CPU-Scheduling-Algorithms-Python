
def priority_scheduling(processes):
    processes = sorted(processes, key=lambda x: x[1])
    completed = []
    time = 0

    while len(completed) < len(processes):
        available = [
            p for p in processes
            if p[1] <= time and p not in completed
        ]

        if not available:
            time += 1
            continue

        process = min(available, key=lambda x: x[3])

        pid, at, bt, priority = process
        ct = time + bt
        tat = ct - at
        wt = tat - bt

        print(f"{pid}\t{at}\t{bt}\t{priority}\t{ct}\t{tat}\t{wt}")

        time = ct
        completed.append(process)


print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")

processes = [
    ("P1", 0, 5, 3),
    ("P2", 1, 3, 1),
    ("P3", 2, 8, 4),
    ("P4", 3, 6, 2)
]

priority_scheduling(processes)
