import pandas as pd
CLIENT_ID = 'V4pzPOqb9yslDw'
SECRET_TOKEN = 'aHASmWLlK4feSRQMsmfu5D0xUR2QmQ'
import requests
from SentimentProcessing import SentimentProcessing
class RedditApp():
    def __init__(self):
        self.coinScore = {}
        self.coinList = ['BTC', 'ETH', 'BNB', 'USDT', 'DOT', 'XRP', 'ADA', 'UNI', 'LTC', 'LINK', 'BCH', 'THETA', 'XLM',
                         'FIL', 'USDC', 'TRX', 'WBTC', 'KLAY', 'DOGE', 'BTT', 'VET', 'LUNA', 'EOS', 'SOL', 'CRO',
                         'AAVE', 'XTZ', 'XMR', 'BSV', 'MIOTA', 'ATOM', 'HOT', 'NEO', 'AVAX', 'BUSD', 'FTT', 'KSM',
                         'XEM', 'ALGO', 'DAI', 'HT', 'EGLD', 'DASH', 'COMP', 'CHZ', 'STX', 'HBAR', 'CAKE', 'SNX', 'DCR',
                         'ZIL', 'BTCB', 'MKR', 'GRT', 'ZEC', 'RUNE', 'NEAR', 'ENJ', 'LEO', 'SUSHI', 'ETC', 'TFUEL',
                         'MATIC', 'BAT', 'DENT', 'UST', 'NPXS', 'RVN', 'NEXO', 'ONT', 'UMA', 'MANA', 'CEL', 'ICX', 'SC',
                         'YFI', 'ONE', 'ZRX', 'BNT', 'WAVES', 'FTM', 'DGB', 'FLOW', 'QTUM', 'OMG', 'HNT', 'CHSB', 'RSR',
                         'ANKR', 'BTG', 'OKB', 'REV', 'REN', 'WRX', 'PAX', 'BTMX', 'CELO', 'AR', 'VGX', 'CFX', 'XVG',
                         'IOST', 'CRV', 'DODO', 'WIN', 'CKB', 'LSK', '1INCH', 'HUSD', 'NANO', 'LPT', 'OGN', 'KCS',
                         'ZEN', 'LRC', 'STORJ', 'SNT', 'OCEAN', 'MED', 'STMX', 'RENBTC', 'ZKS', 'KNC', 'KIN', 'MVL',
                         'GLM', 'HEDG', 'VTHO', 'MAID', 'XVS', 'FUN', 'EWT', 'ORBS', 'ALPHA', 'FET', 'REP', 'ANT',
                         'QNT', 'IOTX', 'SKL', 'REEF', 'SAND', 'STEEM', 'WAXP', 'KAVA', 'BTS', 'CELR', 'META', 'BAL',
                         'TEL', 'CVC', 'SXP', 'AGI', 'VLX', 'MTL', 'POLY', 'ARDR', 'BADGER', 'JST', 'BAND', 'WAN',
                         'MARO', 'ARK', 'NMR', 'UBT', 'SWAP', 'TUSD', 'UTK', 'KMD', 'IQ', 'STRAX', 'NKN', 'BCD', 'BORA',
                         'QKC', 'ROSE', 'XOR', 'SRM', 'OXT', 'TRAC', 'BTM', 'CVT', 'MFT', 'AVA', 'NOIA', 'ELF', 'POWR',
                         'RIF', 'COTI', 'POLS', 'HIVE', 'GNO', 'ALICE', 'HNS', 'TOMO', 'NU', 'RLC', 'SCRT', 'XHV',
                         'RDD']

        self.calculateScores()
    # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'

    def calculateScores(self):
        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

        # here we pass our login method (password), username, and password
        data = {'grant_type': 'password',
                'username': 'bigdoubloon',
                'password': '123qwe4r'}

        # setup our header info, which gives reddit a brief description of our app
        headers = {'User-Agent': 'MyBot/0.0.1'}

        # send our request for an OAuth token
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=headers)

        # convert response to JSON and pull access_token value
        TOKEN = res.json()['access_token']

        # add authorization to our headers dictionary
        headers['Authorization'] = f'bearer {TOKEN}'
        print(headers)

        # while the token is valid (~2 hours) we just add headers=headers to our requests
        requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

        CryptoCurrencyList = []
        CryptoCurrencyRequest = requests.get("https://oauth.reddit.com/r/CryptoCurrency/hot",
                           headers=headers)

        count = 0

        for post in CryptoCurrencyRequest.json()['data']['children']:
            if count<= 1:
                # for x in post['data']:
                #     if 'created' in x:
                #         print(x, "\n")
                print(post['data']['created'])
                count += 1
            CryptoCurrencyList.append((post['data']['title'] + post['data']['selftext'] + post['data']['author_fullname'], post['data']['created']/5000000000))



        CryptoMarketsList = []
        CryptoMarketsRequest = requests.get("https://oauth.reddit.com/r/CryptoMarkets/hot",
                           headers=headers)

        for post in CryptoMarketsRequest.json()['data']['children']:
            CryptoMarketsList.append((post['data']['title'] + post['data']['selftext'] + post['data']['author_fullname'], post['data']['created']/5000000000))



        res = requests.get("https://oauth.reddit.com/r/Bitcoinmarkets/hot",
                           headers=headers)
        #
        # for post in res.json()['data']['children']:
        #     print(post['data']['selftext'])

        self.coinScore = []
        for coin in self.coinList:
            newCoin = {}
            newCoin["name"] = coin
            newCoin["score"] = 0
            self.coinScore.append(newCoin)

        coinScore1 = self.coinScore

        print(self.coinScore)
        print("\n\n\n")

        analyzer = SentimentProcessing()

        for coin in self.coinScore:
            for post in CryptoCurrencyList:
                if coin["name"] in post[0] or coin["name"].lower() in post[0] or coin["name"].title() in post[0]:
                    coin["score"] += 1
                    coin["score"] += post[1]
                    if analyzer.getSentimentScore(post[0]) == "Positive":
                        coin["score"] += 2
                    elif analyzer.getSentimentScore(post[0]) == "Negative":
                        coin["score"] -= 2
                    print(post[1])
            for post in CryptoMarketsList:
                if coin["name"] in post[0] or coin["name"].lower() in post[0] or coin["name"].title() in post[0]:
                    coin["score"] += 1
                    coin["score"] += post[1]
                    if analyzer.getSentimentScore(post[0]) == "Positive":
                        coin["score"] += 2
                    elif analyzer.getSentimentScore(post[0]) == "Negative":
                        coin["score"] -= 2

        coinScore2 = self.coinScore
        print(self.coinScore)

    def getCoinScores(self):
        self.coinScore = sorted(self.coinScore, key=lambda k: k['score'], reverse=True)
        return self.coinScore