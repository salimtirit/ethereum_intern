from pandas.core.base import DataError
import requests
import pandas as pd
from datetime import datetime
import time

header = {
    'x-api-key' : 'c7909e26-0b66-424e-8264-a2ecea6ca5e8' #seven
}
complete = pd.read_csv('Complete.csv')

addresses = complete['Address'].to_list()
atla = {
2373,
2579,
3197,
3323,
3399,
3472,
3485,
3877,
4100,
4134,
4237,
4418,
4582,
4652,
4217,
4670}
#k=4582
data = []
bas = 4230
son = 4231 #4300 olcak ??******************************************
for k in range(bas,son):
    if k in atla:
        continue
    else:

        address = addresses[k]

        print(k,"  ",address)

        length = 50
        i = 0
        if k == bas:
            i = 6411 
        while(length==50):
            ret = requests.get(url='https://api-eu1.tatum.io/v3/ethereum/account/transaction/{}?pageSize=50&offset={}'.format(address,str(i*50)),headers= header)
            ret = ret.json()

            length = len(ret)
            i+=1

            for j in range(0,length):
                transactiontime = requests.get(url='https://api-eu1.tatum.io/v3/ethereum/block/{}'.format(ret[j]['blockHash']),headers=header).json()
                transactiontime = transactiontime['timestamp']
                data.append([ret[j]['blockNumber'],ret[j]['transactionIndex'],ret[j]['transactionHash'],ret[j]['from'],ret[j]['to'],ret[j]['value'],datetime.fromtimestamp(transactiontime)])
                time.sleep(0.2)

            if i > 10000 and i%1000==0:
                print("too much")
        
fileName = "{}.csv".format(son)

AllData = pd.DataFrame(data,columns=['blocknumber','transactionindex','transactionhash','sender','receiver','value','transactiontime'])
AllData.to_csv(fileName,index=None)
print("length ",len(addresses))