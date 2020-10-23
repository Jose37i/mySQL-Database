# importing the requests library
import mysql.connector
import json


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="cmsc491bc",
    auth_plugin='mysql_native_password',
    db='bc',
    autocommit=True
)

mycursor = mydb.cursor()
data = {}

mycursor.execute("select * from difficulty")
data['difficulty'] = []

for (date, difficulty_value) in mycursor:
    data['difficulty'].append({
        'date': str(date),
        'difficulty_value': int(difficulty_value)
    })

mycursor.execute("select * from avgtxnumber")
data['avgtxnumber'] = []

for (date2, avgtxnumber_value) in mycursor:
    data['avgtxnumber'].append({
        'date': str(date2),
        'avgtxnumber_value': float(avgtxnumber_value)
    })

mycursor.execute("select * from avgtxnumber")
data['avgtxnumber'] = []

for (date2, avgtxnumber_value) in mycursor:
    data['avgtxnumber'].append({
        'date': str(date2),
        'avgtxnumber_value': float(avgtxnumber_value)
    })

mycursor.execute("select * from avg_tx_size")
data['avg_tx_size'] = []

for (date3, avg_tx_size_value) in mycursor:
    data['avg_tx_size'].append({
        'date': str(date3),
        'avg_tx_size_value': float(avg_tx_size_value)
    })

mycursor.execute("select * from avg_tx_value")
data['avg_tx_value'] = []

for (date3, tx_value) in mycursor:
    data['avg_tx_value'].append({
        'date': str(date3),
        'tx_value': float(tx_value)
    })


mycursor.execute("select * from bcperblock")
data['bcperblock'] = []

for (date3, current_block_reward_value) in mycursor:
    data['bcperblock'].append({
        'date': str(date3),
        'current_block_reward_value': float(current_block_reward_value)
    })


mycursor.execute("select * from block_count")
data['block_count'] = []

for (date3, block_count_value) in mycursor:
    data['block_count'].append({
        'date': str(date3),
        'block_count_value': int(block_count_value)
    })

mycursor.execute("select * from eta")
data['eta'] = []

for (date3, time) in mycursor:
    data['eta'].append({
        'date': str(date3),
        'time': float(time)
    })

mycursor.execute("select * from hashestowin")
data['hashestowin'] = []

for (date3, hash_attempts) in mycursor:
    data['hashestowin'].append({
        'date': str(date3),
        'hash_attempts': int(hash_attempts)
    })


mycursor.execute("select * from bc.interval")
data['interval'] = []

for (date3, interval_val) in mycursor:
    data['interval'].append({
        'date': str(date3),
        'interval_val': float(interval_val)
    })


mycursor.execute("select * from latest_hash")
data['latest_hash'] = []

for (date3, latest_hash_value) in mycursor:
    data['latest_hash'].append({
        'date': str(date3),
        'latest_hash_value': str(latest_hash_value)
    })

mycursor.execute("select * from nextretarget")
data['nextretarget'] = []

for (date3, block_height) in mycursor:
    data['nextretarget'].append({
        'date': str(date3),
        'block_height': int(block_height)
    })


mycursor.execute("select * from probability")
data['probability'] = []

for (date3, probability) in mycursor:
    data['probability'].append({
        'date': str(date3),
        'probability': float(probability)
    })


mycursor.execute("select * from totalbc")
data['totalbc'] = []

for (date3, total) in mycursor:
    data['totalbc'].append({
        'date': str(date3),
        'total': int(total)
    })


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
