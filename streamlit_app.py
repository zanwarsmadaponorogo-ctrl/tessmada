import streamlit as st
import pandas as pd
import os

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="Aplikasi Penilaian Siswa",
    page_icon="🎓",
    layout="wide"
)

FILE_DATA = "data_siswa.csv"

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
# LOAD AWAL
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
    color: #1e3a8a;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================
st.markdown(
    '<p class="title">🎓 Aplikasi Penilaian Siswa SMA</p>',
    unsafe_allow_html=True
)

# =====================================
# MENU
# =====================================
menu = st.sidebar.radio(
    "Menu",
    [
        "📋 Data Siswa",
        "➕ Tambah Data",
        "✏ Edit Data",
        "❌ Hapus Data",
        "📤 Export Excel"
    ]
)

# =====================================
# TAMPIL DATA
# =====================================
if menu == "📋 Data Siswa":

    st.subheader("Data Penilaian Siswa")

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================
# TAMBAH DATA
# =====================================
elif menu == "➕ Tambah Data":

    st.subheader("Tambah Data Siswa")

    with st.form("form_tambah"):

        nis = st.text_input("NIS")
        nama = st.text_input("Nama Siswa")
        kelas = st.selectbox(
            "Kelas",
            ["X", "XI", "XII"]
        )

        mapel = st.text_input("Mata Pelajaran")

        nilai = st.number_input(
            "Nilai",
            0,
            100
        )

        submit = st.form_submit_button("Simpan")

        if submit:

            data_baru = pd.DataFrame({
                "NIS": [nis],
                "Nama": [nama],
                "Kelas": [kelas],
                "Mapel": [mapel],
                "Nilai": [nilai]
            })

            df = pd.concat(
                [df, data_baru],
                ignore_index=True
            )

            save_data(df)

            st.success("Data berhasil ditambahkan")

# =====================================
# EDIT DATA
# =====================================
elif menu == "✏ Edit Data":

    st.subheader("Edit Data")

    if len(df) > 0:

        pilih_nis = st.selectbox(
            "Pilih NIS",
            df["NIS"]
        )

        index = df[df["NIS"] == pilih_nis].index[0]

        with st.form("form_edit"):

            nama = st.text_input(
                "Nama",
                df.loc[index, "Nama"]
            )

            kelas = st.selectbox(
                "Kelas",
                ["X", "XI", "XII"],
                index=["X","XI","XII"].index(
                    df.loc[index, "Kelas"]
                )
            )

            mapel = st.text_input(
                "Mapel",
                df.loc[index, "Mapel"]
            )

            nilai = st.number_input(
                "Nilai",
                0,
                100,
                int(df.loc[index, "Nilai"])
            )

            update = st.form_submit_button("Update")

            if update:

                df.loc[index, "Nama"] = nama
                df.loc[index, "Kelas"] = kelas
                df.loc[index, "Mapel"] = mapel
                df.loc[index, "Nilai"] = nilai

                save_data(df)

                st.success("Data berhasil diupdate")

# =====================================
# HAPUS DATA
# =====================================
elif menu == "❌ Hapus Data":

    st.subheader("Hapus Data")

    if len(df) > 0:

        pilih_nis = st.selectbox(
            "Pilih NIS",
            df["NIS"]
        )

        if st.button("Hapus"):

            df = df[df["NIS"] != pilih_nis]

            save_data(df)

            st.success("Data berhasil dihapus")

# =====================================
# EXPORT EXCEL
# =====================================
elif menu == "📤 Export Excel":

    st.subheader("Export Data ke Excel")

    file_excel = "data_penilaian_siswa.xlsx"

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

    st.success("File Excel siap didownload")
