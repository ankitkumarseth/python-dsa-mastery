# Transfer amount

Write a function `transfer_amount(accounts:dict, sender:str, recipient:str, amount:int)` that takes a dictionary of accounts with account numbers as keys and their respective balances as values, the account number of the sender, the recipient's account number, and the transfer amount if the transfer is valid else no transfer should happen and the dictionary is not modified.

A transanction is valid if:
- both sender and recipient account numbers are present in accounts dictionary.
- the sender's account has sufficient balance
- the amount is non negative

Note that this function does not return anything just modifies the accounts dictionary. In case of invalid transfer dictionary is not updated.

### Examples
```python
>>> accounts = {'12345': 500, '67890': 1000, '98764': 1500}

>>> transfer_amount(accounts, '12345', '67890', 1000)
>>> accounts # no change as 12345 has less than 1000
{'12345': 500, '67890': 1000, '98764': 1500}

>>> transfer_amount(accounts, '12345', '67890', 400)
>>> accounts # 400 transfered from 12345 to 67890
{'12345': 100, '67890': 1400, '98764': 1500}

>>> transfer_amount(accounts, '98764', '67890', 1500)
>>> accounts # 1500 transfered from 98764 to 67890
{'12345': 100, '67890': 2900, '98764': 0}

>>> transfer_amount(accounts, '98764', '67890', -100)
>>> accounts # no change as the amount is negative
{'12345': 100, '67890': 2900, '98764': 0}

>>> transfer_amount(accounts, '29732', '67890', 100)
>>> accounts # no change as 29732 is not present in accounts
{'12345': 100, '67890': 2900, '98764': 0}
```
