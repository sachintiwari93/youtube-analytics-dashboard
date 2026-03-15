import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("youtube_videos.csv")

# Title
st.title("YouTube Channel Performance Analytics")

# KPI Metrics
col1, col2 = st.columns(2)
col1.metric("Total Videos", len(df))
col2.metric("Total Categories", df['category'].nunique())

# Dataset Preview
st.write("### Dataset Preview")
st.dataframe(df.head())

# Sidebar Filter
st.sidebar.title("Filter Options")
category_filter = st.sidebar.selectbox(
    "Select Category",
    df['category'].unique()
)

filtered_data = df[df['category'] == category_filter]

st.write("### Videos in Selected Category")
st.dataframe(filtered_data)

# Category Distribution Chart
st.write("### Videos by Category")

category_count = df['category'].value_counts()

fig, ax = plt.subplots()
sns.barplot(x=category_count.index, y=category_count.values)

plt.xlabel("Category")
plt.ylabel("Number of Videos")
plt.xticks(rotation=45)

st.pyplot(fig)

# Title Length Analysis
df['title_length'] = df['title'].apply(len)

st.write("### Title Length Distribution")

fig2, ax2 = plt.subplots()
sns.histplot(df['title_length'], bins=20)

plt.xlabel("Title Length")
plt.ylabel("Frequency")

st.pyplot(fig2)

# Top 10 Video Titles
st.write("### Top 10 Video Titles")

top_titles = df['title'].value_counts().head(10)

fig3, ax3 = plt.subplots()
sns.barplot(x=top_titles.values, y=top_titles.index)

plt.xlabel("Count")
plt.ylabel("Video Title")

st.pyplot(fig3)

# Search Video
st.write("### Search Video")

search = st.text_input("Enter video keyword")

if search:
    result = df[df['title'].str.contains(search, case=False)]
    st.dataframe(result)

# Download Filtered Data
st.write("### Download Data")

st.download_button(
    "Download Filtered Data",
    filtered_data.to_csv(index=False),
    file_name="filtered_videos.csv"
)