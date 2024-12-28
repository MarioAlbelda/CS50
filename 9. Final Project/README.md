# SMA (Stock Market Analysis)
#### Video Demo:  <https://youtu.be/GYoEg9ATakE>
#### Description:

The SMA program is a tool designed for analyzing financial data, focused on the S&P 500 index. This script retrieves real-time data and historical weekly data from the Alpha Vantage API, processes it, and presents insightful visualizations to help users better understand market trends.

### Features and Functionality:

1. **Real-Time Data Retrieval**:
   - The program includes a function (`real_time_data`) that fetches the most recent closing price of the S&P 500 index.
   - This data is displayed in USD, making it easy for users to quickly get a snapshot of the current market condition.

2. **Historical Data Analysis**:
   - Using the `historical_data` function, the program fetches weekly historical data for the S&P 500 index from the Alpha Vantage API.
   - The data is processed with the pandas library, converting it into a structured DataFrame format for further analysis.
   - Moving averages, including 1-year and 4-year averages, are calculated to help identify long-term market trends.

3. **Data Visualization**:
   - The `plot_historical_data` function generates a clear and informative plot of the historical closing prices alongside the moving averages.
   - The visualization provides a deeper understanding of market performance over time and highlights fluctuations in the S&P 500 index.
   - The plot is saved as an image file (`S&P500_historical_data.png`) for future reference.

### How It Works:

- **Setup**:
  - Users must ensure they have the required libraries (`requests`, `pandas`, and `matplotlib`) installed.
  - The program fetches data directly from Alpha Vantage API, requiring a valid API key.

- **Execution**:
  - Upon running the program, it retrieves the latest real-time data and processes the historical data.
  - Visualizations are automatically generated and saved, making it easy for users to analyze data without additional effort.

- **Testing**:
  - Accompanying the program are test functions written with pytest to ensure the reliability and accuracy of the script. These tests validate that data retrieval, processing, and plotting are working as expected.

### Testing Details:

The program includes automated tests using pytest to ensure its components function correctly:

1. **Real-Time Data Test**:
   - Validates that `real_time_data` fetches and displays the current price or handles missing data gracefully.

2. **Historical Data Test**:
   - Ensures `historical_data` returns a valid DataFrame with required columns and calculated moving averages.

3. **Plotting Test**:
   - Verifies that `plot_historical_data` successfully generates and saves the plot image.

These tests ensure reliability and robustness by validating individual components of the program.

### Use Cases:

This program is ideal for:
- Quickly access to real-time S&P 500 index data.
- Studying historical market trends.

By combining data fetching, analysis, and visualization, the sma.py program serves as a powerful tool for anyone seeking to explore financial market data.

