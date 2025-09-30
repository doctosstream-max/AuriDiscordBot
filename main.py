import os
import discord
import openai

# Definimos los intents obligatorios para discord.py 2.x
intents = discord.Intents.default()
intents.message_content = True  # permite leer el contenido de los mensajes

# Creamos el client con los intents
client = discord.Client(intents=intents)

# Configuramos la API key de OpenAI desde variables de entorno
openai.api_key = os.environ['OPENAI_API_KEY']

@client.event
async def on_message(message):
    # Ignorar mensajes del propio bot
    if message.author == client.user:
        return

    # Revisar que sea el canal correcto
    if message.channel.name == "auri-chat":
        respuesta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.content}]
        )
        await message.channel.send(respuesta['choices'][0]['message']['content'])

# Ejecutar el bot con el token de Discord desde variables de entorno
client.run(os.environ['DISCORD_TOKEN'])
