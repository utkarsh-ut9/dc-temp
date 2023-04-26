
from multiprocessing import Process, Value
from time import sleep

n = 10
clock = [Value('i', 0) for i in range(n)]  # logical clocks for each process
request = [Value('i', 0) for i in range(n)]  # request flags for each process

# function to request for critical section
def request_cs(pid):
    # set request flag and update logical clock
    request[pid].value = 1
    clock[pid].value += 1
    # iterate through all processes and compare logical clocks to ensure correct process order
    for j in range(n):
        if j != pid:
            while request[j].value == 1:
                if clock[j].value < clock[pid].value:
                    clock[pid].value += 1
                elif (clock[j].value == clock[pid].value) and (j < pid):
                    clock[pid].value += 1
        else:
            break
    # enter critical section
    print(f"Process {pid} enters critical section at {clock[pid].value}")
    sleep(1)  # simulate critical section
    # exit critical section and reset request flag
    print(f"Process {pid} exits critical section")
    request[pid].value = 0

if __name__ == '__main__':
    # create processes and start them
    processes = [Process(target=request_cs, args=(i,)) for i in range(n)]
    for p in processes:
        p.start()
    # wait for all processes to finish
    for p in processes:
        p.join()