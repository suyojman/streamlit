import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from config import config
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)

class DataVisualization:
    """
    This class handles all the methods
    """

    def __init__(self):
        self.summary_file_path = config.file_paths['summary_file_path']
        self.timeline_file_path = config.file_paths['timeline_file_path']

    def show_data(self):
        """

        :return:
        """
        uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])
        iris = datasets.load_iris()
        if uploaded_file is not None:
            st.write("Sucessfully Uploaded CSV")
        if st.sidebar.button("Explore"):
            if uploaded_file == None:
                st.write("Please insert CSV ")
            else:
                data = pd.read_csv(uploaded_file)
                st.table(data)
        if st.sidebar.button("Show Iris Data"):
            df = pd.DataFrame(iris.data, columns=iris.feature_names)
            df['target']=iris.target
            st.table(df)
            
            
        
        

         
        page = st.sidebar.selectbox("Choose a PLOT", ["","Scatter Plot","Scatter Plot from matplotlib","Joint Plot","Box Plot"])
        if page == 'Total Cases View':
            detail_data_df = pd.read_csv(self.summary_file_path)
            st.text('TESTED POSITIVE:' + str(detail_data_df['Tested Positive'][0]) + '\n'
                    'TESTED NEGATIVE:' + str(detail_data_df['Tested Negative'][0]) + '\n'
                    'TESTED TOTAL:' + str(detail_data_df['Tested Total'][0]) + '\n'
                    'IN ISOLATION:' + str(detail_data_df['In Isolation'][0]) + '\n'
                    'QUARANTINED:' + str(detail_data_df['Quarantined'][0]) + '\n'
                    'TESTED RDT:' + str(detail_data_df['Tested RDT'][0]) + '\n'
                    'RECOVERED:' + str(detail_data_df['Recovered'][0]) + '\n'
                    'DEATH:' + str(detail_data_df['Death'][0]))
            st.write('\n BAR GRAPH REPRESENTATION')
            bar_df = pd.DataFrame({'Cases': ['TESTED POSITIVE', 'TESTED NEGATIVE', 'TESTED TOTAL', 'IN ISOLATION',
                                             'QUARANTINED', 'TESTED RDT', 'RECOVERED', ' DEATH'],
                                   'Count': [detail_data_df['Tested Positive'][0],
                                             detail_data_df['Tested Negative'][0],
                                             detail_data_df['Tested Total'][0],
                                             detail_data_df['In Isolation'][0],
                                             detail_data_df['Quarantined'][0],
                                             detail_data_df['Tested RDT'][0],
                                             detail_data_df['Recovered'][0],
                                             detail_data_df['Death'][0]]})

            # Using ALTAIR chart to build the bar chart
            st.write(alt.Chart(bar_df).mark_bar(size=18).encode(
                x='Cases',
                y='Count',
                color='Cases'
            ).properties(
                width=600,
                height=500
            ).interactive())

        elif page == 'Timeline View':
            st.write('TIMELINE REPRESENTATION OF CASES TILL NOW \n')
            timeline_df = pd.read_csv(self.timeline_file_path)
            line_df = pd.DataFrame({'date': timeline_df['Date'],
                                    'Total Cases': timeline_df['Total Cases'],
                                    'New Cases': timeline_df['New Cases'],
                                    'Total recoveries': timeline_df['Total recoveries'],
                                    'New Recoveries': timeline_df['New Recoveries'],
                                    'Total Death': timeline_df['Total Death'],
                                    'New Death': timeline_df['New Death']})

            line_df = line_df.rename(columns={'date': 'index'}).set_index('index')
            st.line_chart(line_df)
        elif page == 'Table':
            df1 = pd.DataFrame(
            np.random.randn(50, 20),
            columns=('col %d' % i for i in range(20)))
            my_table = st.table(df1)
        elif page == 'Scatter Plot':
            df = pd.DataFrame(iris.data, columns=iris.feature_names)
            select_value = st.sidebar.selectbox("Choose a value", ["","Sepal","Petal"])
            if select_value == 'Sepal':
                sepal_width = st.sidebar.slider('Sepal Width',df['sepal width (cm)'].min(),df['sepal width (cm)'].max(),(df['sepal width (cm)'].min(),df['sepal width (cm)'].min()+1.00))
                sepal_length = st.sidebar.slider('Sepal Length',df['sepal length (cm)'].min(),df['sepal length (cm)'].max(),(df['sepal length (cm)'].min(),df['sepal length (cm)'].min()+1.00))
                dfs = df[(df['sepal width (cm)'] >=  sepal_width[0]) & (df['sepal width (cm)'] <= sepal_width[1]) & (df['sepal length (cm)'] >=  sepal_length[0]) & (df['sepal length (cm)'] <= sepal_length[1])]
                st.write(alt.Chart(dfs).mark_circle().encode(
                alt.X('sepal length (cm)'),
                alt.Y('sepal width (cm)'),
                ))
            elif select_value == 'Petal':
                petal_width = st.sidebar.slider('Petal Width',df['petal width (cm)'].min(),df['petal width (cm)'].max(),(df['petal width (cm)'].min(),df['petal width (cm)'].min()+1.00))
                petal_length = st.sidebar.slider('Petal Length',df['petal length (cm)'].min(),df['petal length (cm)'].max(),(df['petal length (cm)'].min(),df['petal length (cm)'].min()+1.00))
                dfa = df[(df['petal width (cm)'] >=  petal_width[0]) & (df['petal width (cm)'] <= petal_width[1]) & (df['petal length (cm)'] >=  petal_length[0]) & (df['petal length (cm)'] <= petal_length[1])]
                st.write(alt.Chart(dfa).mark_circle().encode(
                alt.X('petal length (cm)'),
                alt.Y('petal width (cm)'),
                ))
        elif page == 'Scatter Plot from matplotlib':
            df = pd.DataFrame(iris.data, columns=iris.feature_names)
            df.plot(kind="scatter", x="sepal length (cm)", y="sepal width (cm)")
            st.pyplot()
            a = st.button("Download")
            if a:
                st.write("Successfully downloaded!!!")
                df.plot(kind="scatter", x="sepal length (cm)", y="sepal width (cm)")
                plt.savefig('figure_1.png')
        elif page == 'Box Plot':
            df = pd.DataFrame(iris.data, columns=iris.feature_names)
            df['target']=iris.target  
            df['species'] = df['target'].map({0:iris.target_names[0],1:iris.target_names[1],2:iris.target_names[2]})
            sepal_length = st.sidebar.slider('Sepal Length',df['sepal length (cm)'].min(),df['sepal length (cm)'].max(),(df['sepal length (cm)'].min(),df['sepal length (cm)'].min()+1.00))
            dfs = df[(df['sepal length (cm)'] >=  sepal_length[0]) & (df['sepal length (cm)'] <= sepal_length[1])]
            sns.boxplot(x="species", y="sepal length (cm)", data=dfs)
            st.pyplot()
if __name__ == '__main__':
    dvs = DataVisualization()
    dvs.show_data()
