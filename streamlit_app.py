import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pymysql
import time

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Premium Kasir Dashboard",
    page_icon="💎",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>

/* Background */
.stApp {
    background: #0f172a;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#111827,#1e293b);
    animation: fadeIn 1s ease-in;
}

/* Card */
.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
}

/* Navbar */
.navbar {
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 20px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: white;
}

/* Animation */
@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGIN SYSTEM
# =========================================
USERNAME = "admin"
PASSWORD = "123"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    st.title("🔐 Login Kasir")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("LOGIN"):

        if username == USERNAME and password == PASSWORD:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Username / Password salah")

    st.stop()

# =========================================
# NAVBAR
# =========================================
st.markdown("""
<div class="navbar">
💎 PREMIUM KASIR DASHBOARD
</div>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR MENU
# =========================================
menu = st.sidebar.radio(
    "MENU",
    [
        "🏠 Dashboard",
        "🛒 Kasir",
        "📊 Analytics",
        "📂 Upload File",
        "🤖 AI Chatbot",
        "🗄 Database"
    ]
)

# =========================================
# DASHBOARD
# =========================================
if menu == "🏠 Dashboard":

    st.title("Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>Total Produk</h3>
        <h1>120</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>Total Penjualan</h3>
        <h1>Rp 12 Jt</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>Total Customer</h3>
        <h1>340</h1>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
        <h3>Total Transaksi</h3>
        <h1>890</h1>
        </div>
        """, unsafe_allow_html=True)

# =========================================
# KASIR
# =========================================
elif menu == "🛒 Kasir":

    st.title("Menu Kasir")

    produk = st.selectbox(
        "Pilih Produk",
        ["Laptop", "Mouse", "Keyboard"]
    )

    qty = st.number_input("Jumlah", 1, 100)

    harga = {
        "Laptop": 7000000,
        "Mouse": 100000,
        "Keyboard": 250000
    }

    total = harga[produk] * qty

    st.success(f"Total Bayar : Rp {total:,}")

    if st.button("Simpan Transaksi"):
        st.success("Transaksi berhasil disimpan")

# =========================================
# ANALYTICS
# =========================================
elif menu == "📊 Analytics":

    st.title("Realtime Analytics")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Penjualan', 'Profit', 'Customer']
    )

    st.line_chart(chart_data)

    # Plotly Chart
    data = pd.DataFrame({
        "Bulan": ["Jan","Feb","Mar","Apr","Mei"],
        "Penjualan": [10,20,15,30,40]
    })

    fig = px.bar(
        data,
        x="Bulan",
        y="Penjualan",
        color="Penjualan"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================
# UPLOAD FILE
# =========================================
elif menu == "📂 Upload File":

    st.title("Upload Excel & PDF")

    uploaded = st.file_uploader(
        "Upload File",
        type=["xlsx", "pdf"]
    )

    if uploaded:

        st.success("File berhasil diupload")

        if uploaded.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded)
            st.dataframe(df)

# =========================================
# AI CHATBOT
# =========================================
elif menu == "🤖 AI Chatbot":

    st.title("AI Chatbot")

    pertanyaan = st.text_input("Tanya AI")

    if pertanyaan:

        jawaban = f"""
        Anda bertanya:
        {pertanyaan}

        Ini jawaban AI sederhana menggunakan Streamlit.
        """

        st.info(jawaban)

# =========================================
# MYSQL DATABASE
# =========================================
elif menu == "🗄 Database":

    st.title("Koneksi MySQL")

    host = st.text_input("Host", "localhost")
    user = st.text_input("User", "root")
    password = st.text_input("Password", type="password")
    database = st.text_input("Database")

    if st.button("Connect"):

        try:
            conn = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            st.success("Berhasil connect MySQL")

        except Exception as e:
            st.error(e)
