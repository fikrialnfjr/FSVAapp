import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def loadData():
    df = pd.read_csv('FSVA 2022 Cleaned.csv')
    return df

def performPrediction():
    st.subheader("Dataset")
    df = loadData()
    st.write(df)

    x = df.drop(['Komposit'], axis=1)
    y = df['Komposit']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Normalisasi fitur menggunakan StandardScaler
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    def user_report():
        col1, col2 = st.columns(2)

        with col1:
            NCPR = st.number_input('Input nilai NCPR')
            Kemiskinan = st.number_input('Input nilai Kemiskinan (%)')
            Pengeluaran_Pangan = st.number_input('Input nilai Pengeluaran Pangan (%)')
            Tanpa_Listrik = st.number_input('Input nilai Tanpa Listrik (%)')
            Tanpa_Air_Bersih = st.number_input('Input nilai Tanpa Air Bersih (%)')
        with col2:
            Lama_Sekolah_Perempuan = st.number_input('Input nilai Lama Sekolah Perempuan (tahun)')
            Rasio_Tenaga_Kesehatan = st.number_input('Input nilai Rasio Tenaga Kesehatan')
            Angka_Harapan_Hidup = st.number_input('Input nilai Angka Harapan Hidup (tahun)')
            Stunting = st.number_input('Input nilai Stunting (%)')

        user_data = {'NCPR': NCPR, 'Kemiskinan (%)': Kemiskinan, 'Pengeluaran Pangan (%)': Pengeluaran_Pangan,
                     'Tanpa Listrik (%)': Tanpa_Listrik, 'Tanpa Air Bersih (%)': Tanpa_Air_Bersih,
                     'Lama Sekolah Perempuan (tahun)': Lama_Sekolah_Perempuan,
                     'Rasio Tenaga Kesehatan': Rasio_Tenaga_Kesehatan,
                     'Angka Harapan Hidup (tahun)': Angka_Harapan_Hidup, 'Stunting (%)': Stunting}

        report_data = pd.DataFrame(user_data, index=[0])
        return report_data

    user_data = user_report()
    # Normalisasi inputan user
    user_data_scaled = scaler.transform(user_data)

    # Tambahkan dropdown untuk memilih algoritma
    algorithm = st.selectbox("Choose Algorithm", ["Random Forest", "SVM"])

    if algorithm == "Random Forest":
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        # Melatih model RandomForestClassifier
        model.fit(x_train, y_train)
    elif algorithm == "SVM":
        model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
        # Melatih model LogisticRegression
        model.fit(x_train, y_train)
        
    # Menghitung dan menampilkan akurasi
    accuracy = accuracy_score(y_test, model.predict(x_test)) * 100
    rounded_accuracy = round(accuracy, 2)
    st.subheader("Accuracy : ")
    st.write(f"Accuracy: {rounded_accuracy}%")

    if st.button('Predict'):
        prediction = model.predict(user_data_scaled)
        
        st.subheader('Your Report : ')
        output = ''
        if prediction[0] == 1:
            output = 'Sangat Rentan'
        elif prediction[0] == 2:
            output = 'Rentan'
        elif prediction[0] == 3:
            output = 'Agak Rentan'
        elif prediction[0] == 4:
            output = 'Agak Tahan'
        elif prediction[0] == 5:
            output = 'Tahan'
        elif prediction[0] == 6:
            output = 'Sangat Tahan'
        st.write(output)