import openai
import asyncio
import discord
from discord import app_commands
from discord.ext import commands


openai.api_key = "key here"
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@client.tree.command(name="prompt")
@app_commands.describe(the_prompt = "What do you want from me?")
async def respPrompt(interaction: discord.Interaction, the_prompt: str):
    await interaction.response.send_message("Working on it...")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": the_prompt},
        ],
        temperature=0,
    )
    await interaction.edit_original_response(content=response['choices'][0]['message']['content'])
    #await interaction.response.edit_original_response()


client.run('discord bot token')
