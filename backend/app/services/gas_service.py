from web3 import Web3
import os

RPC=os.getenv("ETH_RPC","https://eth.llamarpc.com")

w3=Web3(Web3.HTTPProvider(RPC))

def estimate_gas():

    try:
        gas=w3.eth.gas_price
        return {"gwei": w3.fromWei(gas,"gwei")}
    except:
        return {"gwei":"unavailable"}