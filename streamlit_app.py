import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Saya",
    page_icon="🏠",
    layout="wide"
)

# Sidebar menu
menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Home", "Tentang"]
)

# Halaman Home
if menu == "Home":
    st.title("🏠 Home")
    st.write("Selamat datang di aplikasi Streamlit saya!")

    col1, col2 = st.columns(2)

    with col1:
        st.info("Ini contoh kolom kiri")

    with col2:
        st.success("Ini contoh kolom kanan")

    st.button("Klik Saya")

# Halaman Tentang
elif menu == "Tentang":
    st.title("📖 Tentang")
    st.write("""
    Aplikasi ini dibuat menggunakan Streamlit.

    Fitur:
    - Menu navigasi
    - Tampilan responsif
    - Mudah dikembangkan
    """)

    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",
        width=250
    )
