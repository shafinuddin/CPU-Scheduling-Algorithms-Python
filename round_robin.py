
from collections import deque

def round_robin(processes, quantum):
    n = len(processes)
    processes.sort(key=lambda x: x[1])

    remaining = {p[0]: p[2] for p in processes}
    completion = {}
    queue = deque()
    time = 0
    i = 0

    while i < n or queue:
        if not queue and i < n:
            time = max(time, processes[i][1])
            queue.append(processes[i][0])
            i += 1

        pid = queue.popleft()
        execution = min(quantum, remaining[pid])
        time += execution
        remaining[pid] -= execution

        while i < n and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completion[pid] = time

    print("PID\tAT\tBT\tCT\tTAT\tWT")

    for pid, at, bt in processes:
        tat = completion[pid] - at
        wt = tat - bt
        print(f"{pid}\t{at}\t{bt}\t{completion[pid]}\t{tat}\t{wt}")


processes = [
    ("P1", 0, 5),
    ("P2", 1, 4),
    ("P3", 2, 2),
    ("P4", 3, 1)
]

round_robin(processes, 2)
