import pickle
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/be814c563aba431f9b85230880565e8c')) #6

n = w3.eth.blockNumber

txs = []
timeStamps = []

blocks_file = open('output_total_1.txt','r')
blocks = blocks_file.readlines()


for j in range(210000,220000):
    i = int(blocks[j][:-1])
    block = w3.eth.getBlock(i,True)
    timeStamp = block.timestamp
    for k in range(0,len(block.transactions)):
        txs.append(block.transactions[k])
        timeStamps.append(timeStamp)
    if j % 1000 == 999:
        print(j)

    if j % 10000 == 9999:
        print(j)
        pickle.dump(txs,open('ether_trans'+str(j)+'pickle','wb'))
        pickle.dump(timeStamps,open('timeStamps'+str(j)+'pickle','wb'))
        txs = []
        timeStamps = []
    
    if j == len(blocks)-1:
        print(j)
        pickle.dump(txs,open('ether_trans'+str(j)+'pickle_last','wb'))
        pickle.dump(timeStamps,open('timeStamps'+str(j)+'pickle_last','wb'))
        txs = []
        timeStamps = []
           