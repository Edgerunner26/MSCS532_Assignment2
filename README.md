# MSCS532_Assignment2

Merge Sort and Quick Sort in Python, with a benchmark that compares them on
sorted, reverse sorted, and random data (Cormen et al., 2022, Chapters 2 and 7).

## Files
| File | Purpose |
|------|---------|
| `sorting.py` | Merge Sort, Quick Sort (first element pivot), and randomized Quick Sort |
| `benchmark.py` | Times each algorithm (median of 3 runs) and measures peak memory with `tracemalloc`; writes `results.csv` |
| `plot_results.py` | Builds `runtime_chart.png` from `results.csv` |

## Run
    pip install matplotlib
    python sorting.py
    python benchmark.py
    python plot_results.py

## Summary of results (n = 8,000)
| Algorithm | Sorted | Reverse | Random |
|-----------|-------:|--------:|-------:|
| Merge Sort | 9.41 ms | 9.40 ms | 11.50 ms |
| Quick Sort | 641.54 ms | 1,095.34 ms | 6.20 ms |
| Randomized Quick Sort | 7.39 ms | 7.22 ms | 7.97 ms |

Fixed pivot Quick Sort hits its Θ(n²) worst case on ordered data. Merge Sort is
Θ(n lg n) on every input but uses Θ(n) extra memory.

## Reference
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction
to algorithms (4th ed.). Random House Publishing Services.
