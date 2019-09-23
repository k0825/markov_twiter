import json
import config
from requests_oauthlib import OAuth1Session


def main():
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)
    purl = "https://api.twitter.com/1.1/statuses/update.json"
    gurl = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    gparams = {'count': 100}

    tweet = input('> ')
    pparams = {'status': tweet}
    pres = twitter.post(purl, params=pparams)

    if pres.status_code == 200:
        print('Successfully')
        gres = twitter.get(gurl, params=gparams)
        if gres.status_code == 200:
            for line in json.loads(gres.text):
                print('{} :: {}'.format(line['user']['name'], line['text']))
                print(line['created_at'])
        else:
            print('GET ERROR:{}'.format(gres.status_code))
    else:
        print('POST ERROR:{}'.format(pres.status_code))


if __name__ == '__main__':
    main()
