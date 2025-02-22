import streamlit as st
import feedparser
import json

# Function to fetch tech news
def fetch_tech_trends():
    url = "https://news.google.com/rss/search?q=technology+trends&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    
    articles = []
    for entry in feed.entries[:5]:  # Get top 5 articles
        articles.append({
            "title": entry.title,
            "summary": entry.summary[:180] + "...",
            "link": entry.link
        })
    
    return articles

# Streamlit API Mode
st.set_page_config(layout="wide")
st.header("📰 Tech Trends Scraper API")

articles = fetch_tech_trends()

# Return JSON output
st.json({"tech_trends": articles})
