import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
from algorithm import merge_sort, heap_sort

# Sayfa ayarları
st.set_page_config(page_title="Sıralama Algoritması Karşılaştırma", layout="wide")

# Başlık
st.title("🧮 Merge Sort vs Heap Sort Karşılaştırması")
st.markdown("---")

# Algoritma seçimi
algorithm = st.radio("Sıralama Algoritması Seçin:", 
                    ["Merge Sort", "Heap Sort"],
                    horizontal=True)

# Dizi girişi
user_input = st.text_input("Sıralanacak diziyi girin (virgülle ayırın):", 
                          "5,3,8,4,2,7,1,10")

try:
    arr = [int(x.strip()) for x in user_input.split(",")]
except:
    st.error("Geçersiz giriş! Lütfen sayıları virgülle ayırın (Örnek: 5,3,8,4)")
    st.stop()

# Sıralama butonu
if st.button("Sıralamayı Başlat"):
    st.markdown("---")
    
    # Sonuçlar için tab oluşturma
    tab1, tab2 = st.tabs(["Sıralama Adımları", "Performans Analizi"])
    
    with tab1:
        st.subheader(f"{algorithm} Sıralama Adımları")
        
        # Algoritmayı çalıştırma
        if algorithm == "Merge Sort":
            start_time = time.time()
            sorted_arr, steps = merge_sort(arr.copy())
            exec_time = time.time() - start_time
        else:
            start_time = time.time()
            sorted_arr, steps = heap_sort(arr.copy())
            exec_time = time.time() - start_time
        
        # Adımları gösterme
        for i, step in enumerate(steps, 1):
            st.markdown(f"**Adım {i}:**")
            st.dataframe(pd.DataFrame(step, columns=["Değer"]), hide_index=True)
        
        st.success(f"Sıralama tamamlandı! Toplam {len(steps)} adım.")
    
    with tab2:
        st.subheader("⏱️ Performans Analizi")
        
        col1, col2 = st.columns(2)
        col1.metric("Sıralama Süresi", f"{exec_time:.6f} saniye")
        
        # Big-O bilgisi
        col2.metric("Zaman Karmaşıklığı", "O(n log n)")
        
        # Karmaşıklık açıklaması
        st.markdown("### 📊 Karmaşıklık Analizi")
        st.markdown("""
        | Metrik          | Merge Sort | Heap Sort |
        |----------------|------------|-----------|
        | **En iyi durum**  | O(n log n) | O(n log n)|
        | **Ortalama**      | O(n log n) | O(n log n)|
        | **En kötü durum** | O(n log n) | O(n log n)|
        | **Bellek**        | O(n)       | O(1)      |
        """)
        
        # Grafik
        fig, ax = plt.subplots()
        ax.plot(range(len(steps)), [i+1 for i in range(len(steps))], 'b-')
        ax.set_xlabel("Adım Sayısı")
        ax.set_ylabel("İşlem Karmaşıklığı")
        ax.set_title("Algoritma Performansı")
        st.pyplot(fig)