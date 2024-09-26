# Helper function to swap elements in the list
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Partition function with pivot as the middle element
def partition(arr, begin, end, size):
    stage = 0  # Static variable equivalent in Python
    pivot = (begin + end) // 2
    L = begin
    R = end
    print(f"\n[{stage + 1} stage: pivot = {pivot}] \n")

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
    print(f"Returning pivot index: {R}\n")
    
    return R

# Quick Sort function with recursion
def quick_sort(arr, begin, end, size):
    if begin < end:
        p = partition(arr, begin, end, size)
        quick_sort(arr, begin, p - 1, size)  # Recursively sort left
        quick_sort(arr, p + 1, end, size)    # Recursively sort right

# Print array helper function
def print_array(arr):
    print("Array:", arr)

# Sample Code
if __name__ == "__main__":
    arr = [42, 20, 17, 13, 28, 14, 23, 15]
    size = len(arr)
    print("Initial array:")
    print_array(arr)
    
    quick_sort(arr, 0, size - 1, size)
    
    print("Sorted array:")
    print_array(arr)