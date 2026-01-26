import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Page setup
st.set_page_config(page_title="StatGuard Dashboard", layout="wide")

st.title("🛰️ StatGuard-Metric: ML Experiment Arena")
st.markdown("Визуализация и мониторинг результатов A/B тестирования")


# 1. Data download out DataBase(SQL)
def load_data():
    conn = sqlite3.connect("data/experiments.db")
    # Pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM experiment_logs", conn)
    conn.close()
    return df


df = load_data()

# 2. Shows the metrics
if not df.empty:
    st.subheader("Последние результаты")
    last_test = df.iloc[-1]

    col1, col2, col3, col4 = st.columns(4) # Теперь 4 колонки
    col1.metric("Тест", last_test['test_name'])
    col2.metric("P-Value", f"{last_test['p_value']:.4f}")
    col3.metric("Прирост (Lift)", f"{last_test['lift']:.2f}%")
    col4.metric("Метод", last_test['test_type']) # ПОКАЗЫВАЕМ ТИП ТЕСТА

    # 3. Visualizing the history of experiments
    st.divider()
    st.subheader("История всех запусков")

    # We draw a graph of the increase (Lift) by time
    fig = px.bar(df, x='timestamp', y='lift', color='is_significant',
                 title="Динамика прироста (Зеленый = значимо)",
                 labels={'lift': 'Прирост (%)', 'timestamp': 'Дата и время'})
    st.plotly_chart(fig, use_container_width=True)

    # 4. Raw data table
    st.subheader("Журнал экспериментов (Raw SQL Data)")
    st.dataframe(df, use_container_width=True)
else:
    st.warning("База данных пуста. Запусти main.py, чтобы создать первый эксперимент!")
