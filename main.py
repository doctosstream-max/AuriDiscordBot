from openai import OpenAI
import os
import discord

client = discord.Client(intents=discord.Intents.default())
openai_client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.name == "auri-chat":
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.content}]
        )
        await message.channel.send(response.choices[0].message.content)

client.run(os.environ['DISCORD_TOKEN'])
