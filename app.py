import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
from algorithm import merge_sort, heap_sort

# Page settings and Layout
st.set_page_config(page_title="Sorting Algorithm Comparison", layout="wide")

# Title
st.title("🧮 Comparison of Merge and Heap Sort")
st.markdown("---")

# Choose sorting algorithm
algorithm = st.radio("Choose a Sorting Algorithm:", 
                    ["Merge Sort", "Heap Sort"],
                    horizontal=True)

# Entering the array to sort
user_input = st.text_input("Enter the array to sort (separate with commas):", 
                          "5,3,8,4,2,7,1,10")

try:
    array = [int(x.strip()) for x in user_input.split(",")]
except:
    st.error("Invalid Input Please Seperate Numbers With Commas (Example: 5,3,8,4)")
    st.stop()

# Sorting button
if st.button("Start Sorting"):
    st.markdown("### 📊 Sorting Steps")
    st.markdown("---")
    
    # Making table for results
    tab1, tab2 = st.tabs(["Steps of Sorting", "Performance Analysis"])
    
    with tab1:
        st.subheader(f"{algorithm} Steps of Sorting")
        
        # Running the selected sorting algorithm
        if algorithm == "Merge Sort":
            start_time = time.time()
            sorted_arr, steps = merge_sort(array.copy())
            exec_time = time.time() - start_time
        else:
            start_time = time.time()
            sorted_arr, steps = heap_sort(array.copy())
            exec_time = time.time() - start_time
        
        # Showing steps
        for i, step in enumerate(steps, 1):
            st.markdown(f"**Step {i}:**")
            st.dataframe(pd.DataFrame(step, columns=["Value"]), hide_index=True)
        
        st.success(f"Sorting complete! Total {len(steps)} steps.")
    
    with tab2:
        st.subheader("⏱️ Performance Analysis")
        
        col1, col2 = st.columns(2)
        col1.metric("Sorting Time", f"{exec_time:.6f} seconds")
        
        # Big-O information
        col2.metric("Time Complexity", "O(n log n)")
        
        # Explanation of complexity 
        st.markdown("### 📊 Complexity Analysis")
        st.markdown("""
        | Metrik          | Merge Sort | Heap Sort |
        |----------------|------------|-----------|
        | **Best Case**  | O(n log n) | O(n log n)|
        | **Average**      | O(n log n) | O(n log n)|
        | **Worst Case** | O(n log n) | O(n log n)|
        | **Memory**        | O(n)       | O(1)      |
        """)
        
        # Chart
        fig, ax = plt.subplots()
        ax.plot(range(len(steps)), [i+1 for i in range(len(steps))], 'b-')
        ax.set_xlabel("Number of Steps")
        ax.set_ylabel("Process Complexity")
        ax.set_title("Algorithm Performance")
        st.pyplot(fig)