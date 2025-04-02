import multiprocessing as mp
import time


def worker(r):
    pid = mp.current_process().name

    # do some hard and time consuming work:
    global result
    res = 0

    for i in r:
        res += i

    result += res

    print("Worker {} is working with {}".format(pid, r))


if __name__ == "__main__":
    # #################################################
    # # Sequential Processing:
    # #################################################
    # t = time.time()
    result = 0

    # worker(range(20_000_000))
    # worker(range(20_000_000, 40_000_000))

    # print("Sequential Processing result: ", result)
    # print("Sequential Processing took:", time.time() - t, "\n")

    #################################################
    # Multithreaded Processing:
    #################################################
    t = time.time()
    # Define an output queue
    # output = mp.Queue()

    p1 = mp.Process(target=worker, args=(range(20_000_000),))
    p2 = mp.Process(target=worker, args=(range(20_000_000, 40_000_000),))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Multiprocess Processing result: ", result)  # 799999980000000
    print("Multiprocess Processing took:", time.time() - t, "\n")
