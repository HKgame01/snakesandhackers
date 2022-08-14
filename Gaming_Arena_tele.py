import cohere
import telebot

API_KEY = "5328666176:AAHwVXAevVBWdHzdvOYYn4wZSb5Exc6U1bU"

bot = telebot.TeleBot(API_KEY)
print("Bot is running!")
@bot.message_handler(commands=['start'])
def greet(message):
  bot.send_message(message.chat.id, "Hello, Welcome to the Birthday Helper Bot.Please write /help to see the commands available.")

@bot.message_handler(commands=['help'])
def hello(message):
  bot.send_message(message.chat.id, """Available Commands :-
	`played (game_name)` - to get the recommendation of games from NLP
  `wanna play (game_name)` - to play the game
  /about - This bot is made by Hardik and Henok for Snakes and Hackers 2
	"""
  
  "use  in the (game_name) type the game you haved played to get the recommendation from NLP\nuse  in the (game_name) type the game you wanna play to play it")


@bot.message_handler(commands=['about'])
def greet(message):
  bot.send_message(message.chat.id, "This bot is made by Hardik and Henok for Snakes and Hackers 2")

def game_request(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "played":
    return False
  else:
    return True

@bot.message_handler(func=game_request)
def send_price(message):
	g = message.text.split()[1]
	co = cohere.Client('zgwXd870rQz3cVQyzJqRcQITzKsIR8lx873qlmsZ')

	response = co.generate(
		model='xlarge',
		prompt=f'This program will generate games based on played games.\n--\nPlayed games: billiards\nGames: bagatelle, balkline billiards, baseball, carom billiards, eight ball, golf, pocket billiards.\n--\nPlayed games: Monopoly\nGames: checkers, chess, Chinese chess, go, goose, Monopoly, Nine Men’s Morris\n--\nPlayed games: blackjack\nGames: baccarat, Casino War, Faro, Fan Tan,pai gow poker, poker, red dog, rummy, TexasHold’em poker.\n--\nPlayed games: dice\nGames: Bank Craps, barbooth, chuck-a-luck, crown and anchor, grand hazard, hazard, poker dice\n--\nPlayed games: {g}\nGames: \n',
		max_tokens=100,
		temperature=0.9,
		k=0,
		p=0.75,
		frequency_penalty=0,
		presence_penalty=0,
		stop_sequences=[],
		return_likelihoods='NONE')
	f=str('Here you go: {}'.format(response.generations[0].text))
  
	bot.send_message(message.chat.id, f)

def play_request(message):
  request = message.text.split()
  if len(request) < 3 or request[0].lower() not in "wanna play":
    return False
  else:
    return True

@bot.message_handler(func=play_request)
def send_link(message):
	g = message.text.split()[2]
	if g=="tetris":
		f = "https://tetris.com/play-tetris"
	elif g=="checker":
		f = "https://www.247checkers.com/"
	elif g=="dice":
		f = "https://freeonlinedice.com/"
	else:
		f = f"https://www.google.com/search?q={g} game online"

  
	bot.send_message(message.chat.id, f"Here you go:\n\n Click {f} to play {g}")

bot.polling()
