import telebot
import politics
bot = telebot.TeleBot('1029704857:AAH1zRIwuFqTtXAMX3Hg3LwjXi2gV1pk0Kg')
# bot = telebot.TeleBot('626951912:AAEVZD1dubkRDyzejiCGFx2t_fkLx2C6bRU')
all_links = []
@bot.message_handler(commands=['start'])
def start_message(message):
	with open('politics.csv', 'r') as file:
		count = 0
		number = 1
		for line in file:
			if count % 2 == 0:
				if number == 21:
					break

				res = str(number) + ')' + line
				bot.send_message(message.chat.id, res)
				number += 1

			elif count % 2 == 1:
				all_links.append(line)
			count = count + 1

numbers = [str(x) for x in range(1, 21)]

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text in numbers:
		bot.send_message(message.chat.id, all_links[int(message.text) - 1])


bot.polling()