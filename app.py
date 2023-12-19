import streamlit as st
#from prediction import *
from clustering import *
from visualization import *


# def showRawData():
#     df = loadData()
#     # st.subheader('Raw Data')
#     # st.dataframe(df)

def main():
    st.title('FSVA Web App')
    st.sidebar.subheader('Menu')
    menu_options = ['Overview Project', 'Prediction', 'Clustering', 'Visualization']
    selected_menu = st.sidebar.selectbox('Select Option', menu_options)

    if selected_menu == 'Clustering':
        performClustering()
    elif selected_menu == 'Visualization':
        showVisualization()

if __name__ == '__main__':
    main()
    st.set_option('deprecation.showPyplotGlobalUse', False)