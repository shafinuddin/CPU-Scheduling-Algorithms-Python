CPU Scheduling Algorithms in Python

A Python-based implementation of four fundamental CPU Scheduling Algorithms used in Operating Systems. This project demonstrates how the CPU allocates processing time to different processes and calculates their scheduling performance.

📌 Algorithms Implemented

FCFS (First Come First Serve)

Non-preemptive scheduling algorithm.

Executes processes according to their arrival time.

SRTF (Shortest Remaining Time First)

Preemptive scheduling algorithm.

Selects the process with the shortest remaining burst time.

Round Robin Scheduling

Preemptive scheduling algorithm.

Allocates a fixed time quantum to each process.

Uses a ready queue to manage processes.

Priority Scheduling

Non-preemptive scheduling algorithm.

Executes the available process with the highest priority.

A smaller priority number represents a higher priority.

🛠️ Technologies Used

Programming Language: Python

IDE: Visual Studio Code

Version Control: Git & GitHub

📂 Project Structure
CPU-Scheduling-Algorithms-Python/
│
├── fcfs.py
├── srtf.py
├── round_robin.py
├── priority_scheduling.py
│
└── README.md
📖 Scheduling Terminologies

Term

Description

PID

Process ID

AT

Arrival Time

BT

Burst Time

CT

Completion Time

TAT

Turnaround Time

WT

Waiting Time

🧮 Formulas Used

Turnaround Time (TAT)

TAT = Completion Time - Arrival Time

Waiting Time (WT)

WT = Turnaround Time - Burst Time

Completion Time (CT)

CT = Start Time + Burst Time

For preemptive algorithms, completion time is recorded when the process finishes its final execution.

🚀 How to Run the Project

Step 1: Clone the Repository

git clone https://github.com/YOUR-USERNAME/CPU-Scheduling-Algorithms-Python.git

Step 2: Navigate to the Project Directory

cd CPU-Scheduling-Algorithms-Python

Step 3: Run the Algorithms

Run each Python file separately:

FCFS

python fcfs.py

SRTF

python srtf.py

Round Robin

python round_robin.py

Priority Scheduling

python priority_scheduling.py

No external Python libraries are required. Round Robin uses Python's built-in collections module.
📊 Comparison of Algorithms

Algorithm

Scheduling Type

Selection Criteria

FCFS

Non-Preemptive

Arrival Time

SRTF

Preemptive

Shortest Remaining Time

Round Robin

Preemptive

Time Quantum

Priority

Non-Preemptive

Process Priority

🎯 Project Objectives

Understand the fundamentals of CPU scheduling.

Implement different scheduling algorithms using Python.

Calculate Completion Time, Turnaround Time, and Waiting Time.

Compare preemptive and non-preemptive scheduling techniques.

Develop practical knowledge of Operating System concepts.

👨‍💻 Author

Shafin Uddin
Computer Science and Engineering (CSE)
University of Science and Technology Chittagong (USTC)

📜 License

This project is open-source and available for educational and learning purposes under the MIT License.
