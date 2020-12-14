# import twitter
# api = twitter.Api(consumer_key="HpjymvsHGkZfa4WtJg4Y3BgkN",
#                   consumer_secret="NqyQ6LblsqPSPVdo6IGFR1U5RQieeIsHSCaEPcRy4uG83GZhL4",
#                   access_token_key="AAAAAAAAAAAAAAAAAAAAAD0nKQEAAAAA3W3vlvuDaoP3ZHiff6%2BgaebX4PU%3DS8MtsU2fmrymJ3PHoOhqF5dtrMl9A7meddAoUoHvCL0zy0DJZv",
#                   access_token_secret="")

# import requests
# r = requests.get('https://api.twitter.com/1.1/collections/entries.json?id=custom-539487832448843776')
# print(r.json())

# python3 test_api.py

import json
from searchtweets import load_credentials, ResultStream, gen_rule_payload, collect_results
import datetime


premium_search_args = load_credentials(filename="./search_tweets_creds_example.yaml",
                 yaml_key="search_tweets_api",
                 env_overwrite=False)

# rule = gen_rule_payload("beyonce", results_per_call=100) # testing with a sandbox account
# print(rule)

# query = "@V2019N (#COVID19 OR patients OR pandemic OR hospitalization OR virus OR corona OR (tested positive) OR infected OR vaccine)"
# rule = gen_rule_payload(query, results_per_call=100, from_date="2020-01-01", to_date="2020-03-31")

# try:
#     tweets = collect_results(rule, max_results=100, result_stream_args=premium_search_args)
# except:
#     pass # Handle error here.

# [print(tweet.all_text, end='\n\n') for tweet in tweets[0:10]]; 

# rs = ResultStream(rule_payload=rule, max_results=3000, **premium_search_args)
# print(rs)
# tweets = rs.stream()

today = datetime.date.today()
start_date = today + datetime.timedelta(-30)
rule = gen_rule_payload("from:NYCASP", from_date=str(start_date), to_date=str(today), results_per_call=500)
print(rule)

rs = ResultStream(rule_payload=rule, max_results=500, max_pages=1, **premium_search_args)
print(rs)

tweets = rs.stream()
list_tweets = list(tweets)
[print(tweet.all_text, end='\n\n') for tweet in list_tweets[0:5]]

# with open('tweetsData.json', 'a', encoding='utf-8') as f:
#     for tweet in rs.stream():
#         json.dump(tweet, f)
#         f.write('\n')
        # print(tweet)
print('done')