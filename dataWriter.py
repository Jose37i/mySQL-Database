# importing the requests library
import requests
import mysql.connector
from datetime import datetime

date = str(datetime.today().strftime('%Y-%m-%d'))


def run_insert(passed_db_connection, passed_api_endpoint, passed_table):
    # sending get request and saving the response as response object
    r = requests.get(url=passed_api_endpoint)

    if passed_table == "latest_hash" or passed_table == "probability":
        data = r.text
        data = "\'" + str(data) + "\'"

    # extracting data in json format
    else:
        data = r.json()

    print(data)

    passed_db_connection.execute("insert into " + passed_table + " values (\'" + date + "\', " + str(data) + ")")


# api-endpoint
# Current difficulty target as a decimal number
# date:
#
get_difficulty_call = "https://blockchain.info/q/getdifficulty"

# Current block height in the longest chain
get_block_count = "https://blockchain.info/q/getblockcount"

# Hash of the latest block
get_latest_hash = "https://blockchain.info/q/latesthash"

# Current block reward in BTC
get_bc_reward_in_bc = "https://blockchain.info/q/bcperblock"

# Total Bitcoins in circulation (delayed by up to 1 hour])
get_total_bc_in_circulation = "https://blockchain.info/q/totalbc"

#  Probability of finding a valid block each hash attempt
get_probability_hash_attempt = "https://blockchain.info/q/probability"

# Average number of hash attempts needed to solve a block
get_average_hash_attempts = "https://blockchain.info/q/hashestowin"

# Block height of the next difficulty retarget
get_block_next_difficulty_target = "https://blockchain.info/q/nextretarget"

# Average transaction size for the past 1000 blocks. Change the number of blocks by passing an integer as
# the second argument e.g. avgtxsize/2000
get_avg_tx_size = "https://blockchain.info/q/avgtxsize"

#  Average transaction value (1000 Default)
get_avg_tx_value = "https://blockchain.info/q/avgtxvalue"

# average time between blocks in seconds
get_average_interval = "https://blockchain.info/q/interval"

# estimated time until the next block (in seconds)
get_avg_eta_next_block = "https://blockchain.info/q/eta"

# Average number of transactions per block (100 Default)
get_avg_tx_in_block = "https://blockchain.info/q/avgtxnumber"

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="cmsc491bc",
    auth_plugin='mysql_native_password',
    db='bc',
    autocommit=True
)

mycursor = mydb.cursor()

run_insert(mycursor, get_difficulty_call, "difficulty")

run_insert(mycursor, get_block_count, "block_count")

run_insert(mycursor, get_latest_hash, "latest_hash")

run_insert(mycursor, get_bc_reward_in_bc, "bcperblock")

run_insert(mycursor, get_total_bc_in_circulation, "totalbc")

run_insert(mycursor, get_probability_hash_attempt, "probability")

run_insert(mycursor, get_average_hash_attempts, "hashestowin")

run_insert(mycursor, get_block_next_difficulty_target, "nextretarget")

run_insert(mycursor, get_avg_tx_size, "avg_tx_size")

run_insert(mycursor, get_avg_tx_value, "avg_tx_value")

run_insert(mycursor, get_average_interval, "bc.interval")

run_insert(mycursor, get_avg_eta_next_block, "eta")

run_insert(mycursor, get_avg_tx_in_block, "avgtxnumber")
