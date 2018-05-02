def clock_in(worker_dict, name, clock_in_time):
    worker_info = worker_dict.get(name)
    worker_info[0] = clock_in_time
    worker_dict[name] = worker_info

def clock_out(worker_dict, name, clock_out_time):
    worker_info = worker_dict.get(name)
    worker_info[1] = clock_out_time
    worker_info[2] = worker_info[1] - worker_info[0]
    worker_dict[name] = worker_info

def main():
    workers = {"George Spelvin": [0,0,0], "Jane Doe": [0,0,0], "John Smith": [0,0,0]}
    print(workers.get("George Spelvin"))   # should print [0,0,0]
    clock_in(workers, "George Spelvin", 8)
    clock_out(workers, "George Spelvin", 17)
    print(workers.get("George Spelvin"))   # should print [8, 17, 9]

if __name__ == "__main__":
    main()
