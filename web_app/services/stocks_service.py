from requests import get
from json import loads
from os import getenv
from dotenv import load_dotenv

load_dotenv()
API_KEY = getenv("ALPHAVANTAGE_API_KEY")

def get_quote(symbol):
    """Squery the alpha vantage API and grab the squotes for the stock symbol provided
    Arguments:
    ----------
    symbol {str} : the stock symbol disgnator to look up
    """
    stock_symbol = symbol
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={API_KEY}"
    response = get(request_url)
    parsed_response = loads(response.text)

    return parsed_response
