import cx_Oracle
import pickle
import config as cfg
from datetime import datetime

def insert_billing(transactionhash, sender, receiver, value, date):
    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into ethereum_data values(:transactionhash, :sender, :receiver, :value, :date)')

    try:
        # establish a new connection
        with cx_Oracle.connect(user = cfg.username,
                            password = cfg.password,
                            dsn = "localhost:1521/XEPDB1",
                            mode=cx_Oracle.SYSDBA) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                #cursor.execute(sql, [transactionhash, sender, receiver, value, date])

                #print("INSERT INTO ethereum_data VALUES ('{0}', '{1}', '{2}', {3}, TO_DATE('{4}','yyyy-mm-dd hh24:mi:ss'))".format(transactionhash, sender, receiver, value, date))
                cursor.execute("INSERT INTO ethereum_data VALUES ('{0}', '{1}', '{2}', {3}, TO_DATE('{4}','yyyy-mm-dd hh24:mi:ss'))".format(transactionhash, sender, receiver, value, date))
                #cursor.execute('insert into ethereum_data values(%s, %s, %s, %d, %s)', (transactionhash, sender, receiver, value, date))
                #cursor.execute("INSERT INTO ethereum_data (TRANSACTIONHASH, SENDER, RECEIVER, VALUE, TRANSACTIONTIME) VALUES ('saas','salim','tirit',12,'12-sep-2020')")
                # commit work
                connection.commit()
    except cx_Oracle.Error as error:
        print('Error occurred:')
        print(error)


def select(tablename):
    sql = ('select * from ethereum_data')

    try:
        with cx_Oracle.connect(user = cfg.username,
                        password = cfg.password,
                        dsn = "localhost:1521/XEPDB1",
                        mode = cx_Oracle.SYSDBA) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
    except:
        print('error')


if __name__ == '__main__':
    #select('ethereum_data')

    transactionFile = open('ether_trans12930000pickle','rb')
    transaction = pickle.load(transactionFile)
    transactionFile.close()

    timeFile = open('timeStamps12930000pickle','rb')
    time = pickle.load(timeFile)
    timeFile.close()

    begin = datetime.now()
    for i in range(70000,71000):
        insert_billing(dict(transaction[i])['hash'].hex(),dict(transaction[i])['from'],dict(transaction[i])['to'],dict(transaction[i])['value'],datetime.fromtimestamp(time[i]).strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.now()-begin)
   
    #insert_billing("son", "kerem", "talha", 222, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))





#dict(ether[0])['hash'].hex() #transaction hash (str)
#dict(ether[0])['from'] #from (str)
#dict(ether[0])['to']  #to (str)
#dict(ether[0])['value'] #value (int)   
