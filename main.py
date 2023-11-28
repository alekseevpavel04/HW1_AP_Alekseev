import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
file_path = 'merged_df.csv'  # Укажите путь к вашему CSV файлу
data = pd.read_csv(file_path)

# Заголовок приложения
st.title('Разведочный анализ данных')

# Отображение первых строк данных
st.subheader('Первые строки данных')
st.write(data.head())

# Графики распределений признаков
st.subheader('Графики распределений признаков')

# Выберите колонну для построения гистограммы
selected_column = st.selectbox('Выберите колонку для построения гистограммы', data.columns)
fig, ax = plt.subplots(figsize=(8, 6))  # Создаем объект figure и axis
sns.histplot(data[selected_column], kde=True, ax=ax)
plt.grid()
st.pyplot(fig)  # Передаем объект figure в st.pyplot()

# Матрица корреляций
st.subheader('Матрица корреляций')
fig, ax = plt.subplots(figsize=(10, 8))  # Создаем объект figure и axis для корреляций
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)  # Передаем объект figure в st.pyplot()

# Графики зависимостей целевой переменной и признаков
st.subheader('Графики зависимостей целевой переменной и признаков')

# Выбираем признак для оси y
selected_column_y = st.selectbox('Выберите признак для оси y', data.columns)

# Создаем график с осью x как 'TARGET' и осью y как выбранный признак
fig, ax = plt.subplots(figsize=(8, 6))  # Создаем объект figure и axis
sns.scatterplot(x='TARGET', y=selected_column_y, data=data, ax=ax)
st.pyplot(fig)  # Передаем объект figure в st.pyplot()

# Boxplots для сравнения различных категорий
st.subheader('Boxplots для сравнения различных категорий относительно TARGET')

# Выбор колонны для сравнения
selected_column_boxplot = st.selectbox('Выберите колонку для построения Boxplot', data.columns)

fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='TARGET', y=selected_column_boxplot, data=data, ax=ax)
st.pyplot(fig)

# streamlit run main.py