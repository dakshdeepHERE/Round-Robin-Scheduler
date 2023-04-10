from collections import deque

def round_robin(q1, q2):
    time = 0
    quantum = 3
    waiting_time = {}
    while q1 or q2:
        if q1:
            p = q1.popleft()
            if p[1] > quantum:
                time += quantum
                p[1] -= quantum
                q1.append(p)
            else:
                time += p[1]
                if p[0] not in waiting_time:
                    waiting_time[p[0]] = time - p[1]
                else:
                    waiting_time[p[0]] += time - p[1]
                print(f"Process {p[0]} finished at {time}")
        elif q2:
            p = q2.popleft()
            if p[1] > quantum:
                time += quantum
                p[1] -= quantum
                q2.append(p)
            else:
                time += p[1]
                if p[0] not in waiting_time:
                    waiting_time[p[0]] = time - p[1]
                else:
                    waiting_time[p[0]] += time - p[1]
                print(f"Process {p[0]} finished at {time}")
        else:
            break
    return sum(waiting_time.values()) / len(waiting_time)

print("All the processes with priority 0 will be pushed into the queue 1 i.e. Teacher's queue and all the processes "
      "which will have priority 1 will pushed into the student's queue")
print("Make sure you give teacher's process priority 0 and student's process priority is 1")
q1 = deque() #Teacher's queue
q2 = deque() #Student's queue
n = int(input("Enter the number of processes: "))
for i in range(n):
    bt = int(input(f"Enter burst time for process {i+1}: "))
    priority = int(input(f"Enter priority for process {i+1}: "))
    if priority == 0:
        q1.append([i+1, bt])
    else:
        q2.append([i+1, bt])
avg_waiting_time = round_robin(q1, q2)
print(f"Average Waiting Time: {avg_waiting_time}")
