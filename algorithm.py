def merge_sort(array):
    steps = [array.copy()]
    comparisons = 0
    swaps = 0
    
    def merge(left, right):
        nonlocal comparisons, swaps
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            swaps += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    if len(array) <= 1:
        return array, steps
    
    mid = len(array) // 2
    left, left_steps = merge_sort(array[:mid])
    right, right_steps = merge_sort(array[mid:])
    
    # Combine all steps
    all_steps = steps + left_steps + right_steps
    merged = merge(left, right)
    all_steps.append(merged)
    
    return merged, all_steps

def heap_sort(array):
    steps = [array.copy()]
    n = len(array)
    
    def heapify(arrayHeapify, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arrayHeapify[left] > arrayHeapify[largest]:
            largest = left
        
        if right < n and arrayHeapify[right] > arrayHeapify[largest]:
            largest = right
        
        if largest != i:
            arrayHeapify[i], arrayHeapify[largest] = arrayHeapify[largest], arrayHeapify[i]
            steps.append(arrayHeapify.copy())
            heapify(arrayHeapify, n, largest)
    
    # Creating max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)
    
    # Removing elements from the heap
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        steps.append(array.copy())
        heapify(array, i, 0)
    
    return array, steps