# Import library wajibnya
import streamlit as st

# -- Konfigurasi Halaman (opsional, tapi bikin keren) --
# 'st.set_page_config' harus jadi perintah streamlit pertama yang dijalanin
st.set_page_config(
    page_title="Aplikasi Sederhana",
    page_icon="✨", # Bisa pake emoji
    layout="centered"
)

# -- Mulai Bikin Konten Halaman --

# 1. Judul Aplikasi
st.title("Contoh Aplikasi Streamlit Sederhana 🚀")
st.write("---") # Garis pemisah

# 2. Header dan Teks
st.header("Widget Interaktif")
st.write("Coba deh interaksi sama komponen di bawah ini.")

# 3. Input Teks
# st.text_input akan nampilin kotak buat ngetik dan nyimpen hasilnya ke variabel 'nama'
nama = st.text_input("Siapa nama kamu?")

# Cek kalo 'nama' udah diisi, baru tampilin pesan
if nama:
    st.write(f"Halo, **{nama}**! Selamat datang di dunia Streamlit.")

# 4. Slider (Penggeser Angka)
# st.slider akan bikin slider dari angka minimum ke maksimum
umur = st.slider("Berapa umur kamu?", min_value=0, max_value=100, value=25)
st.write(f"Wow, kamu berumur **{umur}** tahun.")
st.write("---")

# 5. Tombol (Button)
st.subheader("Coba Klik Tombol Ini")
# 'st.button' akan menghasilkan nilai True kalo tombolnya diklik
if st.button("Tampilkan pesan rahasia"):
    st.success("Kamu berhasil! Streamlit itu gampang dan asik kan? 😉")
    st.balloons() # Efek balon sebagai bonus!
else:
    st.info("Tombolnya belum diklik nih.")