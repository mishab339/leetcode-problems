def insert(heap, value):
    # Add the new element to the end of the heap
    heap.append(value)
    
    # Get the index of the last element
    index = len(heap) - 1
    # Compare the new element with
    # its parent and swap if necessary
    while index > 0 and heap[(index - 1) // 2] > heap[index]:
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        # Move up the tree to the
        # parent of the current element
        index = (index - 1) // 2

    
if __name__ == "__main__":
    arr = []
    values = [10, 3, 2, 4, 5, 1]
    n = len(values)
    for i in range(n):
        insert(arr, values[i])
        print(f"Inserted {values[i]} into the min-heap: ", end="")
        for j in range(len(arr)):
            print(arr[j], end=" ")
        print()