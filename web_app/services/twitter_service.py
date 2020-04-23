from tweepy import OAuthHandler,API
from os import getenv
from dotenv import load_dotenv

# load creds into memory from .env
load_dotenv()
TWITTER_API_KEY = getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")

def api_client():
    """Init a connection to the offical twitter api hanler and returns a session
    for the api instance.
    requires:
    ----------
    .env file in the base directory with :

    TWITTER_API_KEY

    TWITTER_API_SECRET

    TWITTER_ACCESS_TOKEN

    TWITTER_ACCESS_TOKEN_SECRET
    """
    # authenicate with API access information provided in env.
    auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    # init an API session with the auth
    api = API(auth)
    return api
