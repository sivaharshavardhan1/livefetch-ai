import streamlit as st
from playwright.sync_api import sync_playwright

st.set_page_config(page_title="Web Navigator AI", page_icon="🤖")

st.title("🤖 Web Navigator AI Prototype")
st.write("Enter any query, and the AI agent will search the web and show top 5 results.")

# Input from user
query = st.text_input("Enter your query:")

def search_web(query):
    results = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(f"https://www.google.com/search?q={query}")
            # Fetch top 5 search results
            results = page.locator('h3').all_text_contents()[:5]
            browser.close()
    except Exception as e:
        results = [f"Error occurred: {e}"]
    return results

if query:
    st.write("🔎 Searching the web...")
    top_results = search_web(query)
    st.write("### Top Results:")
    for idx, res in enumerate(top_results, 1):
        st.write(f"{idx}. {res}")