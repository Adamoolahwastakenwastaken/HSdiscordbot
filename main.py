import discord
from random import *

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        cool_jokes = ["why was 6 afraid of 7 ... because 7 8 9", "what kind of tea is hard to swallow? ... REALITY", "why did the cookie go to the doctor?... cuz it felt crumby *Cymbal plays*", "How do celebreties keep cool?.. They have many fans", "The secret of wheight loss was cracked but a secret is a secret", "A dog went to the post office and wanted to write a letter so an employee said : (Alright Dictate me so i will write) so the dog said : (woof woof woof bark bark bark bark woof woof bark) you wrote 9 words so you have one more word free the post office employee said (But that doesnt make sense) the dog said"]
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'what can you do?':
            await message.channel.send('Hi, Im the High Standards chat bot designed to help you!, I can do many things such as : Tell a joke, Help you contact the High Standards team and much more if you want a full list of commands message : Commands if you have any suggestions visit : https://github.com/Adamoolahwastakenwastaken/HSdiscordbot and leave an issue or as an alternate solution Message : Adamoolah#4563')
        if message.content == 'tell me a joke':
            await message.channel.send(cool_jokes[randint(0,6)])  
        if message.content == 'What is High Standards Whatsapp Number':
            await message.channel.send("Here is the whatsapp number : +9710558861666 dont spam this number, send your message and wait 1-2 days")
        if message.content == 'What is High Standards phone Number':
            await message.channel.send("Here is the phone number : +9710509129777 dont spam this number, send your message and wait 1-2 days")
            
        if message.content == 'Commands':
            await message.channel.send("tell me a joke : Sends a randomly generated joke")
            await message.channel.send("What is High Standards Whatsapp Number : Sends High Standards' whatsapp number")
            await message.channel.send("What is High Standards phone Number : Sends High Standards' phone number")
            await message.channel.send("Show me the source code : Sends the source code for this bot")
            await message.channel.send("I wanna know more about the developer : tells you abt me lmao") 

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA3MDk1NDYzNDk1ODYxMDQ2Mg.GLM7r0.XORnSk5kuZcV2-2ITpPwPFpZf6nKNAXeChUHC4')