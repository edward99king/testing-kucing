import streamlit as st
from PIL import Image

def main():
    st.set_page_config(layout="wide")  # Set wide layout for better organization

    st.title("Biodata-ku")

    image = Image.open("../../kucing.jpeg")
    st.image(image, width=300)

    with st.container():
        st.subheader("Biodata")
        st.write("Nama Lengkap: Kucing Kuning")
        st.write("Jenis Kelamin: Male")
        st.write("Tanggal Lahir: 29 Februari 2000")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Pendidikan")
        st.write("S1 - Teknik Informatika")
        st.write("SMAN 3 Bandung")

    with col2:
        st.subheader("Pengalaman Kerja")
        st.write("2022 - 2024: PT. Sejahtera")
        st.write("2020 - 2022: PT. Hari-hari")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Pengalaman Organisasi")
        st.write("S1 - Teknik Informatika")
        st.write("SMAN 3 Bandung")

    with col4:
        st.subheader("Pengalaman Pelatihan")
        st.write("2024: Data Science")

    with st.container():
        st.subheader("Skill yang berhubungan")
        st.write("Bahasa Pemrograman: Python")
        st.write("Framework: Sci-Kit Learn")

if __name__ == "__main__":
    main()