import streamlit as st

def show_overview():
    st.subheader("About")

    st.write("""
    FSVA merupakan peta tematik yang menggambarkan visualisasi geografis dari hasil analisa data indikator kerentanan terhadap kerawanan pangan. 
    FSVA disusun menggunakan sembilan indikator yang mewakili tiga aspek ketahanan pangan, yaitu ketersediaan, keterjangkauan dan pemanfaatan pangan.

    FSVA adalah sistem kewaspadaan yang memberikan rekomendasi kepada pembuat keputusan dalam 
    penyusunan kebijakan dan program intervensi baik di tingkat pusat dan daerah dengan melihat 
    indikator utama yang menjadi pemicu terjadinya kerentanan terhadap kerawanan pangan.  
    """)

    st.subheader("Why is it Importants?")

    st.write('''
    Ketersediaan pangan yang lebih kecil dibandingkan kebutuhannya dapat menciptakan ketidak-stabilan ekonomi. 
    Berbagai gejolak sosial dan politik dapat juga terjadi jika ketahanan pangan terganggu. 
    Kondisi pangan yang kritis ini bahkan dapat membahayakan stabilitas ekonomi dan stabilitas Nasional.
    ''')

    st.subheader("Problems")

    st.write('''
    Banyak daerah di Indonesia yang masih belum memiliki Indeks Ketahanan Pangan (IKP) atau Indeks Komposit 
    yang menjadi penentu pemerintah dalam membuat skala prioritas perhatian dalam upaya pemerintah menciptakan Indonesia Tahan Pangan.
    ''')

    st.subheader("Goals")

    st.write("""
    - Memberikan kemudahan kepada daerah-daerah yang tertinggal dalam penyediaan data

    - Menghilangkan kerumitan perhitungan

    - Waktu yang lebih cepat untuk memperoleh status ketahanan pangan

    - Proses mendapatkan saran yang tepat dan cepat menjadi lebih efisien

    Dengan aplikasi ini kami berharap mendukung pemerintah dalam menciptakan masyarakat 
    yang tahan pangan dimana hal tersebut juga memberi dampak positif bagi kemajuan dan keberlanjutan masyarakat.

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
    st.write("**Atribut feature pada dataset :**")
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

    st.write("**Atribut target pada dataset :**")
    st.write('''
    Komposit : Indikator yang menunjukkan tingkat ketahanan suatu wilayah terhadap masalah pangan.

    - Komposit 1 mengartikan bahwa "Sangat Rentan"

    - Komposit 2 mengartikan bahwa "Rentan"

    - Komposit 3 mengartikan bahwa "Agak Rentan"

    - Komposit 4 mengartikan bahwa "Agak Tahan"

    - Komposit 5 mengartikan bahwa "Tahan"

    - Komposit 6 mengartikan bahwa "Sangat Tahan"
    ''')

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