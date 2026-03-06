from fastapi import FastAPI
from .services.wallet_service import create_eth_wallet, create_sol_wallet
from .services.portfolio_service import get_portfolio
from .services.gas_service import estimate_gas

app = FastAPI()

wallets = {}

@app.post("/auth/telegram")
def telegram_login(user_id:str):

    if user_id not in wallets:

        wallets[user_id] = {
            "eth": create_eth_wallet(),
            "sol": create_sol_wallet()
        }

    return wallets[user_id]


@app.get("/wallet/{user_id}")
def wallet(user_id:str):
    return wallets.get(user_id)


@app.get("/portfolio/{user_id}")
async def portfolio(user_id:str):
    return await get_portfolio(wallets.get(user_id))


@app.get("/gas")
def gas():
    return estimate_gas()