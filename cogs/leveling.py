import discord, json
from discord.ext import commands


class leveling(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.id == 760415780176658442:
			print("yes")
			return
		with open('./Data/levels.json', 'r', encoding='utf8') as f:
			user = json.load(f)
		
		if str(message.guild.id) not in user:
			user[str(message.guild.id)] = {}

		if str(message.author.id) not in user[str(message.guild.id)] :
			user[str(message.guild.id)][str(message.author.id)] = {}
			user[str(message.guild.id)][str(message.author.id)]['level'] = 0
			user[str(message.guild.id)][str(message.author.id)]['exp'] = 0

			with open('./Data/levels.json', 'w', encoding='utf8') as f:
				json.dump(user, f,indent=5)
			return
		
		user[str(message.guild.id)][str(message.author.id)]['exp'] += 1
		exp = user[str(message.guild.id)][str(message.author.id)]['exp']
		lvl = user[str(message.guild.id)][str(message.author.id)]['level']  + 1
		exps=[60]
		if lvl == 696969696969696969696970:
			return
		while lvl > len(exps):
			exps.append(int(exps[-1] + exps[-1]/10))
			if lvl == len(exps):
				break
		lvl_end = exps[-1]
		with open('./Data/levels.json', 'w', encoding='utf8') as f:
				json.dump(user, f,indent=5)
		if lvl_end <= exp:
			user[str(message.guild.id)][str(message.author.id)]['exp'] = 1
			user[str(message.guild.id)][str(message.author.id)]['level'] +=1
			lvl = user[str(message.guild.id)][str(message.author.id)]['level']
			with open('./Data/levels.json', 'w', encoding='utf8') as f:
				json.dump(user, f,indent=5)
			chanel = message.channel
			await chanel.send(f'Oh,{message.author.mention} has leveled up to {lvl}')
			return
	
def setup(client):
	client.add_cog(leveling(client))
