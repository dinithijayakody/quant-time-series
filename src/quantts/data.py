from pathlib import Path

import pandas as pd 
import yfinance as yf

def download_market_data(
        ticker: str = "SPY",
        start: str = "2010-01-01",
) -> pd.DataFrame: 
    """Download daily market data from Yahoo Finance"""

    data = yf.download(
        ticker,
        start=start,
        interval="1d",
        auto_adjust=False,
        multi_level_index=False,
        progress=False,
    )

    if data.empty:
        raise ValueError(f"No data downloaded for {ticker}")

    return data
def save_raw_data(
    data: pd.DataFrame,
    ticker: str,
    output_dir: str = "data/raw",
) -> Path:

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / f"{ticker.lower()}_daily.csv"

    data.to_csv(file_path)

    return file_path

def save_raw_data(
    data: pd.DataFrame,
    ticker: str,
    output_dir: str = "data/raw",
) -> Path:

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / f"{ticker.lower()}_daily.csv"

    data.to_csv(file_path)

    return file_path