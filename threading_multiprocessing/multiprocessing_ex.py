import multiprocessing


def compute(name):
    print(f"{name} started")
    total = 0
    for i in range(10**7):  # Simulate CPU-heavy work
        total += i
    print(f"{name} finished with total {total}")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=compute, args=("Process-1",))
    p2 = multiprocessing.Process(target=compute, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Multiprocessing example done.")
