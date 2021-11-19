import psycopg2
import config

pass = config.password

conn = psycopg2.connect(f"host='localhost' port='5432' dbname='postgres' user='postgres' password='{pass}'")

cur = conn.cursor()

for i in range(11400000,11500000,10000):
    print(i)
    cur.execute("""copy ether_data(blocknumber,transactionindex,transactionhash, sender, receiver, value, transaction_time) from 'D:\\eth\\{}.csv' delimiter ',' csv header;""".format(i))
    conn.commit()

conn.close()