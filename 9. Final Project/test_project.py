import pytest
import os
from project import real_time_data, historical_data, plot_historical_data

def test_real_time_data(capfd):

    #Test the real_time_data function to ensure it fetches real-time data without errors.

    try:
        real_time_data()
        out, _ = capfd.readouterr()  # Capture printed output
        assert "Current price:" in out or "Real-time data not available." in out, \
            "Test failed: Output does not indicate real-time price or handle unavailable data."
    except Exception as e:
        pytest.fail(f"Test failed: real_time_data raised an exception: {e}")

def test_historical_data():

    #Test the historical_data function to ensure it returns a valid DataFrame.

    try:
        df = historical_data()
        assert not df.empty, "Test failed: historical_data returned an empty DataFrame."
        assert 'close' in df.columns, "Test failed: 'close' column missing in DataFrame."
        assert '1_year_MA' in df.columns, "Test failed: '1_year_MA' column missing in DataFrame."
        assert '4_year_MA' in df.columns, "Test failed: '4_year_MA' column missing in DataFrame."
    except Exception as e:
        pytest.fail(f"Test failed: historical_data raised an exception: {e}")

def test_plot_historical_data(tmp_path):

    #Test the plot_historical_data function to ensure it generates a plot image file.

    try:
        df = historical_data()
        plot_historical_data(df)

        # Check if the plot file exists
        plot_path = os.path.join(tmp_path, "S&P500_historical_data.png")
        assert os.path.exists("S&P500_historical_data.png"), \
            "Test failed: Plot image file was not created."
        os.remove("S&P500_historical_data.png")  # Cleanup after the test
    except Exception as e:
        pytest.fail(f"Test failed: plot_historical_data raised an exception: {e}")

