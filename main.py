import discord
from discord.ext import commands
from discord.ext import tasks


intents = discord.Intents.default()
intents.members = True



client = commands.Bot(command_prefix = "_", intents=intents, help_command=None)


@client.event
async def on_ready():
    print('Bot is ready')
    change_status.start()


@tasks.loop(seconds=10)
async def change_status():
    status = ["felis i lubyu"]
    await client.change_presence(activity=discord.Game(choice(status)))
    
    
    
    
    
initial_extensions=[
            '',

]

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)








client.run("TOKEN")

