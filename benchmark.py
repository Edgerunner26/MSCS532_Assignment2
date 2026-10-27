"""Benchmark merge sort and quick sort on sorted, reverse, and random data."""
import csv
import random
import statistics
import time
import tracemalloc

from sorting import merge_sort, quick_sort

SIZES = [500, 1000, 2000, 4000, 8000]
REPEATS = 3
ALGORITHMS = {
    "Merge Sort": lambda a: merge_sort(a),
    "Quick Sort": lambda a: quick_sort(a),
    "Randomized Quick Sort": lambda a: quick_sort(a, randomized=True),
}


def make_data(kind, n):
    """Build a test list of size n."""
    if kind == "sorted":
        return list(range(n))
    if kind == "reverse":
        return list(range(n, 0, -1))
    rng = random.Random(42 + n)    # fixed seed for repeatable results
    return [rng.randint(0, 10 * n) for _ in range(n)]


def time_run(func, data):
    """Return the median run time in milliseconds."""
    times = []
    for _ in range(REPEATS):
        a = data.copy()
        start = time.perf_counter()
        func(a)
        times.append((time.perf_counter() - start) * 1000)
        assert a == sorted(data)   # check correctness every run
    return statistics.median(times)


def peak_memory(func, data):
    """Return peak extra memory in KiB measured with tracemalloc."""
    a = data.copy()
    tracemalloc.start()
    func(a)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024


def main():
    rows = []
    for kind in ["sorted", "reverse", "random"]:
        for n in SIZES:
            data = make_data(kind, n)
            for name, func in ALGORITHMS.items():
                ms = time_run(func, data)
                kib = peak_memory(func, data)
                rows.append([name, kind, n, round(ms, 2), round(kib, 1)])
                print(f"{name:22} {kind:8} n={n:5}  {ms:9.2f} ms  {kib:8.1f} KiB")
    with open("results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["algorithm", "dataset", "n", "time_ms", "peak_kib"])
        w.writerows(rows)


if __name__ == "__main__":
    main()
