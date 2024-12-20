#This is my Stock Market Analysis program, by Mario Albelda

import requests
import pandas as pd
import matplotlib.pyplot as plt

def main():
    real_time_data()
    data = historical_data()
    plot_historical_data(data)

# Function to extract the current price of the index and print it in USD
def real_time_data():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SPY&interval=60min&apikey=YOUR_API_KEY'
    r = requests.get(url)
    data = r.json()

    # Extracting the last closing price data from "Time Series (60min)"
    if "Time Series (60min)" in data:
        hour_data = list(data["Time Series (60min)"].keys())
        price = float(data["Time Series (60min)"][hour_data[0]]["4. close"])
        print(f"Current price: {price} USD")
    else:
        print("Real-time data not available.")

# Function to fetch and process historical data
def historical_data():
    # Fetch weekly data
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=SPY&apikey=YOUR_API_KEY'
    r = requests.get(url)
    data = r.json()

    # Extract the "Weekly Time Series" data
    weekly_data = data['Weekly Time Series']

    # Convert the weekly data to a Pandas DataFrame
    df = pd.DataFrame.from_dict(weekly_data, orient='index')

    # Rename columns for better readability
    df.columns = ['open', 'high', 'low', 'close', 'volume']

    # Convert the index to datetime format (from string)
    df.index = pd.to_datetime(df.index)

    # Convert the "close" prices to numeric (they are strings by default)
    df['close'] = pd.to_numeric(df['close'])

    # Calculate moving averages
    df['1_year_MA'] = df['close'].rolling(window=52).mean()
    df['4_year_MA'] = df['close'].rolling(window=208).mean()

    return df

# Function to plot historical data
def plot_historical_data(df):
    # Plot the weekly closing prices and moving averages
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['close'], label='S&P 500 Weekly Close Price', color='blue')
    plt.plot(df.index, df['1_year_MA'], label='1-Year Moving Average', color='orange')
    plt.plot(df.index, df['4_year_MA'], label='4-Year Moving Average', color='green')

    # Add labels, title, and legend
    plt.xlabel('Date (Year)')
    plt.ylabel('Price (USD)')
    plt.title('S&P 500 Weekly Prices with Moving Averages')
    plt.legend()

    # Save plot as an image
    plt.savefig("S&P500_historical_data.png")
    print("Historical data plot saved as 'S&P500_historical_data.png'")

if __name__ == "__main__":
    main()
