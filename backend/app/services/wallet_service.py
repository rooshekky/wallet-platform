from web3 import Web3
from solana.keypair import Keypair
import base64

def create_eth_wallet():
    acct = Web3().eth.account.create()
    return {
        "address": acct.address,
        "private_key": acct.key.hex()
    }

def create_sol_wallet():
    kp = Keypair()
    return {
        "address": str(kp.public_key),
        "private_key": base64.b64encode(bytes(kp.secret_key)).decode()
    }