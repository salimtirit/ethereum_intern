select * from ethereum_data;

--for every address
--          flag                            ??
--          avg min sent
--          avg min received
--          time between first and last
--          n of sent transactions
--          n of received transactions
--          n of created contracts          ??
--          unique sent addresses
--          unique received addresses
--          min value sent
--          max value sent
--          avg value sent
--          min value received
--          max value received
--          avg value received
--          min value sent to contract      ??
--          max value sent to contract      ??
--          avg value sent to contract      ??
--          total transactions (including_tnx_to_create_contract)       ??
--          total ether sent
--          total ether received
--          total ether sent to contracts   ??
--          total ether balance             ??

select distinct sender from ethereum_data; -- list of different sender
select distinct receiver from ethereum_data; -- list of different receiver

select * from ethereum_data where (sender="ourguy" and not receiver="ourguy" )or (receiver="ourguy" and not sender="ourguy") or (receiver="ourguy" and sender="ourguy")



select transactionhash,sender, count(*)
from ethereum_data
group by transactionhash, sender
having count(*)>1;

create table new_table as 
SELECT DISTINCT * from ethereum_data;