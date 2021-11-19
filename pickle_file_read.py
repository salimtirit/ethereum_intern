from datetime import datetime
import pandas as pd
import pickle

for i in range (11400000,11420000,10000):
    my_time = datetime.now()
    infile = open("ether_trans{}pickle".format(i),'rb')
    ether = pickle.load(infile)
    infile.close()

    infile_time = open("timeStamps{}pickle".format(i),"rb")
    ether_time = pickle.load(infile_time)
    infile_time.close()

    col_names = ['blocknumber','transactionindex','transactionhash', 'sender','receiver','value','transactiontime']
    all_data = pd.DataFrame(ether,columns=['blockNumber','transactionIndex','hash','from','to','value'])
    #all_data['time'] = ['to_date('+"'{}'".format(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(my_ether_time)))+", 'dd-mm-yyyy hh:mi:ss')" for my_ether_time in ether_time]
    #all_data['time'] = [time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(my_ether_time)) for my_ether_time in ether_time]
    #all_data['time'] = [time.localtime(my_ether_time) for my_ether_time in ether_time]
    all_data['time'] = [datetime.fromtimestamp(my_ether_time) for my_ether_time in ether_time]
    all_data['hash'] = [hash_data.hex() for hash_data in all_data['hash']]
    all_data.columns = col_names
    all_data.to_csv("{}.csv".format(i),index=None)
    print(datetime.now()-my_time)

#my_time = datetime.now()

#try:
#    DIALECT = 'oracle'
#    SQL_DRIVER = 'cx_oracle'
#    USERNAME = 'SYS' #enter your username
#    PASSWORD = 'h3mSalim.2021' #enter your password
#    HOST = 'localhost' #enter the oracle db host url
#    PORT = 1521 # enter the oracle port number
#    SERVICE = 'XEPDB1' # enter the oracle db service name
#    ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE 
#
#    engine = create_engine(ENGINE_PATH_WIN_AUTH,connect_args={"mode":cx_Oracle.SYSDBA})
#
#    
#    test_df = pd.read_sql_query('SELECT * FROM ethereum_data', engine)
#
#    all_data.to_sql('ethereum_data',engine, if_exists='append',index=False)
#except cx_Oracle.Error as error:
#    print('Error occurred:')
#    print(error)
#
#
#print(datetime.now()-my_time)