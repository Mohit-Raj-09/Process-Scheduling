# FCFS - First Come First Serve
def fcfs(processes):
    time = 0
    result = []
    for p in processes:
        p['start_time'] = time
        p['completion_time'] = time + p['burst_time']
        time += p['burst_time']
        result.append(p)
    return result

# SJF - Shortest Job First (Non-preemptive)
def sjf(processes):
    processes.sort(key=lambda x: x['burst_time'])
    time = 0
    result = []
    for p in processes:
        p['start_time'] = time
        p['completion_time'] = time + p['burst_time']
        time += p['burst_time']
        result.append(p)
    return result

# Priority Scheduling (Non-preemptive)
def priority_scheduling(processes):
    processes.sort(key=lambda x: x['priority'])
    time = 0
    result = []
    for p in processes:
        p['start_time'] = time
        p['completion_time'] = time + p['burst_time']
        time += p['burst_time']
        result.append(p)
    return result

# RR - Round Robin Scheduling
def round_robin(processes, quantum):
    time = 0
    queue = processes.copy()
    result = []
    while queue:
        p = queue.pop(0)
        run_time = min(p['burst_time'], quantum)
        p['start_time'] = time
        time += run_time
        p['burst_time'] -= run_time
        if p['burst_time'] > 0:
            queue.append(p)
        else:
            p['completion_time'] = time
            result.append(p)
    return result