import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "*", description = "AidenQuiz")

@bot.event
async def on_ready():
	print("Le bot à démarré avec succès !")

@bot.command()
async def quiz1(ctx):
	await ctx.send("Bienvenue dans le quiz 1 !")

	def check(message):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Le quizz n°1 va commencer. Veuillez valider en réagissant avec :white_check_mark: . Sinon réagissez avec :no_entry_sign: .")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Le quiz démarre... A vos cervelles de moineaux !")
		await ctx.send("Il s'agit tout simplement d'un vrai ou faux !")
		await ctx.send("Commence le quiz avec la commande *question1 !")

	else:
		await ctx.send("Pauvre ignorant... Tu ne sais pas ce que tu rate...")

@bot.command()
async def question1(ctx):

	def check(question1):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question2")

	else:
		await ctx.send("Pauvre ignorant... Tu ne sais même pas grâce à qui tu pourra jouer prochaînement...")
		await ctx.send("Ici ta réponse")

@bot.command()
async def question2(ctx):

	def check(question2):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question3")

	else:
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question3")

@bot.command()
async def question3(ctx):

	def check(question3):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question4")

	else:
		await ctx.send("Et bien si, en aôut 2000 plus exactement ! ;)")
		await ctx.send("Ici ta réponse")

@bot.command()
async def question4(ctx):

	def check(question4):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question5")

	else:
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question5")

@bot.command()
async def question5(ctx):

	def check(question5):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question6")

	else:
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question6")

@bot.command()
async def question6(ctx):

	def check(question6):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question7")

	else:
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question7")

@bot.command()
async def question7(ctx):

	def check(question7):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question8")

	else:
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question8")

@bot.command()
async def question8(ctx):

	def check(question8):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question9")

	else:
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question9")

@bot.command()
async def question9(ctx):

	def check(question9):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Merci de croire en nous!")
		await ctx.send("Ici ta réponse")

	else:
		await ctx.send("Ici ta réponse")
		await ctx.send("Passe désormais à la question suivante avec *question10")

@bot.command()
async def question10(ctx):

	def check(question10):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	
	message = await ctx.send(f"Ici ta question")
	
	await message.add_reaction("✅")
	
	await message.add_reaction("⛔")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "⛔")


	reaction, user = await bot.wait_for("reaction_add", check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("Ici ta réponse")
		await ctx.send("Merci d'avoir participé, un nouveau quiz sort la semaine prochaine !")

	else:
		await ctx.send("Ici ta réponse")
		await ctx.send("Merci d'avoir participé, un nouveau quiz sort la semaine prochaine !")




bot.run("Ici le token de ton bot")