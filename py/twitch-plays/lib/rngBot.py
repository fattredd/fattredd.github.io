import time
from random import choice

from config.config import config
from lib.game import Game
from lib.misc import pbutton

class Bot:

	def __init__(self):
		self.config = config
		self.game = Game()
		self.message_buffer = [{'button': ''}] * self.config['misc']['chat_height']

	def set_message_buffer(self, message):
		self.message_buffer.insert(self.config['misc']['chat_height'] - 1, message)
		self.message_buffer.pop(0)

	def run(self):
		throttle_timers = {button:0 for button in config['throttled_buttons'].keys()}

		while True:
			button = choice(self.game.keymap)
			if button in self.config['throttled_buttons']:
				if time.time() - throttle_timers[button] < self.config['throttled_buttons'][button]:
					continue
				throttle_timers[button] = time.time()

			self.set_message_buffer({'username': username, 'button': button})
			pbutton(self.message_buffer)
			self.game.push_button(button)