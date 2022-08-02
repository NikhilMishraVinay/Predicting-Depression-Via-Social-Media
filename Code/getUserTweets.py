import requests

Bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAJbbQEAAAAAx9JXxtPeZ%2FK0KQYMTPhKfIKx0YA%3DOm3YaPKoqeiZZV573gD1TGN6QUEpA9SMXkY2iQNY2HzEEPEOGb'

def connect_to_twitter():
  return {"Authorization" : "Bearer {}".format(Bearer_token)}

def make_request(headers):
  url = 'https://api.twitter.com/2/users/2244994945/tweets/'
  #params = 'query=from:TwitterDev'
  params = "max_results=90&tweet.fields=lang,conversation_id,created_at"
  return requests.request("GET",url,params=params,headers=headers).json()

headers = connect_to_twitter()

response = make_request(headers)

public_tweet=[]
def public_tweets():
    for tweet in response['data']:
      public_tweet.append(tweet['text'])
    return public_tweet

