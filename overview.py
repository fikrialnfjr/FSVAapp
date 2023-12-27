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

    st.subheader("Goals")

    st.write("""
    Tujuan proyek ini adalah mengembangkan model prediktif untuk mengukur tingkat ketahanan dan kerentanan pangan 
    suatu wilayah berdasarkan indikator-indikator tertentu. Model ini diharapkan dapat memberikan pemahaman yang lebih 
    akurat dan komprehensif terhadap situasi pangan di wilayah tersebut. Hasil prediksi akan mengelompokkan wilayah 
    ke dalam salah satu kategori berikut:

    - Komposit 1 mengartikan bahwa "Sangat Rentan"

    - Komposit 2 mengartikan bahwa "Rentan"

    - Komposit 3 mengartikan bahwa "Agak Rentan"

    - Komposit 4 mengartikan bahwa "Agak Tahan"

    - Komposit 5 mengartikan bahwa "Tahan"

    - Komposit 6 mengartikan bahwa "Sangat Tahan"

    Kategori ini dapat meningkatkan pemahaman terhadap situasi pangan dan memberikan kontribusi dalam mengambil 
    keputusan yang berkelanjutan dan berdampak positif terhadap ketahanan pangan di wilayah yang diteliti.
    """)

    st.subheader("Workflow App")
    local_image_1 = "1.png"
    st.image(local_image_1, caption="Workflow FSVA", use_column_width=True)

    st.subheader("Workflow Modelling")
    local_image_2 = "2.png"
    st.image(local_image_2, caption="Workflow Modelling", use_column_width=True)

    st.write("#### **Pengumpulan Dataset**")
    st.write("""
    Dataset yang digunakan berasal dari web Badan Pangan Nasional (BPN) : 
    https://fsva.badanpangan.go.id
    """)
    st.write("Berikut ini adalah atribut yang terdapat pada dataset : ")
    st.write("""
    - NCPR\t\t: Rasio Konsumsi Normatif terhadap Ketersediaan Bersih per Kapita

    - Kemiskinan (%)\t: Persentase Penduduk Miskin

    - Pengeluaran Pangan (%)\t: Persentase Rumah Tangga dengan Pengeluaran Pangan > 65% Total Konsumsi

    - Tanpa Listrik (%)\t: Persentase Rumah Tangga tanpa Listrik

    - Tanpa Air Bersih (%)\t: Persentase Rumah Tangga tanpa Air Bersih

    - Lama Sekolah Perempuan (tahun)\t: Rata-rata Lama Sekolah (tahun) Perempuan berusia 15 tahun keatas

    - Rasio Tenaga Kesehatan\t: Rasio Penduduk per Tenaga Kesehatan terhadap Tingkat Kepadatan Penduduk

    - Angka Harapan Hidup (tahun)\t: Angka Harapan Hidup (tahun)

    - Stunting (%)\t\t: Persentase Balita dengan Tinggi Badan dibawah Standar (Stunting)
    """)

    st.write("#### **Preprocessing**")
    st.write("""
    Preprocessing yang dilakukan hanya menghapus kolom yang tidak digunakan pada saat modelling.
    """)

    st.write("#### **Featuring Engineering**")
    st.write("""
    **Featuring Engineering menggunakan StandardScaler**

    StandardScaler adalah metode normalisasi yang digunakan untuk mentransformasi data sehingga setiap fitur memiliki rata-rata 0 
    dan deviasi standar 1. Hal ini membantu menghilangkan perbedaan skala antar fitur, yang dapat mempengaruhi performa 
    algoritma machine learning, terutama yang sensitif terhadap skala seperti regresi logistik dan support vector machines (SVM).
    """)

    st.write("#### **Modelling**")
    st.write("##### Supervised Learning")
    st.write("""
    - **Random Forest**

    Random Forest adalah algoritma ensemble yang membangun sejumlah pohon keputusan selama pelatihan dan menggabungkan 
    hasilnya. Ini termasuk konsep pengambilan sampel acak dari setiap data pelatihan dan konstruksi pohon keputusan 
    independen satu sama lain. Random Forest memiliki kinerja yang baik untuk tugas klasifikasi dan regresi, serta 
    toleran terhadap overfitting.

    Model Random Forest terbaik yang kami buat adalah : 
    
    RandomForestClassifier(n_estimators=100, random_state=42)

    dimana akurasinya sebagai berikut : 

        \t- Pada data train\t: 1.0

        - Pada data test\t: 0.8349514563106796

    - **SVM**

    SVM adalah algoritma pembelajaran mesin yang digunakan untuk tugas klasifikasi dan regresi. SVM mencari pemisah optimal 
    (hyperplane) antara dua kelas dengan memaksimalkan margin antara kedua kelas. SVM dapat bekerja baik dengan data yang 
    memiliki dimensi tinggi dan sangat baik untuk tugas klasifikasi, terutama dalam kasus ketika ada kebutuhan untuk 
    menangani data yang tidak linier.

    Model Random Forest terbaik yang kami buat adalah : 
    
    SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)

    dimana akurasinya sebagai berikut : 

        \t- Pada data train\t: 0.8880778588807786

        - Pada data test\t: 0.8349514563106796
    """)


    st.write("##### Unupervised Learning")
    st.write("""
    **K-Means Clustering**

    K-Means Clustering adalah algoritma pembelajaran mesin yang digunakan untuk mengelompokkan data menjadi beberapa kelompok 
    (cluster) berdasarkan kesamaan fitur. Algoritma ini mencoba untuk membagi data menjadi k kelompok dengan cara meminimalkan 
    varians di dalam setiap kelompok. Setiap kelompok ditentukan oleh pusat massa atau centroid, dan setiap data diatribusikan 
    ke kelompok dengan pusat massa terdekat.
    """)