import pandas as pd
import streamlit as st

def main():
    st.write("""
        Thiru Praturi's Stock Market Web Application..
        This is testing waters (a warmup exercise) using Python based Web Apps where you can select a stock and look at its price chart
        A **Lot MORE** coming very soon on this site (including Predictive Analysis and Portfolio Optimization tools)
        """)
    st.sidebar.header("User Input")
    df = load_data()
    st.dataframe(df)

def load_data():
    return pd.read_csv("https://stksdata1.s3.us-east-2.amazonaws.com/stksDat.csv")
    #return pd.read_csv("https://docs.google.com/spreadsheets/d/1oxIZj2DwHaIhAPt4tMnqeK5T8o0DcLXYGglHdae-ioc/edit?usp=sharing")

if __name__ == '__main__':
    main()