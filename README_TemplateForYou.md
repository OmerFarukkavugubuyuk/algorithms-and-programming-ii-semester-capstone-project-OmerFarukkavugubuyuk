# [Your Algorithm Name] - Interactive Visualization

## Project Overview

This project is an interactive web application that compares Merge Sort and Heap Sort algorithms with step-by-step visualizations, developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

[Provide a comprehensive explanation of your algorithm here. Include the following elements:]

### Problem Definition

Comparison of two efficient sorting algorithms (Merge Sort and Heap Sort) that both have O(n log n) time complexity but differ in space usage and implementation details.

### Mathematical Background
- **Merge Sort**: Divide-and-conquer approach with recurrence relation T(n) = 2T(n/2) + O(n)
- **Heap Sort**: Based on binary heap data structure with heapify operation O(log n)

### Algorithm Steps

**Merge Sort:**
1. Divide the unsorted list into n sublists
2. Recursively merge sublists to produce new sorted sublists
3. Repeat until there is only 1 sublist remaining

**Heap Sort:**
1. Build a max heap from the input data
2. Swap the root (maximum value) with the last item
3. Reduce heap size by 1 and heapify the root
4. Repeat until heap size is 1

### Pseudocode

**Merge Sort:**
function mergeSort(array)
if length(array) ≤ 1
return array
mid = length(array) / 2
left = mergeSort(array[0..mid])
right = mergeSort(array[mid..end])
return merge(left, right)

**Heap Sort:**
function heapSort(array)
buildMaxHeap(array)
for i = length(array) downto 2
swap(array[1], array[i])
heap_size = heap_size - 1
heapify(array, 1)

## Complexity Analysis

### Time Complexity

- **Best Case:** O(n log n) - Already sorted input
- **Average Case:** O(n log n) - Random input
- **Worst Case:** O(n log n) - Reverse sorted input

### Space Complexity

- **Merge Sort:** O(n) - Requires auxiliary space for merging
- **Heap Sort:** O(1) - Sorts in-place

## Features

- Interactive array input with comma-separated values
- Step-by-step visualization of sorting process
- Real-time performance metrics
- Time complexity comparison
- Responsive design for all devices

## Screenshots

![Main Interface](docs/screenshots/main_interface.png)
*Application interface with algorithm selection and array input*

![Algorithm Steps](docs/screenshots/algorithm_steps.png)
*Step-by-step visualization of Merge Sort*

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/FiratUniversity-IJDP-SoftEng/algorithms-and-programming-ii-semester-capstone-project-OmerFarukkavugubuyuk
   cd your-repository
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Select an algorithm (Merge Sort or Heap Sort)

2. Enter comma-separated numbers (e.g., "5,3,8,4,2")

3. Click "Sıralamayı Başlat" (Start Sorting)

4. View step-by-step sorting process

5. Analyze performance metrics

### Example Inputs

Input: 5,3,8,4,2

Merge Sort Output: [2, 3, 4, 5, 8] (12 steps)

Heap Sort Output: [2, 3, 4, 5, 8] (9 steps)

## Implementation Details

### Key Components

- `algorithm.py`: Contains the core algorithm implementation
- `app.py`: Main Streamlit application
- `utils.py`: Helper functions for data processing
- `visualizer.py`: Functions for visualization

### Code Highlights

```python
# Include a few key code snippets that demonstrate the most important parts of your implementation
def merge_sort(arr):
    """Merge Sort implementation with step tracking"""
    steps = [arr.copy()]
    if len(arr) <= 1:
        return arr, steps
    
    mid = len(arr) // 2
    left, left_steps = merge_sort(arr[:mid])
    right, right_steps = merge_sort(arr[mid:])
    
    merged = merge(left, right)
    return merged, steps + left_steps + right_steps + [merged]
```

## Testing

This project includes a test suite to verify the correctness of the algorithm implementation:

```bash
python -m unittest test_algorithm.py
```

### Test Cases

Empty array

Already sorted array

Reverse sorted array

Array with duplicate values

## Live Demo

A live demo of this application is available at: [Insert Streamlit Cloud URL here]

## Limitations and Future Improvements

### Current Limitations

Maximum array size limited to 100 elements

No parallel processing support

Limited visualization customization

### Planned Improvements

Implement parallel sorting

Enhanced visualization options

## References and Resources

### Academic References

Cormen, T.H. - Introduction to Algorithms

Knuth, D.E. - The Art of Computer Programming

### Online Resources

GeeksforGeeks Sorting Algorithms

Wikipedia: Merge Sort/Heap Sort

Claude ai

## Author

- **Name:** [Ömer Faruk Kavuğubüyük]
- **Student ID:** [230543015]
- **GitHub:** [OmerFarukkavugubuyuk]

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project, and the open source community for valuable resources.

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*
