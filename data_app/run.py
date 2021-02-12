import pandas as pd
from datetime import datetime
from io import BytesIO

from minio import Minio
from minio.error import S3Error

MINIO_SERVER = "play.min.io"
MINIO_ACCESS_KEY = "Q3AM3UQ867SPQQA43P2F"
MINIO_SECRET_KEY = "zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG"

DATA_BUCKET = 'cntnrzd-dtsc-2021-02-12'

DATA_FOLDER = './data'
TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

FILENAME = f'stats_{TIMESTAMP}.csv'

def save_results(df,fname):
    try:
        client = Minio(
            MINIO_SERVER,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
        )
        # Make DATA_BUCKET if not exist.
        bucket_exists = client.bucket_exists(DATA_BUCKET)
        if not bucket_exists:
            client.make_bucket(DATA_BUCKET)
        else:
            print(f"Bucket {DATA_BUCKET} already exists")

         # save the DF as CSV
         # https://stackoverflow.com/questions/58955092/how-to-save-panda-data-frame-as-csv-in-minio

        csv_bytes = df.to_csv(index=False,header=True).encode('utf-8')
        csv_buffer = BytesIO(csv_bytes)

        client.put_object(DATA_BUCKET,
                            fname,
                            data = csv_buffer,
                            length=len(csv_bytes),
                            content_type='application/csv')

    except S3Error as exc:
        print(F"Error: {exc}")


def compute_stats():
    input_stats = pd.read_csv(f'{DATA_FOLDER}/input.csv',header=0)
    stats = input_stats.groupby(['platform'],as_index=False).agg(
        count = ('user_id',pd.Series.count),
        unique = ('user_id',pd.Series.nunique)
    )
    #stats.to_csv(f'{DATA_FOLDER}/stats_{TIMESTAMP}.csv',index=False,header=True)
    save_results(stats,FILENAME)


if __name__ == "__main__":
    compute_stats()