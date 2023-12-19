import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def loadData():
    df = pd.read_csv('FSVA 2022 Cleaned.csv')
    return df

def performClustering():
    df = loadData()

    def getSelectedAttributes():
        selected_attributes = []
        
        # Membagi layar menjadi dua kolom
        col1, col2 = st.columns(2)

        # Kolom pertama
        with col1:
            if st.checkbox('NCPR'):
                selected_attributes.append('NCPR')
            if st.checkbox('Kemiskinan (%)'):
                selected_attributes.append('Kemiskinan (%)')
            if st.checkbox('Pengeluaran Pangan (%)'):
                selected_attributes.append('Pengeluaran Pangan (%)')
            if st.checkbox('Tanpa Listrik (%)'):
                selected_attributes.append('Tanpa Listrik (%)')
            if st.checkbox('Tanpa Air Bersih (%)'):
                selected_attributes.append('Tanpa Air Bersih (%)')

        # Kolom kedua
        with col2:
            if st.checkbox('Lama Sekolah Perempuan (tahun)'):
                selected_attributes.append('Lama Sekolah Perempuan (tahun)')
            if st.checkbox('Rasio Tenaga Kesehatan'):
                selected_attributes.append('Rasio Tenaga Kesehatan')
            if st.checkbox('Angka Harapan Hidup (tahun)'):
                selected_attributes.append('Angka Harapan Hidup (tahun)')
            if st.checkbox('Stunting (%)'):
                selected_attributes.append('Stunting (%)')

        if len(selected_attributes) != 2:
            st.warning('Select 2 Attributes!')
            st.stop()

        return selected_attributes
    
    num_clusters = st.slider('Number of Clusters', min_value=2, max_value=10, value=3)

    def performClustering(selected_attributes, num_clusters):
        X = df[selected_attributes]
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(X)
        labels = kmeans.labels_
        df['Cluster'] = labels

        fig, ax = plt.subplots()
        for cluster in range(num_clusters):
            cluster_data = df[df['Cluster'] == cluster]
            ax.scatter(cluster_data[selected_attributes[0]], cluster_data[selected_attributes[1]], label=f'Cluster {cluster + 1}')
        ax.set_xlabel(selected_attributes[0])
        ax.set_ylabel(selected_attributes[1])
        ax.set_title('K-Means Clustering')
        ax.legend()
        st.pyplot(fig)

        st.subheader('Cluster Labels:')
        st.write(df[['Cluster'] + selected_attributes])

        # Perform prediction on user data based on cluster centroids
        user_data = pd.DataFrame(columns=selected_attributes)
        for attribute in selected_attributes:
            user_input = st.number_input(f'Input nilai {attribute}')
            user_data[attribute] = [user_input]

        user_cluster = kmeans.predict(user_data)
        st.subheader('Your Report : ')
        output = f'You belong to Cluster {user_cluster[0]}'
        st.write(output)

    selected_attributes = getSelectedAttributes()

    if len(selected_attributes) == 2:
        performClustering(selected_attributes, num_clusters)