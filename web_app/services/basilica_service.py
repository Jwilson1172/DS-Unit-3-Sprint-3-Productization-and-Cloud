from basilica import Connection
from os import getenv
from dotenv import load_dotenv

# load the enviroment variables from .env
load_dotenv()
API_KEY = getenv("BASILICA_API_KEY")

# create a new balistica connection
connection = Connection(API_KEY)
