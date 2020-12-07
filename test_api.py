# import twitter
# api = twitter.Api(consumer_key="HpjymvsHGkZfa4WtJg4Y3BgkN",
#                   consumer_secret="NqyQ6LblsqPSPVdo6IGFR1U5RQieeIsHSCaEPcRy4uG83GZhL4",
#                   access_token_key="AAAAAAAAAAAAAAAAAAAAAD0nKQEAAAAA3W3vlvuDaoP3ZHiff6%2BgaebX4PU%3DS8MtsU2fmrymJ3PHoOhqF5dtrMl9A7meddAoUoHvCL0zy0DJZv",
#                   access_token_secret="")

# import requests
# r = requests.get('https://api.twitter.com/1.1/collections/entries.json?id=custom-539487832448843776')
# print(r.json())

# python3 test_api.py

from searchtweets import load_credentials

load_credentials(filename="./search_tweets_creds_example.yaml",
                 yaml_key="search_tweets_api",
                 env_overwrite=False)
