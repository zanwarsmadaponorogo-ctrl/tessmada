import streamlit as st
import pandas as pd
import numpy as np

# ==================================
# PAGE CONFIG
# ==================================
st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ==================================
# CUSTOM CSS
# ==================================
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #0f172a;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Card */
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    text-align: center;
}

/* Title */
.title {
    font-size: 40px;
    font-weight: bold;
    color: white;
}

/* Text */
.small-text {
    color: #94a3b8;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR
# ==================================
st.sidebar.title("📌 MENU")

menu = st.sidebar.radio(
    "Navigasi",
    ["🏠 Home", "📊 Dashboard", "📖 Tentang"]
)

# ==================================
# HOME
# ==================================
if menu == "🏠 Home":

    st.markdown(
        '<p class="title">🚀 Home Page</p>',
        unsafe_allow_html=True
    )

    st.write("Selamat datang di aplikasi dashboard modern.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>👥 Users</h3>
            <h1>2,540</h1>
            <p class="small-text">Total pengguna</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>💰 Revenue</h3>
            <h1>Rp 24 Jt</h1>
            <p class="small-text">Pendapatan bulan ini</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>📦 Orders</h3>
            <h1>1,240</h1>
            <p class="small-text">Total pesanan</p>
        </div>
        """, unsafe_allow_html=True)

# ==================================
# DASHBOARD
# ==================================
elif menu == "📊 Dashboard":

    st.markdown(
        '<p class="title">📊 Analytics Dashboard</p>',
        unsafe_allow_html=True
    )

    # DATA RANDOM
    data = pd.DataFrame({
        "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"],
        "Penjualan": np.random.randint(10, 100, 6)
    })

    st.subheader("Grafik Penjualan")

    st.line_chart(
        data.set_index("Bulan")
    )

    st.subheader("Data Penjualan")

    st.dataframe(data, use_container_width=True)

# ==================================
# ABOUT
# ==================================
elif menu == "📖 Tentang":

    st.markdown(
        '<p class="title">📖 Tentang</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>🚀 Aplikasi Streamlit</h3>
        <p>
        Dashboard ini dibuat menggunakan Streamlit dengan desain modern,
        dark mode, dan tampilan profesional.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Versi aplikasi: 1.0")
