import os
import faust
from dotenv import load_dotenv


load_dotenv()
app = faust.App(
    'produtitas',
    broker=os.getenv('BROKER_SERVER', 'kafka://localhost:9092'),
    # topic_partitions=3,
    # broker_credentials=faust.SASLCredentials(
    #     username=os.getenv('BROKER_USERNAME', 'x'),
    #     password=os.getenv('BROKER_PASSWORD', 'y'),
    # )
)


if __name__ == '__main__':
    app.main()
