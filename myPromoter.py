# import the required libraries
import time
import tweepy
from variables_gigurl_woeid import gig_list, woeid_list
# to read the configuration file
import configparser



def get_api():
    """
    authenticate and connect with the twitter bot using keys and tokens
    :return
        api: obeject of the tweepy api
    """
    # pass interpolation=None so it doesn't raise error (https://stackoverflow.com/questions/14340366/configparser-and-string-with)
    config = configparser.ConfigParser(interpolation=None)
    # read the configuration file
    config.read("config.ini")

    # get the credentials
    API_KEY = config['twitter']["api_key"]
    API_KEY_SECRET = config['twitter']["api_key_secret"]
    ACCESS_TOKEN = config['twitter']["access_token"]
    ACCESS_TOKEN_SECRET = config['twitter']["access_token_secret"]

    # authenticate
    auth = tweepy.OAuth1UserHandler(consumer_key=API_KEY,
                                    consumer_secret=API_KEY_SECRET,
                                    access_token=ACCESS_TOKEN,
                                    access_token_secret=ACCESS_TOKEN_SECRET
                                   )
    # initialize API
    api = tweepy.API(auth)
    
    return api

def get_trends(api_obj, country_woeid):
    """
    get trends usind woeid 
    :return:
        list of 5 trends
    """
    # get trends
    trends = api_obj.get_place_trends(country_woeid)
    # empty list to hold trends with hashtag
    trend_list = []
    for trend in trends[0]["trends"]:
        if "#" in trend["name"]:
            trend_list.append(trend["name"])
            
    return trend_list[:6]

def make_post(api_obj, list_of_trends, gig_url):
    """
    make the text to post and tweet
    """
    tweet_post = gig_url + "\n" + "\n".join(list_of_trends)
    api_obj.update_status(tweet_post)


def run():
    """
    runs the bot
    """
    api = get_api()
    
    # run forever
    while True:

        for loc_id in woeid_list: # (cyprus, belarus, uk, norway, australia, us, austria, sweden)
            trend_list = get_trends(api, loc_id)

            for url in gig_list:
                make_post(api, trend_list, url)
                time.sleep(5)
            # wait for 2 hours before getting the trend of another country
            # meaning get individual country trends every 16 hours 
            time.sleep(300)
            

            
if __name__ == "__main__":
    run()
