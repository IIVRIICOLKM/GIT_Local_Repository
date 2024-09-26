# Stack structure for holding start and finish indices
class QS:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

# Swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Partition function (modified with ascending order check)
def partition(arr, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    print(f"\n[Stage: pivot = {pivot}] \n")

    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1
        while arr[R] >= arr[pivot] and L < R:
            R -= 1

        if L < R:
            swap(arr, L, R)
            print(f"Swapped {arr[L]} and {arr[R]}")
            if L == pivot:
                pivot = R

    swap(arr, pivot, R)
    print(f"Pivot swapped with {arr[R]}")
    print("Array after partition:", arr)
    
    return R

# sortedCheck_ASC: Check if the array is sorted in ascending order
def sortedCheck_ASC(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

# Non-recursive Quick Sort implementation
def quick_sort_non_recursive(arr):
    quickSortStack = []
    start = 0
    finish = len(arr) - 1
    pivot = partition(arr, start, finish)
    
    while True:
        # When partitioning is possible (i.e., there are unsorted elements)
        if start + 1 < finish:
            if start < pivot - 1 and finish <= pivot + 1:
                print("Left partition")
                finish = pivot - 1
            elif start >= pivot - 1 and finish > pivot + 1:
                print("Right partition")
                start = pivot + 1
            else:
                print("Both partitions")
                quickSortStack.append(QS(pivot + 1, finish))
                finish = pivot - 1
        # No more partitions available
        else:
            if quickSortStack:
                print("Pop from stack (LIFO)")
                segment = quickSortStack.pop()
                start = segment.start
                finish = segment.finish
            else:
                break

        # Repartition with the new segment
        pivot = partition(arr, start, finish)

        # If the array is fully sorted, break the loop
        if sortedCheck_ASC(arr):
            print("\nSorting complete\n")
            break

# Example usage
if __name__ == "__main__":
    arr = [42, 20, 17, 13, 28, 14, 23, 15]
    print("Initial array:", arr)
    
    quick_sort_non_recursive(arr)
    
    print("Sorted array:", arr)