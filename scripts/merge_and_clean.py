import pandas as pd

def load_and_clean(filepath, value_name):
    df = pd.read_csv(filepath, parse_dates=['date'])
    df.rename(columns={'value': value_name}, inplace=True)
    return df

def merge_datasets():
    # Load each dataset
    unemployment_df = load_and_clean("./data/raw/unemployment.csv", "Unemployment")
    inflation_df = load_and_clean("./data/raw/inflation.csv", "Inflation")
    
    # Merge datasets on 'Date'
    merged_df = pd.merge(inflation_df, unemployment_df, on='date')
    
    # Save merged data for further processing
    merged_df.to_csv("./data/processed/italy_economic_indicators.csv", index=False)
    print("Merged data saved to data/processed/italy_economic_indicators.csv")
    
if __name__ == "__main__":
    merge_datasets()
