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

def getOwnerID():
	f = open('OwnerID.txt', 'r')
	text = f.read()
	f.close()
	return text

client = discord.Client()

#server = client.servers[0]
#channels = server.channels

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
	msg = None
	deleteMessage = False
	if message.content.startswith('!test'):
		msg = message
		print (message.channel.id)
		print (message.author.id)
		await client.send_message(message.channel, "Hello world!")
		deleteMessage = True
	if message.content.startswith('!joinme'):
		msg = message
		if message.author.voice_channel != None:
			await client.join_voice_channel(message.author.voice_channel)
		deleteMessage = True
	if message.content.startswith('!leave'):
		msg = message
		await client.disconnect()
		deleteMessage = True
	if message.content.startswith('!changegame'):
		msg = message
		if (message.author.id == getOwnerID()):
			print ("Changing game to " + message.content[12:])
			await client.change_status(game = discord.Game(name = message.content[12:], url = '', type = 0), idle = False)
		else:
			await client.send_message(message.channel, "You don't have the permission to change my now playing :upside_down:")
		deleteMessage = True
	if message.content.startswith('!setnickname'):
		msg = message
		await client.change_nickname(message.author, message.content[13:])
		deleteMessage = True
	if deleteMessage:
		await client.delete_message(msg)

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