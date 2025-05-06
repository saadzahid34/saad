![image](https://github.com/user-attachments/assets/d34ea48f-1c8d-4f2d-9425-501f7ca743aa) Printing Task Scheduler – SJF (Non-Preemptive Algorithm)

Project Description

This project simulates a Printing Task Scheduler using the Shortest Job First (SJF) Non-Preemptive Scheduling Algorithm. The program schedules print jobs based on their arrival time and burst time (duration required for printing), optimizing the average waiting timeand turnaround time.

This scheduling strategy ensures that shorter tasks are executed first, improving system efficiency and reducing the time jobs spend in the queue.

Core Logic

-SJF Non-Preemptive Algorithm:  
  - Selects the job with the shortest burst time from the set of available jobs.
  - Once selected, a job runs to completion before the next one begins.


Code Structure & Explanation

Main Components:
- `calculate_waiting_time()` – Calculates waiting times for all tasks.
- `calculate_turnaround_time()` – Calculates turnaround times.
- `sjf_scheduling()` – Main function to implement the SJF logic and output results.
- `print_table()` – (Optional) Uses `tabulate` for pretty formatting.

External Libraries Used:
- `tabulate` – Used to display output in a clean table format. Install using:
  ```bash
  pip install tabulate
