import os
import faust
from dotenv import load_dotenv

load_dotenv()
app = faust.App('produtitas', broker=os.getenv('BROKER_SERVER', 'kafka://localhost:9092'))
