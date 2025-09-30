import os
import discord
import openai

client = discord.Client()
openai.api_key = os.environ['OPENAI_API_KEY']

@client.event
async def on_message(message):
    if message.author == client.user: 
        return
    if message.channel.name == "auri-chat":
        respuesta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.content}]
        )
        await message.channel.send(respuesta['choices'][0]['message']['content'])

client.run(os.environ['DISCORD_TOKEN'])
