"""Merge Sort and Quick Sort (Cormen et al., 2022, Chapters 2 and 7)."""
import random


def merge_sort(a, low=0, high=None):
    """Sort a[low:high] in place using merge sort."""
    if high is None:
        high = len(a)
    # A slice with zero or one element is already sorted
    if low + 1 >= high:
        return a
    mid = (low + high) // 2
    merge_sort(a, low, mid)        # divide: sort the left half
    merge_sort(a, mid, high)       # divide: sort the right half
    merge(a, low, mid, high)       # combine: merge the two halves
    return a


def merge(a, low, mid, high):
    """Merge the sorted runs a[low:mid] and a[mid:high]."""
    left = a[low:mid]              # copy of left run (extra memory)
    right = a[mid:high]            # copy of right run (extra memory)
    i = j = 0
    k = low
    # Repeatedly copy the smaller front element back into a
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:    # <= keeps the sort stable
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    # Copy whatever is left over from either run
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def partition(a, low, high):
    """Partition a[low:high] around the pivot a[low] and return its index."""
    pivot = a[low]
    i = low                        # end of the "less than or equal" region
    for j in range(low + 1, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[low], a[i] = a[i], a[low]    # place pivot in its final spot
    return i


def quick_sort(a, low=0, high=None, randomized=False):
    """Sort a[low:high] in place using quick sort.

    The pivot is the first element unless randomized is True.
    The loop recurses on the smaller side and iterates on the larger
    side so the stack depth stays O(log n) (Cormen et al., 2022, Problem 7.4).
    """
    if high is None:
        high = len(a)
    while low + 1 < high:
        if randomized:
            r = random.randrange(low, high)
            a[low], a[r] = a[r], a[low]
        p = partition(a, low, high)
        # Recurse into the smaller part, loop on the larger part
        if p < (low + high) // 2:
            quick_sort(a, low, p, randomized)
            low = p + 1
        else:
            quick_sort(a, p + 1, high, randomized)
            high = p
    return a


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Merge sort:", merge_sort(data.copy()))
    print("Quick sort:", quick_sort(data.copy()))
    print("Randomized quick sort:", quick_sort(data.copy(), randomized=True))
