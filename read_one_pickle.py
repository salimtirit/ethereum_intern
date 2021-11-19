from datetime import datetime
import pandas as pd
import pickle

file_number = 11780000

infile = open("ether_trans{}pickle".format(file_number),'rb')
data = pickle.load(infile)
infile.close()

infile_time = open("timeStamps{}pickle".format(file_number),"rb")
time = pickle.load(infile_time)
infile_time.close()

all_data = pd.DataFrame(data,columns=['blockNumber','transactionIndex','hash','from','to','value'])
all_data['time'] = [datetime.fromtimestamp(my_ether_time) for my_ether_time in time]
all_data['hash'] = [hash_data.hex() for hash_data in all_data['hash']]
all_data.columns = ['blocknumber','transactionindex','transactionhash', 'sender','receiver','value','transactiontime']

#burdan sonrasını gerekmedikçe çalıştırma

all_data.to_csv("{}.csv".format(file_number),index=None)

data = all_data.groupby(['transactiontime'])

data.describe()

data['blocknumber'].describe()['count'].sum()

