import discord
from discord.ext import commands 

TOKEN = ''
RESPONSE = 'Why not put those Beans on Toast https://tenor.com/view/beans-on-toast-beans-on-toast-bean-gif-21264075'



if __name__ == '__main__':
    
    intents = discord.Intents.default()        
    intents.message_content = True
    client = discord.Client(intents=intents) 


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    @client.event
    async def on_message(message):
            if message.author == client.user:
                 return
                 
            if 'beans' in message.content:
                 print('beans')
                 await message.channel.send(RESPONSE)
            if 'Beans' in message.content:
                 print('Beans')    
                 await message.channel.send(RESPONSE)
            if 'BEANS' in message.content:
                 print('BEANS')
                 await message.channel.send(RESPONSE) 
             if 'bean' in message.content:
                 print('beans')
                 await message.channel.send(RESPONSE)
            if 'Bean' in message.content:
                 print('Beans')    
                 await message.channel.send(RESPONSE)
            if 'BEAN' in message.content:
                 print('BEANS')
                 await message.channel.send(RESPONSE) 
    client.run(TOKEN)





