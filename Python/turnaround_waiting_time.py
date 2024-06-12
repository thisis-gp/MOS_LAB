class Process: # Defines a class to represent a process with attributes pid, arrival_time, burst_time, and priority if provided.
    def __init__(self, pid, arrival_time, burst_time, priority=None):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

def fcfs(processes): # Implements First Come, First Served scheduling algorithm for given processes.
    processes.sort(key=lambda x: x.arrival_time)  # Sort processes by arrival time
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in range(n):
        if i == 0:
            waiting_time[i] = 0
        else:
            waiting_time[i] = waiting_time[i - 1] + processes[i - 1].burst_time
        turnaround_time[i] = waiting_time[i] + processes[i].burst_time
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n 
    return avg_waiting_time, avg_turnaround_time

def sjf(processes): # Implements Shortest Job First scheduling algorithm for given processes.
    processes.sort(key=lambda x: x.burst_time)  # Sort processes by burst time
    return fcfs(processes)

def priority(processes): # Implements Priority scheduling algorithm for given processes.
    processes.sort(key=lambda x: x.priority, reverse=True)  # Sort processes by priority
    return fcfs(processes)

def round_robin(processes, time_slice): # Implements Round Robin scheduling algorithm for given processes with a specified time slice.
    n = len(processes)
    burst_remaining = [p.burst_time for p in processes]
    waiting_time = 0
    turnaround_time = 0
    t = 0
    while True:
        done = True
        for i in range(n):
            if burst_remaining[i] > 0:
                done = False
                if burst_remaining[i] > time_slice:
                    t += time_slice
                    burst_remaining[i] -= time_slice
                else:
                    t += burst_remaining[i]
                    waiting_time += t - processes[i].burst_time
                    turnaround_time += t
                    burst_remaining[i] = 0
        if done:
            break
    avg_waiting_time = waiting_time / n
    avg_turnaround_time = turnaround_time / n
    return avg_waiting_time, avg_turnaround_time


if __name__ == "__main__":
    processes = [
        Process(3, 5, 4, 1),
        Process(4, 1, 8, 4),
        Process(3, 2, 3, 1),
        Process(2, 3, 6, 2)
    ]
    print("FCFS:")
    avg_waiting_time, avg_turnaround_time = fcfs(processes)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)
    print("\nSJF:")
    avg_waiting_time, avg_turnaround_time = sjf(processes)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)
    print("\nPriority:")
    avg_waiting_time, avg_turnaround_time = priority(processes)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)
    print("\nRound Robin:")
    avg_waiting_time, avg_turnaround_time = round_robin(processes, 2)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)
