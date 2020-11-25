import pandas as pd
import numpy as np

def scrape(year):
    season = f"{str(year)[-2:]}{str(year+1)[-2:]}"
    try:
        df = pd.read_csv(f"https://www.football-data.co.uk/mmz4281/{season}/E0.csv", 
                         parse_dates=[1], 
                         encoding= 'unicode_escape'    # referee's name (0405)
                        )
        data = data.append(df).dropna(axis='columns', how='all')
    except:    # extra commas result in more columns than expected (0304)
        df = pd.read_csv(f"https://www.football-data.co.uk/mmz4281/{season}/E0.csv", 
                         parse_dates=[1], 
                         nrows=1)
        df = pd.read_csv(f"https://www.football-data.co.uk/mmz4281/{season}/E0.csv", 
                         parse_dates=[1], 
                         encoding= 'unicode_escape',    # referee's name (0405)
                         usecols=list(range(len(df.columns))))
    df.dropna(axis='columns', how='all', inplace=True)
    df.to_csv(f"data/{season}_E0.csv", index=False)
    return df

if __name__ == "__main__":
#     for year in np.arange(1993, 2020):
    for year in np.arange(2020, 2021):
        print(year)
        scrape(year)
