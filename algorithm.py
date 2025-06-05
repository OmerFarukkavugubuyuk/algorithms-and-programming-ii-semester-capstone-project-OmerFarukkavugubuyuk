def merge_sort(arr):
    steps = [arr.copy()]
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
    
    if len(arr) <= 1:
        return arr, steps
    
    mid = len(arr) // 2
    left, left_steps = merge_sort(arr[:mid])
    right, right_steps = merge_sort(arr[mid:])
    
    # Tüm adımları birleştirme
    all_steps = steps + left_steps + right_steps
    merged = merge(left, right)
    all_steps.append(merged)
    
    return merged, all_steps

def heap_sort(arr):
    steps = [arr.copy()]
    n = len(arr)
    
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps.append(arr.copy())
            heapify(arr, n, largest)
    
    # Max heap oluşturma
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Heap'ten eleman çıkarma
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps.append(arr.copy())
        heapify(arr, i, 0)
    
    return arr, steps