#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.sav')


encoding_info = {
   'Ekran Boyutu': {'13,4 inç': 0, '14 inç': 1, '15,6 inç': 2, '16 inç': 3, '16,1 inç': 4, '17 inç': 5, '17,3 inç': 6, '18 inç': 7}, 
    'Ekran Kartı': {'AMD Radeon RX6500M': 0,'Intel Iris Graphics': 2, 'Nvidia GeForce GTX 1650': 3, 'Nvidia GeForce GTX1650 Ti': 4, 'Nvidia GeForce MX350': 5, 'Nvidia GeForce MX450': 6, 'Nvidia GeForce MX550': 7, 'Nvidia GeForce RTX 2050': 8, 'Nvidia GeForce RTX 3050': 9, 'Nvidia GeForce RTX 3050 Ti': 10, 'Nvidia GeForce RTX 3060 Ti': 11, 'Nvidia GeForce RTX 3070': 12, 'Nvidia GeForce RTX 3070Ti': 13, 'Nvidia GeForce RTX 3080': 14, 'Nvidia GeForce RTX 4050': 15, 'Nvidia GeForce RTX 4060': 16, 'Nvidia GeForce RTX 4070': 17, 'Nvidia GeForce RTX 4080': 18, 'Nvidia GeForce RTX 4090': 19, 'Nvidia GeForce RTX3060': 20},
    'Ekran Kartı Hafızası': {'12 GB': 0, '16 GB': 1, '2 GB': 2, '4 GB': 3, '6 GB': 4, '8 GB': 5},
    'Ekran Yenileme Hızı': {'120 Hz': 0, '144 Hz': 1, '165 Hz': 2, '240 Hz': 3, '360 Hz': 4, '480 Hz': 5, '60 Hz': 6, '90 Hz': 7}, 'Garanti Süresi': {'2 Yıl': 0, '3 Yıl': 1},
    'Klavye': {'Q Türkçe': 0, 'Q Türkçe (Aydınlatmalı)': 1, 'Q Türkçe (Aydınlatmasız)': 2, 'Q Türkçe (RGB Aydınlatmalı)': 3, 'Q Türkçe + Numerik (Aydınlatmalı)': 4, 'Q Türkçe + Numerik (Aydınlatmasız)': 5, 'Q Türkçe + Numerik (RGB Aydınlatmalı)': 6, 'Q İngilizce': 7, 'RGB Türkçe': 8},
    'Panel Tipi': {'Anti-Glare': 0, 'Full HD': 1, 'IPS': 2, 'LED': 3, 'Mikro Kenarlı': 4, 'SVA': 5, 'TN': 6, 'VA': 7}, 
    'Çözünürlük': {'1800 x 1200': 0, '1920 x 1080': 1, '1920 x 1200': 2, '2160 x 1440': 3, '2560 x 1440': 4, '2560 x 1600': 5, '2880 x 1800': 6, '3200 x 1800': 7, '3840 x 2160': 8},
    'Çözünürlük Standartı': {'FHD+': 0, 'Full HD (FHD)': 1, 'QHD': 2, 'QHD+': 3, 'Ultra HD 4K (UHD)': 4, 'WQHD': 5, 'WQXGA': 6, 'WUXGA': 7}, 'İşlemci Modeli': {'10300H': 0, '11320H': 1, '1135G7': 2, '11370H': 3, '11390H': 4, '11400': 5, '11400H': 6, '11600H': 7, '11800H': 8, '1235U': 9, '12450H': 10, '12500H': 11, '1255U': 12, '1260p': 13, '12650H': 14, '12700H': 15, '1280P': 16, '12900H': 17, '13420H': 18, '13450HX': 19, '13500H': 20, '13500HX': 21, '13620H': 22, '13650HX': 23, '13700H': 24, '13700HX': 25, '13900H': 26, '13900HX': 27, '13950HX': 28, '13980HX': 29, '14500HX': 30, '14700HX': 31, '14900HX': 32, '3700X': 33, '4600H': 34, '4800H': 35, '550': 36, '5600H': 37, '5800H': 38, '660': 39, '6600H': 40, '6800H': 41, '6800HS': 42, '6900HX': 43, '7535HS': 44, '7640HS': 45, '7735HS': 46, '7840HS': 47, '7845HX': 48, '7940HS': 49, '7945HX': 50, '7Y75': 51, '8100': 52, '9750H': 53}, 
    'İşlemci Tipi': {'AMD Ryzen 5': 0, 'AMD Ryzen 7': 1, 'AMD Ryzen 9': 2, 'Intel Core i5': 3, 'Intel Core i7': 4, 'Intel Core i9': 5}, 
    'İşlemci Çekirdek Sayısı': {'10': 0, '12': 1, '14': 2, '16': 3, '24': 4, '4': 5, '6': 6, '8': 7}, 
    'İşletim Sistemi': {'Free Dos': 0, 'Linux': 1, 'Windows': 2}, 
    'marka': {'ACER': 0, 'ASUS': 1, 'Casper': 2, 'Dell': 3, 'Game Garaj': 4, 'Gigabyte': 5, 'HP': 6, 'LENOVO': 7, 'MSI': 8, 'Monster': 9, 'Technopc': 10}, 
    'SSD Kapasitesi': {'1 TB': 0, '2 TB': 1, '256 GB': 2, '4 TB': 3, '500 GB': 4, '512 GB': 5}, 
    'Ram (Sistem Belleği)': {'16 GB': 0, '24 GB': 1, '32 GB': 2, '40 GB': 3, '48 GB': 4, '64 GB': 5, '8 GB': 6}, 'Ram (Sistem Belleği) Tipi': {'DDR4': 0, 'DDR5': 1, 'DDR6': 2, 'LPDDR5': 3}}

