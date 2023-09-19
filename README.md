# What is this?

This script reads a dictionary of the form
```
 data = {
    "payee_name": [<transfer_id>,<transfer_id>]
 }
```
And gets the receipts for all the transfers for each payee in the dictionary and exports them to `output/<payeename>`
It also creates `output/<payeename>_receipts.pdf` with all the receipts for each payee
It also creates `output/all_receipts.pdf` which is a join of all the merges of the receipts

# Install

- Install virtual env if you dont have it
```
    pip3 install virtualenv 
```
- Create a virtual env
```
    virtualenv -p python3 env
```
- Activate virtual env
```
    source env/bin/activate
```
- Install dependencies
```
    pip3 install -r requirements.txt
```
- Setup the api key in `runme.py`
- Setup the data {} object in `runme.py`
- Run the script
```
    python3 runme.py
```


# Author:
Marny lopez
www.marnylopez.com