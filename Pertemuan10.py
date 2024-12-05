import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf

st.title("pertemuan 10: Interaksi streamlit dan yahoo finance")
st.write("# pendahuluan")

kamus_ticker = {
    'GOOGL': 'Google',
    'AAPL': 'Apple',
    'SBUX': 'Starbucks',
    'MCD': 'McDonalds',
    'BBNI': 'Bank Negara Indonesia (Persero) Tbk PT',
    'BMRI': 'Bank Mandiri (Persero) Tbk PT',
    'BBRI': 'Bank Rakyat Indonesia (Persero) Tbk PT'
}
tickerSymbol = st.selectbox(
    'silakan pilih kode perusahaan:',
    kamus_ticker.keys()
)


st.write(f'Harga saham {tickerSymbol}.')

tickerdata = yf.Ticker(tickerSymbol)
pilihan_periode = st.selectbox(
    'pilhan periode:',
    ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y']
)

tickerdata = yf.Ticker(tickerSymbol)
tickerDF = tickerdata.history(
    period='1d',
    start='2024-10-01',
    end='2024-11-06'
)
flag_tampil = st.checkbox('Tampilkan tabel')
if flag_tampil:
    st.write(tickerDF.head(10))

flag_grafik = st.checkbox('Tampil grafik')
pilihan_atribut = st.multiselect(
    'silahkan pilih atribut yang akan ditampilkan:',
    ['Low', 'High', 'Open', 'Close', 'Volume']
)

grafik = px.line(
    tickerDF,
    title=f'Harga saham {tickerSymbol}',
    y = pilihan_atribut
)
st.plotly_chart(grafik)

# cara ngambil data dari BPS
# df_
