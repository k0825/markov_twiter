import json
import config
from datetime import datetime
from requests_oauthlib import OAuth1Session
import re


def connect_tw():
    # tweetを読み込む
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {'count': 20}
    list = []

    req = twitter.get(url, params=params)
    if req.status_code == 200:
        for tweet in json.loads(req.text):
            text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', "", tweet['text'])
            text = re.sub('RT', "", text)
            text = re.sub(r'@[\w]+:?\s?', "", text)
            person = { "text": text }
            list.append(person)
        return list
    else:
        print("GET ERROR {}".format(req.status_code))
        exit()


def output_data(docs):
    filename = 'tweet/{0:%Y%m%d_%H%M%S_%f}'.format(datetime.now()) + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(docs, f, indent=4, ensure_ascii=False)
    with open(filename, 'r', encoding='utf-8') as f:
        print(json.load(f))

def main():
    print('get tweet')
    output_data(connect_tw())

if __name__ == "__main__":
    main()
