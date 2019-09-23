import json, config
from requests_oauthlib import OAuth1Session


def main():
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"  # load endpoint of timeline
    params = {'count': 100}
    res = twitter.get(url, params=params)

    if res.status_code == 200:
        for line in json.loads(res.text):
            print(line['text'])

    else:
        print('Filed:{0}'.format(res.status_code))


if __name__ == '__main__':
    main()
