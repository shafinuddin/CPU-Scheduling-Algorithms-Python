
def fcfs(processes):
    processes.sort(key=lambda x: x[1])
    current_time = 0

    print("PID\tAT\tBT\tCT\tTAT\tWT")

    for pid, at, bt in processes:
        start = max(current_time, at)
        ct = start + bt
        tat = ct - at
        wt = tat - bt
        current_time = ct

        print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")


processes = [
    ("P1", 0, 5),
    ("P2", 1, 3),
    ("P3", 2, 8),
    ("P4", 3, 6)
]

fcfs(processes)
