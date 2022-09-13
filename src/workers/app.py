import os
import faust
from dotenv import load_dotenv


load_dotenv()

def create_app(app_name):
    app = faust.App(
        app_name,
        broker=os.getenv('BROKER_SERVER', 'kafka://localhost:9092'),
        # broker_credentials=faust.SASLCredentials(
        #     username=os.getenv('BROKER_USERNAME', 'x'),
        #     password=os.getenv('BROKER_PASSWORD', 'y'),
        # )
    )

    return app
