# CORD-19 Metadata Analysis
# ==========================

# Part 1: Load and Explore the Data
import pandas as pd

# Load the data
df = pd.read_csv('metadata.csv', low_memory=False)
print("Shape of dataset:", df.shape)

# Check data structure
print(df.info())

# Check missing values in key columns
important_cols = ['title', 'abstract', 'publish_time', 'journal', 'authors']
print("Missing values:\n", df[important_cols].isnull().sum())

# Part 2: Data Cleaning and Preparation

# Drop rows with missing title or publish_time
df_cleaned = df.dropna(subset=['title', 'publish_time'])

# Fill missing abstracts with placeholder
df_cleaned['abstract'] = df_cleaned['abstract'].fillna("No abstract available")

# Convert publish_time to datetime
df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')

# Drop rows with invalid dates
df_cleaned = df_cleaned.dropna(subset=['publish_time'])

# Extract publication year
df_cleaned['year'] = df_cleaned['publish_time'].dt.year

# Add abstract word count
df_cleaned['abstract_word_count'] = df_cleaned['abstract'].apply(lambda x: len(str(x).split()))

# Part 3: Data Analysis and Visualization
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

# Publications per year
year_counts = df_cleaned['year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
year_counts.plot(kind='bar')
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.tight_layout()
plt.show()

# Top Journals
top_journals = df_cleaned['journal'].value_counts().head(10)
plt.figure(figsize=(10,6))
top_journals.plot(kind='bar', color='skyblue')
plt.title('Top Journals Publishing COVID-19 Research')
plt.ylabel('Paper Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Word Cloud from Titles
title_text = ' '.join(df_cleaned['title'].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(title_text)

plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Frequent Words in Paper Titles')
plt.tight_layout()
plt.show()
