import streamlit as st
import pandas as pd
import plost
from datetime import datetime, timedelta

# Настройка страницы
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard `version 2`')

# Параметры для визуализаций
st.sidebar.subheader('Line chart parameters')
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤️ by [Your Name](https://yourwebsite.com).
''')

# Функция для генерации тестовых данных
def generate_vulnerability_data():
    dates = [datetime.now() - timedelta(days=i) for i in range(14)]
    data = []
    for date in dates:
        nvd_count = random.randint(0, 10)
        mitre_count = random.randint(0, 10)
        bdu_count = random.randint(0, 10)
        data.append({'date': date, 'NVD': nvd_count, 'MITRE': mitre_count, 'BDU': bdu_count})
    return pd.DataFrame(data)

# Генерация данных уязвимостей
vulnerability_data = generate_vulnerability_data()

# Обработка данных для круговой диаграммы
total_nvd = vulnerability_data['NVD'].sum()
total_mitre = vulnerability_data['MITRE'].sum()
total_bdu = vulnerability_data['BDU'].sum()
donut_data = pd.DataFrame({
    'source': ['NVD', 'MITRE', 'BDU'],
    'count': [total_nvd, total_mitre, total_bdu]
})

# Row A: Метрики
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Total NVD", total_nvd)
col2.metric("Total MITRE", total_mitre)
col3.metric("Total BDU", total_bdu)

# Row B: Графики
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Vulnerabilities Over Time')
    st.line_chart(vulnerability_data.set_index('date'), height=plot_height)

with c2:
    st.markdown('### Vulnerability Sources')
    plost.donut_chart(
        data=donut_data,
        theta='count',
        color='source',
        legend='bottom', 
        use_container_width=True)

# Если вам нужно загрузить реальные данные, замените функцию generate_vulnerability_data() на код для парсинга уязвимостей с NVD, MITRE и BDU.
