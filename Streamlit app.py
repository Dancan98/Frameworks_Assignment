import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers using metadata.csv")

@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    df = df.dropna(subset=['title', 'publish_time'])
    df['abstract'] = df['abstract'].fillna("No abstract available")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df = df.dropna(subset=['publish_time'])
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# Year filter
st.sidebar.header("Filters")
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.sidebar.slider("Select year range", min_year, max_year, (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications per year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# Word cloud of titles
st.subheader("Word Cloud of Paper Titles")
title_text = ' '.join(filtered_df['title'].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(title_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
st.pyplot(plt)

# Data preview
st.subheader("Sample of the Data")
st.write(filtered_df[['title', 'journal', 'publish_time']].head())
