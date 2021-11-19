import pickle
from web3 import Web3


w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/0ec754f1d1d34ef9a431fb08fda2d1d1'))

n = w3.eth.blockNumber

txs = []
timeStamps = []
kaldik=  11789999

for i in range(kaldik,11779999 ,-1):
   
    block = w3.eth.getBlock(i,True)
    timeStamp = block.timestamp
    for j in range(0,len(block.transactions)):
        txs.append(block.transactions[j])
        timeStamps.append(timeStamp)

    if i % 1000 == 0:
        print(i)
       
    if i % 10000 == 0:
        print(i)
        pickle.dump(txs,open('ether_trans'+str(i)+'pickle','wb'))
        pickle.dump(timeStamps,open('timeStamps'+str(i)+'pickle','wb'))
        txs = []
        timeStamps = []
        