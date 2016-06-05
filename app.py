import discord
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def getToken():
	f = open('DiscordToken.txt', 'r')
	text = f.read()
	print(text)
	f.close()
	return text

client = discord.Client()

#server = client.servers[0]
#channels = server.channels

#token = ''

server = None

@client.event
async def on_ready():
	print ('Logged in as')
	print (client.user.name)
	print (client.user.id)
	print ('--------')
	print (client.servers)
	await client.change_status(game = discord.Game(name = "I can't code", url = '', type = 0), idle = False)
	#print (channels)
	#print (discord.inviteURL)


@client.event
async def on_message(message):
	if message.content.startswith('!test'):
		print (message.channel.id)
		await client.send_message(message.channel, "Hello world!")
	if message.content.startswith('!joinme'):
		if message.author.voice_channel != None:
			await client.join_voice_channel(message.author.voice_channel)
			server = message.server
	if message.content.startswith('!leave'):
		print ("Is server none")
		print (server != None)
		print ("--------------")
		if server != None:
			if client.is_voice_connected(server):
				await client.disconnect()
			server = None
	if message.content.startswith('!changegame'):
		print (message.content[12:])
		await client.change_status(game = discord.Game(name = message.content[12:], url = '', type = 0), idle = False)
	if message.content.startswith('!setnickname'):
		await client.change_nickname(message.author, message.content[13:])

@client.event
async def on_error(error):
	print ("##################")
	print ("##ERROR RECIEVED##")
	print ("##################")
	print (error)
	print ("##################")
	print ("####ERROR END#####")
	print ("##################")

def main():
	token = getToken()
	client.run(token)


main()