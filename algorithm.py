# deneme-algorithm.py

def merge_sort(arr):
    steps = []
    
    def merge_sort_recursive(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(arr, left, mid)
            merge_sort_recursive(arr, mid + 1, right)
            merge(arr, left, mid, right)
            steps.append(arr.copy())  # Her bir birleşmeden sonra durumu kaydet

    def merge(arr, left, mid, right):
        left_part = arr[left:mid+1]
        right_part = arr[mid+1:right+1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1

    temp_arr = arr.copy()
    merge_sort_recursive(temp_arr, 0, len(temp_arr) - 1)
    return temp_arr, steps


def heap_sort(arr):
    steps = []

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps.append(arr.copy())  # Swap sonrası durumu kaydet
            heapify(arr, n, largest)

    temp_arr = arr.copy()
    n = len(temp_arr)

    # Max heap oluştur
    for i in range(n // 2 - 1, -1, -1):
        heapify(temp_arr, n, i)

    # Heap'ten çıkar
    for i in range(n - 1, 0, -1):
        temp_arr[i], temp_arr[0] = temp_arr[0], temp_arr[i]
        steps.append(temp_arr.copy())  # Her swap sonrası
        heapify(temp_arr, i, 0)

    return temp_arr, steps
