import discord
import asyncio

async def start_bot(token):
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user} with token: {token}')

    await client.start(token, bot=False)

with open('tokens.txt', 'r') as file:
    tokens = file.read().splitlines()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*[start_bot(token) for token in tokens]))
loop.run_forever()
