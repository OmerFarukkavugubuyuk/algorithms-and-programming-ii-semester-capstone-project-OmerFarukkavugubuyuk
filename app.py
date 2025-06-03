import streamlit as st
from algorithm import merge_sort, heap_sort
from utils import plot_list
import time

st.title("Merge Sort vs Heap Sort Karşılaştırma")

# Kullanıcıdan liste al
input_list_str = st.text_input("Sıralanacak sayıları virgülle girin (örnek: 5,3,8,1,2)", "5,3,8,1,2")
try:
    input_list = list(map(int, input_list_str.strip().split(',')))
except:
    st.error("Lütfen sadece sayı ve virgül kullanarak listeyi doğru formatta girin.")
    st.stop()

# Algoritma seçimi
algorithm = st.selectbox("Algoritma seçin", ["Merge Sort", "Heap Sort"])

# Adım adım gösterim seçeneği
step_by_step = st.checkbox("Adım adım göster")

if st.button("Sıralamayı Başlat"):
    if algorithm == "Merge Sort":
        sorted_list, steps = merge_sort(input_list)
    else:
        sorted_list, steps = heap_sort(input_list)

    st.write("**Sıralanmış Liste:**", sorted_list)

    if step_by_step:
        st.write("**Adımlar:**")
        for i, step in enumerate(steps):
            st.write(f"Adım {i+1}:")
            plot_list(step, title=f"Adım {i+1}")
            time.sleep(0.7)
    else:
        st.write("Adım adım gösterim seçilmedi, sadece sonuç gösterildi.")
