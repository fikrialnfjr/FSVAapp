import streamlit as st

def show_overview():
    st.subheader("About")

    st.write("""
    Proyek ini menggambarkan tingkat ketahanan dan kerentanan pangan suatu wilayah melalui pendekatan prediktif
    menggunakan Food Security and Vulnerability Atlas (FSVA).
    FSVA merupakan alat analisis yang menyajikan informasi terkait 
    ketahanan dan kerentanan pangan berdasarkan indikator-indikator kunci.

    Pemilihan topik FSVA sebagai fokus proyek ini didasarkan pada pentingnya pemahaman mendalam terhadap ketahanan pangan, 
    terutama dalam konteks perubahan iklim dan tantangan global. FSVA memberikan pemahaman yang holistik terhadap 
    faktor-faktor yang memengaruhi ketahanan pangan dan berpotensi memberikan wawasan berharga untuk kebijakan dan strategi mitigasi.
    """)

    st.subheader("Goals Project")

    st.write("""
    Tujuan proyek ini adalah mengembangkan model prediktif untuk mengukur tingkat ketahanan dan kerentanan pangan 
    suatu wilayah berdasarkan indikator-indikator tertentu. Model ini diharapkan dapat memberikan pemahaman yang lebih 
    akurat dan komprehensif terhadap situasi pangan di wilayah tersebut. Hasil prediksi akan mengelompokkan wilayah 
    ke dalam salah satu kategori berikut:
    - Sangat Rentan
    - Rentan
    - Agak Rentan
    - Agak Tahan
    - Tahan
    - Sangat Tahan

    Kategori ini dapat meningkatkan pemahaman terhadap situasi pangan dan memberikan kontribusi dalam mengambil 
    keputusan yang berkelanjutan dan berdampak positif terhadap ketahanan pangan di wilayah yang diteliti.
    """)

    st.subheader("Workflow App")
    local_image_path_1 = "/Users/fikrialinfijar/Developer/FSVA/1.png"
    st.image(local_image_path_1, caption="Workflow FSVA", use_column_width=True)

    st.subheader("Workflow Modelling")
    local_image_path_2 = "/Users/fikrialinfijar/Developer/FSVA/2.png"
    st.image(local_image_path_2, caption="Workflow Modelling", use_column_width=True)
