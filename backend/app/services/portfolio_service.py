import httpx

async def get_portfolio(wallet):

    if not wallet:
        return {"error":"wallet not found"}

    async with httpx.AsyncClient() as client:

        eth_price = await client.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        )

        sol_price = await client.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
        )

    return {
        "eth_price": eth_price.json(),
        "sol_price": sol_price.json(),
        "wallet": wallet
    }