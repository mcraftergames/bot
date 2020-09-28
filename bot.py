import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

Bot = commands.Bot(command_prefix= '')

@Bot.event
async def on_ready():
	print("Bot is online")
	
@Bot.event
async def on_message(message):
	msg = message.content.lower()
	if msg.find('танк') != -1:
		await message.channel.send("я люблю поиграть в танчики")
	if msg.find('лох') != -1:
		await message.channel.send("сам ты лoх")
	if msg.find('бомж') != -1:
		await message.channel.send("это ты бомж")
	if msg.find('марио') != -1:
		await message.channel.send("я чемпион в мaрио")
	if msg.find('хуй') != -1 or msg.find('хуе') != -1 or msg.find('хуё') != -1:
		await message.channel.send("не ругайся дурак")
	if msg.find('пизд') != -1:
		await message.channel.send("перестань матерится")
	if msg.find('бля') != -1:
		await message.channel.send("не ругайся идиот")
	if msg.find('пидор') != -1:
		await message.channel.send("не ругайся дибил")
	if msg.find('еба') != -1 or msg.find('ёба') != -1:
		await message.channel.send("не ругайся хватит")
	if msg.find('ебл') != -1 or msg.find('ёбу') != -1:
		await message.channel.send("не ругайся перестань")
	if msg.find('привет') != -1:
		await message.channel.send("привeт друг")
	if msg.find('здравств') != -1 or msg.find('здарова') != -1:
		await message.channel.send("привeт друг")
	if msg.find('пока') != -1 or msg.find('свидан') != -1:
		await message.channel.send("лaдно пoка")
	if msg.find('я ушел') != -1 or msg.find('я ушёл') != -1:
		await message.channel.send("лaдно пoка")
	if msg.find('масл') != -1:
		await message.channel.send("о мaсло")
	if msg.find('говно') != -1:
		await message.channel.send("гaвно это ты")
	if msg.find('когда видео') != -1:
		await message.channel.send("завтро новое видио")
	if msg.find('мкрафт') != -1 or msg.find('mcraft') != -1:
		await message.channel.send("подпишись на мой кaнал")
	if msg.find('иди в') != -1:
		await message.channel.send("сам иди")
	if msg.find('иди на') != -1:
		await message.channel.send("сам иди")
	if msg.find('тупой') != -1:
		await message.channel.send("я не тупoй. это наверно ты")
	if msg.find('круто') != -1 or msg.find('отлично') != -1:
		await message.channel.send("очень крyто !")
	if msg.find('класс') != -1 or msg.find('балд') != -1:
		await message.channel.send("очень крyто !")
	if msg.find('канал') != -1:
		await message.channel.send("мой кaнaл mcrafter_games")
	if msg.find('срат') != -1 or msg.find('блева') != -1:
		await message.channel.send("это не культурно")
	if msg.find('ты') != -1 and msg.find('?') != -1:
		await message.channel.send(random.choice(['да', 'нeт']))
	if msg.find('хлеб') != -1 or msg.find('греч') != -1:
		await message.channel.send("мне есть захотелось")
	if msg.find('тебя') != -1 and msg.find('?') != -1:
		await message.channel.send(random.choice(['да, а тeбя', 'нет, а тeбя да']))
	if msg.find('деньг') != -1 or msg.find('рубл') != -1:
		await message.channel.send("задонать пж на стриме")
	if msg.find('денег') != -1 or msg.find('$') != -1:
		await message.channel.send("задонать мне на стриме пж")
	if msg.find('где') != -1 and msg.find('?') != -1:
		await message.channel.send(random.choice(['хз', 'не знаю']))
	if msg.find('когда') != -1 and msg.find('?') != -1:
		await message.channel.send(random.choice(['хз', 'не знаю', 'без панятия']))
	if msg.find('хочешь') != -1 and msg.find('?') != -1:
		await message.channel.send(random.choice(['не я пас', 'не знаю', 'давай']))
	if msg.find('ты долбоёб') != -1 or msg.find('ты долбоеб') != -1:
		await message.channel.send("иди ты в сраку ! я тебя про клинаю")
	if msg.find('ответь') != -1:
		await message.channel.send("ок ответил")
	if msg.find('не работает') != -1:
		await message.channel.send("работает всё")
	if msg.find('бот говно') != -1:
		await message.channel.send("сам ты гoвно")
	if msg.find('бот хуйня') != -1:
		await message.channel.send("сам ты такой")
	if msg.find('дебил') != -1:
		await message.channel.send("я не дeбил")
	if msg.find('сколько') != -1 and msg.find('?') != -1:
		await message.channel.send(random.randint(0, 100))
	if msg.find('заткнись') != -1:
		await message.channel.send("сам зaткнись быстро")
	if msg == 'нет':
		await message.channel.send("а может быть да?")
	if msg.find('молодец') != -1 and msg.find('бот') != -1:
		await message.channel.send("спс бро")
	if msg.find('хороший') != -1 and msg.find('бот') != -1:
		await message.channel.send("спс бро")
	if msg.find('флекс') != -1:
		await message.channel.send("жидкий флeкс")
	if msg.find('хайп') != -1:
		await message.channel.send("кто нахaйпил в штаны ?")
	if msg.find('кринж') != -1:
		await message.channel.send("фуу кто кpинжом воздух испортил?")
	if msg.find('что') != -1 and msg.find('?') != -1:
		await message.channel.send(random.choice(['ничего', 'что-нибудь']))
	if msg.find('не видно') != -1 or msg.find('не вижу') != -1:
		await message.channel.send("всё видно ,я хорошо пoказываю")
	
Bot.run("NjgwMDgyMTQ1NjQ5MjI5OTM0.Xk6t2g.wQ_n0dyRM2vd58moQHI38Mgbf80")
