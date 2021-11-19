import requests
import pandas

header = {
    'x-api-key' : 'ee5477ce-d4d0-406b-8791-aa20c6ded556'
}
complete = pandas.read_csv('Complete.csv')

addresses = complete['Address'].to_list()

#k=3997 not max
for k in range(4290,4300):
    address = addresses[k]

    output = open('output1.txt','a')

    print(k,"  ",address)
    length = 50
    i = 0
    while(length==50):
        ret = requests.get(url='https://api-eu1.tatum.io/v3/ethereum/account/transaction/{}?pageSize=50&offset={}'.format(address,str(i*50)),headers= header)
        ret = ret.json()

        length = len(ret)
        i+=1

        for j in range(0,length):
            output.write(str(ret[j]['blockNumber'])+"\n")

        if i > 10000 and i%1000==0:
            print("too much")

    output.close()

print("length ",len(addresses))