import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def loadData():
    df = pd.read_csv('FSVA 2022 Cleaned.csv')
    return df

def showVisualization():
    df = loadData()

    # Checkbox untuk opsi visualisasi
    x_axis = st.sidebar.selectbox('Select X-Axis', ['-', *df.columns])
    y_axis = st.sidebar.selectbox('Select Y-Axis', ['-', *df.columns])
    color_option = st.sidebar.selectbox('Select Color', ['-', *df.columns])
    size_option = st.sidebar.selectbox('Select Size', ['-', *df.columns])
    visualization_option = st.sidebar.selectbox('Select Visualization', ['Scatter Plot', 'Histogram'])

    # Scatter plot
    if visualization_option == 'Scatter Plot':
        st.subheader('Scatter Plot')
        if x_axis != '-' and y_axis != '-':
            if x_axis != y_axis:
                scatterplot_data = df[[x_axis, y_axis]]
                if color_option != '-':
                    scatterplot_data['Color'] = df[color_option]
                if size_option != '-':
                    scatterplot_data['Size'] = df[size_option]
                    scatterplot = sns.scatterplot(data=scatterplot_data, x=x_axis, y=y_axis, hue=None if color_option == '-' else 'Color', size='Size', legend=False)
                else:
                    scatterplot = sns.scatterplot(data=scatterplot_data, x=x_axis, y=y_axis, hue=None if color_option == '-' else 'Color', size=None)
                scatterplot.set_xlabel(x_axis)
                scatterplot.set_ylabel(y_axis)
                scatterplot.set_title('Scatter Plot')
                st.pyplot()
            else:
                st.warning('X-Axis and Y-Axis must be different.')
        else:
            st.info('Please select both X-Axis and Y-Axis.')

    # Histogram
    elif visualization_option == 'Histogram':
        st.subheader('Histogram')
        if x_axis != '-':
            if y_axis == '-':
                if color_option != '-':
                    if size_option == '-':
                        colors = df[color_option]
                        sns.histplot(data=df, x=x_axis, hue=color_option, multiple="stack", kde=False, palette="muted")
                        plt.xlabel(x_axis)
                        plt.ylabel('Count')
                        plt.title('Histogram')
                        st.pyplot()
                    else:
                        st.warning('Cannot choose size for Histogram.')
                else:
                    if size_option == '-':
                        plt.hist(df[x_axis], bins='auto', color='skyblue')
                        plt.xlabel(x_axis)
                        plt.ylabel('Count')
                        plt.title('Histogram')
                        st.pyplot()
                    else:
                        st.warning('Cannot choose size for Histogram.')
            else:
                st.warning('Only select X-Axis for Histogram.')
        else:
            st.info('Please select X-Axis.')