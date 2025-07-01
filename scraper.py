# use yfinance to scrape news
import yfinance as yf
import pandas as pd

def scrape_news_yfinance(ticker: str):
    news = ticker.news
    df = pd.DataFrame(news)
    # Convert dict columns to separate columns
    df["title"] = df["content"].apply(lambda x: x.get("title", ""))
    df["summary"] = df["content"].apply(lambda x: x.get("summary", ""))
    df["pub_date"] = df["content"].apply(lambda x: x.get("pubDate", ""))
    df = df[["title", "summary", "pub_date"]]
    return df

# -----------------------------------------------------------------------
import os # set environment variable for yfinance
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36"

from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool

def invoke_news_tool_langchain(ticker: str):
    tool = YahooFinanceNewsTool()
    res = tool.invoke(ticker)
    return res