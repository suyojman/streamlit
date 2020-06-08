import streamlit as st
import pandas as pd


def show_data():
    """

    :return:
    """
    page = st.sidebar.selectbox("Choose a page", ["Total Cases View", "Timeline View"])
    if page == 'Total Cases View':
        detail_data_df = pd.read_csv('/home/yipl/Workspace/learn/streamlitapp/nepal_detail.csv')
        dict_data = detail_data_df.to_dict()
        st.text('TESTED POSITIVE:' + str(detail_data_df['Tested Positive'][0]) + '\n'
                'TESTED NEGATIVE:' + str(dict_data['Tested Negative'][0]) + '\n'
                'TESTED TOTAL:' + str(dict_data['Tested Total'][0]) + '\n'
                'IN ISOLATION:' + str( dict_data['In Isolation'][0]) + '\n'
                'QUARANTINED:' + str(dict_data['Quarantined'][0]) + '\n'
                'TESTED RDT:' + str(dict_data['Tested RDT'][0]) + '\n'
                'RECOVERED:' + str(dict_data['Recovered'][0]) + '\n'
                'DEATH:' + str(dict_data['Death'][0]))

    elif page == 'Timeline View':
        timeline_df = pd.read_csv('/home/yipl/Workspace/learn/streamlitapp/nepal_timeline.csv')
        line_df = pd.DataFrame({'date': timeline_df['Date'],
                                'Total Cases': timeline_df['Total Cases'],
                                'New Cases': timeline_df['New Cases'],
                                'Total recoveries': timeline_df['Total recoveries'],
                                'New Recoveries': timeline_df['New Recoveries'],
                                'Total Death': timeline_df['Total Death'],
                                'New Death': timeline_df['New Death']})

        line_df = line_df.rename(columns={'date': 'index'}).set_index('index')
        st.line_chart(line_df)


if __name__ == '__main__':
    print('browse to see the output.')
    show_data()
