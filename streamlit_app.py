import streamlit as st

# ======================
# CONFIG PAGE
# ======================
st.set_page_config(
    page_title="Website Saya",
    page_icon="🚀",
    layout="wide"
)

# ======================
# CUSTOM CSS
# ======================
st.markdown("""
<style>
/* Background */
.stApp {
    background-color: #f5f7fa;
}

/* Title */
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #1f2937;
}

/* Card */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

section[data-testid="stSidebar"] .css-1d391kg {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ======================
# SIDEBAR MENU
# ======================
st.sidebar.title("📌 Menu")

menu = st.sidebar.radio(
    "Navigasi",
    ["🏠 Home", "📖 Tentang"]
)

# ======================
# HOME PAGE
# ======================
if menu == "🏠 Home":

    st.markdown(
        '<p class="main-title">Dashboard Home</p>',
        unsafe_allow_html=True
    )

    st.write("Selamat datang di aplikasi modern Streamlit 🚀")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>👥 Users</h3>
            <h1>1,250</h1>
            <p>Total pengguna</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>💰 Pendapatan</h3>
            <h1>Rp 12 Jt</h1>
            <p>Bulan ini</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>📦 Produk</h3>
            <h1>320</h1>
            <p>Total produk</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>📊 Statistik</h3>
        <p>Contoh dashboard modern menggunakan Streamlit.</p>
    </div>
    """, unsafe_allow_html=True)

# ======================
# ABOUT PAGE
# ======================
elif menu == "📖 Tentang":

    st.markdown(
        '<p class="main-title">Tentang Aplikasi</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>🚀 Deskripsi</h3>
        <p>
        Aplikasi ini dibuat menggunakan Streamlit dengan tampilan modern.
        Cocok untuk dashboard, AI app, data science, dan web internal.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",
        width=250
    )

    st.success("Aplikasi berhasil dibuat 🎉")
