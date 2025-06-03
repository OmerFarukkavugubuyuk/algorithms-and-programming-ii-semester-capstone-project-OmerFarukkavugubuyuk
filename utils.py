import matplotlib.pyplot as plt
import streamlit as st

def plot_list(arr, title=""):
    plt.figure(figsize=(10, 4))
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.ylim(0, max(arr) * 1.1)  # Grafiğin üst sınırı biraz boşluk bırakacak
    st.pyplot(plt)
    plt.clf()  # Grafik temizle
