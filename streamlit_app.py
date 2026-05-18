import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="Sistem Penilaian Siswa",
    page_icon="🎓",
    layout="wide"
)

FILE_DATA = "data_siswa.csv"
FILE_USER = "users.csv"

# =====================================
# LOAD DATA
# =====================================
def load_data():
    if os.path.exists(FILE_DATA):
        return pd.read_csv(FILE_DATA)
    else:
        df = pd.DataFrame(columns=[
            "NIS",
            "Nama",
            "Kelas",
            "Mapel",
            "Nilai"
        ])
        return df

# =====================================
# SAVE DATA
# =====================================
def save_data(df):
    df.to_csv(FILE_DATA, index=False)

# =====================================
# LOGIN
# =====================================
def check_login(username, password):

    users = pd.read_csv(FILE_USER)

    user = users[
        (users["username"] == username) &
        (users["password"] == password)
    ]

    return len(user) > 0

# =====================================
# SESSION LOGIN
# =====================================
if "login" not in st.session_state:
    st.session_state.login = False

# =====================================
# LOGIN PAGE
# =====================================
if not st.session_state.login:

    st.title("🔐 LOGIN GURU")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("LOGIN"):

        if check_login(username, password):
            st.session_state.login = True
            st.success("Login berhasil")
            st.rerun()

        else:
            st.error("Username/password salah")

    st.stop()

# =====================================
# LOAD DATA
# =====================================
df = load_data()

# =====================================
# CSS MODERN
# =====================================
st.markdown("""
<style>

.stApp {
    background-color: #f4f6f9;
}

.title {
    font-size: 38px;
    font-weight: bold;
    color: #1d4ed8;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================
st.markdown(
    '<p class="title">🎓 Sistem Penilaian Siswa SMA</p>',
    unsafe_allow_html=True
)

# =====================================
# SIDEBAR
# =====================================
menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Dashboard",
        "📋 Data Siswa",
        "➕ Tambah Data",
        "✏ Edit Data",
        "❌ Hapus Data",
        "📊 Ranking",
        "📈 Grafik Nilai",
        "📤 Export Excel",
        "📥 Upload Excel",
        "🚪 Logout"
    ]
)

# =====================================
# DASHBOARD
# =====================================
if menu == "🏠 Dashboard":

    st.subheader("Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
        <h3>Total Siswa</h3>
        <h1>{len(df)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        rata = 0 if len(df)==0 else round(df["Nilai"].mean(),2)

        st.markdown(f"""
        <div class="card">
        <h3>Rata-rata Nilai</h3>
        <h1>{rata}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        tertinggi = 0 if len(df)==0 else df["Nilai"].max()

        st.markdown(f"""
        <div class="card">
        <h3>Nilai Tertinggi</h3>
        <h1>{tertinggi}</h1>
        </div>
        """, unsafe_allow_html=True)

# =====================================
# DATA SISWA
# =====================================
elif menu == "📋 Data Siswa":

    st.subheader("Data Penilaian Siswa")

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================
# TAMBAH DATA
# =====================================
elif menu == "➕ Tambah Data":

    st.subheader("Tambah Data")

    with st.form("form_tambah"):

        nis = st.text_input("NIS")
        nama = st.text_input("Nama")
        kelas = st.selectbox(
            "Kelas",
            ["X","XI","XII"]
        )
        mapel = st.text_input("Mapel")

        nilai = st.number_input(
            "Nilai",
            0,
            100
        )

        submit = st.form_submit_button("Simpan")

        if submit:

            data_baru = pd.DataFrame({
                "NIS":[nis],
                "Nama":[nama],
                "Kelas":[kelas],
                "Mapel":[mapel],
                "Nilai":[nilai]
            })

            df = pd.concat(
                [df,data_baru],
                ignore_index=True
            )

            save_data(df)

            st.success("Data berhasil ditambahkan")

# =====================================
# EDIT
# =====================================
elif menu == "✏ Edit Data":

    st.subheader("Edit Data")

    if len(df) > 0:

        pilih = st.selectbox(
            "Pilih NIS",
            df["NIS"]
        )

        index = df[
            df["NIS"] == pilih
        ].index[0]

        with st.form("edit_form"):

            nama = st.text_input(
                "Nama",
                df.loc[index,"Nama"]
            )

            kelas = st.selectbox(
                "Kelas",
                ["X","XI","XII"]
            )

            mapel = st.text_input(
                "Mapel",
                df.loc[index,"Mapel"]
            )

            nilai = st.number_input(
                "Nilai",
                0,
                100,
                int(df.loc[index,"Nilai"])
            )

            update = st.form_submit_button(
                "Update"
            )

            if update:

                df.loc[index,"Nama"] = nama
                df.loc[index,"Kelas"] = kelas
                df.loc[index,"Mapel"] = mapel
                df.loc[index,"Nilai"] = nilai

                save_data(df)

                st.success("Data berhasil diupdate")

# =====================================
# HAPUS
# =====================================
elif menu == "❌ Hapus Data":

    st.subheader("Hapus Data")

    pilih = st.selectbox(
        "Pilih NIS",
        df["NIS"]
    )

    if st.button("Hapus"):

        df = df[
            df["NIS"] != pilih
        ]

        save_data(df)

        st.success("Data berhasil dihapus")

# =====================================
# RANKING
# =====================================
elif menu == "📊 Ranking":

    st.subheader("Ranking Siswa")

    ranking = df.sort_values(
        by="Nilai",
        ascending=False
    )

    ranking["Ranking"] = range(
        1,
        len(ranking)+1
    )

    st.dataframe(
        ranking,
        use_container_width=True
    )

# =====================================
# GRAFIK
# =====================================
elif menu == "📈 Grafik Nilai":

    st.subheader("Grafik Nilai Siswa")

    fig = px.bar(
        df,
        x="Nama",
        y="Nilai",
        color="Kelas"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================
# EXPORT EXCEL
# =====================================
elif menu == "📤 Export Excel":

    st.subheader("Export Excel")

    file_excel = "nilai_siswa.xlsx"

    df.to_excel(
        file_excel,
        index=False
    )

    with open(file_excel, "rb") as file:

        st.download_button(
            label="⬇ Download Excel",
            data=file,
            file_name=file_excel,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# =====================================
# UPLOAD EXCEL
# =====================================
elif menu == "📥 Upload Excel":

    st.subheader("Upload Excel")

    uploaded = st.file_uploader(
        "Upload File Excel",
        type=["xlsx"]
    )

    if uploaded:

        data_upload = pd.read_excel(
            uploaded
        )

        st.dataframe(data_upload)

        if st.button("Simpan Data Upload"):

            save_data(data_upload)

            st.success("Data berhasil diupload")

# =====================================
# LOGOUT
# =====================================
elif menu == "🚪 Logout":

    st.session_state.login = False
    st.rerun()
