# import twitter
# api = twitter.Api(consumer_key="HpjymvsHGkZfa4WtJg4Y3BgkN",
#                   consumer_secret="NqyQ6LblsqPSPVdo6IGFR1U5RQieeIsHSCaEPcRy4uG83GZhL4",
#                   access_token_key="AAAAAAAAAAAAAAAAAAAAAD0nKQEAAAAA3W3vlvuDaoP3ZHiff6%2BgaebX4PU%3DS8MtsU2fmrymJ3PHoOhqF5dtrMl9A7meddAoUoHvCL0zy0DJZv",
#                   access_token_secret="")

# import requests
# r = requests.get('https://api.twitter.com/1.1/collections/entries.json?id=custom-539487832448843776')
# print(r.json())

# python3 test_api.py

from searchtweets import load_credentials, ResultStream, gen_rule_payload, collect_results


premium_search_args = load_credentials(filename="./search_tweets_creds_example.yaml",
                 yaml_key="search_tweets_api",
                 env_overwrite=False)

rule = gen_rule_payload("beyonce", results_per_call=100) # testing with a sandbox account
print(rule)

tweets = collect_results(rule, max_results=100, result_stream_args=premium_search_args)

[print(tweet.all_text, end='\n\n') for tweet in tweets[0:10]]; 