st.title("Gaming Laptop Fiyat Tahmin Uygulaması")
ekran_boyutu = st.selectbox("Ekran Boyutu", list(encoding_info['Ekran Boyutu'].keys()))
ekran_karti = st.selectbox("Ekran Kartı", list(encoding_info['Ekran Kartı'].keys()))
ekran_karti_hafizasi = st.selectbox("Ekran Kartı Hafızası", list(encoding_info['Ekran Kartı Hafızası'].keys()))
ekran_yenileme_hizi = st.selectbox("Ekran Yenileme Hızı", list(encoding_info['Ekran Yenileme Hızı'].keys()))
klavye = st.selectbox("Klavye", list(encoding_info['Klavye'].keys()))
panel_tipi = st.selectbox("Panel Tipi", list(encoding_info['Panel Tipi'].keys()))
ram_bellek = st.selectbox("Ram (Sistem Belleği)", list(encoding_info['Ram (Sistem Belleği)'].keys()))
ram_tipi = st.selectbox("Ram (Sistem Belleği) Tipi", list(encoding_info['Ram (Sistem Belleği) Tipi'].keys()))
ssd_kapasitesi = st.selectbox("SSD Kapasitesi", list(encoding_info['SSD Kapasitesi'].keys()))
cozunurluk = st.selectbox("Çözünürlük", list(encoding_info['Çözünürlük'].keys()))
cozunurluk_standarti = st.selectbox("Çözünürlük Standartı", list(encoding_info['Çözünürlük Standartı'].keys()))
islemci_modeli = st.selectbox("İşlemci Modeli", list(encoding_info['İşlemci Modeli'].keys()))
islemci_tipi = st.selectbox("İşlemci Tipi", list(encoding_info['İşlemci Tipi'].keys()))
islemci_cikirdek_sayisi = st.selectbox("İşlemci Çekirdek Sayısı", list(encoding_info['İşlemci Çekirdek Sayısı'].keys()))
isletim_sistemi = st.selectbox("İşletim Sistemi", list(encoding_info['İşletim Sistemi'].keys()))
marka = st.selectbox("Marka", list(encoding_info['marka'].keys()))

# Kullanıcı girişlerini dönüştür
input_data = {
    'Ekran Boyutu': [encoding_info['Ekran Boyutu'][ekran_boyutu]],
    'Ekran Kartı': [encoding_info['Ekran Kartı'][ekran_karti]],
    'Ekran Kartı Hafızası': [encoding_info['Ekran Kartı Hafızası'][ekran_karti_hafizasi]],
    'Ekran Yenileme Hızı': [encoding_info['Ekran Yenileme Hızı'][ekran_yenileme_hizi]],
    'Klavye': [encoding_info['Klavye'][klavye]],
    'Panel Tipi': [encoding_info['Panel Tipi'][panel_tipi]],
    'Ram (Sistem Belleği)': [encoding_info['Ram (Sistem Belleği)'][ram_bellek]],
    'Ram (Sistem Belleği) Tipi': [encoding_info['Ram (Sistem Belleği) Tipi'][ram_tipi]],
    'SSD Kapasitesi': [encoding_info['SSD Kapasitesi'][ssd_kapasitesi]],
    'Çözünürlük': [encoding_info['Çözünürlük'][cozunurluk]],
    'Çözünürlük Standartı': [encoding_info['Çözünürlük Standartı'][cozunurluk_standarti]],
    'İşlemci Modeli': [encoding_info['İşlemci Modeli'][islemci_modeli]],
    'İşlemci Tipi': [encoding_info['İşlemci Tipi'][islemci_tipi]],
    'İşlemci Çekirdek Sayısı': [encoding_info['İşlemci Çekirdek Sayısı'][islemci_cikirdek_sayisi]],
    'İşletim Sistemi': [encoding_info['İşletim Sistemi'][isletim_sistemi]],
    'marka': [encoding_info['marka'][marka]],
}

prediction = model.predict(pd.DataFrame(input_data))

st.write("Tahmin Edilen Fiyat:", prediction[0])



# In[ ]:




