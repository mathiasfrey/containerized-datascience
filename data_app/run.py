import pandas as pd
from datetime import datetime

DATA_FOLDER = './data'
TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

def compute_stats():
    input_stats = pd.read_csv(f'{DATA_FOLDER}/input.csv',header=0)
    stats = input_stats.groupby(['platform'],as_index=False).agg(
        count = ('user_id',pd.Series.count),
        unique = ('user_id',pd.Series.nunique)
    )
    #stats.to_csv(f'{DATA_FOLDER}/stats_{TIMESTAMP}.csv',index=False,header=True)
    print(stats)


if __name__ == "__main__":
    print("Computation")
    compute_stats()