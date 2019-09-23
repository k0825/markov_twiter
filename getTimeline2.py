import json
import config
import datetime
from markov import markov_twitter
from requests_oauthlib import OAuth1Session
import re


def main():
    filename = 'tweet.txt'
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)
    purl = "https://api.twitter.com/1.1/statuses/update.json"
    gurl = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    gparams = {'count': 100}
    gres = twitter.get(gurl, params=gparams)

    if gres.status_code == 200:
        with open(filename, 'a', encoding='utf-8') as f:
            for getw in json.loads(gres.text):
                #URL,RT以外の単語を正規表現で取得
                tw = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', getw['text'])
                tw = re.sub('RT', '', tw)
                tw = re.sub(r'@[\w]+:?\s?', '', tw)
                f.write(tw)
    else:
        print('Writing Failed')


    postw = markov_twitter(filename)
    pparams = { 'status': postw }
    print(postw)


if __name__ == '__main__':
    main()
    input("何かキーを押すと終了します")
