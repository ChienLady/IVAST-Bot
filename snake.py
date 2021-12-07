from tkinter import *
from tkinter import messagebox
import os, sys
from PIL import Image, ImageTk, ImageDraw
from threading import Thread
import main
from random import randint

BLACK = '#000000'
WHITE = '#FFFFFF'

MOVE_INCREMENT = 20
MOVES_PER_SECOND = 12
GAME_SPEED = 1000 // MOVES_PER_SECOND

class SNAKE:
	def __init__(self, master):
		self.master = master
		self.canvas = Canvas(self.master, height = 600, width = 1024)
		self.canvas.pack()

		self.bg_img = ImageTk.PhotoImage(file = os.path.join('Assets', os.path.join('Snake', 'background.png')))
		self.bg_render = self.canvas.create_image((0, 0), image = self.bg_img, anchor = N + W)
		
		self.label_msg_render = self.canvas.create_text((520, 50), text = 'IVAST Bot - Snake Game', font = ('Transformers Movie', 40), fill = '#CCCCFF')

		
		self.return_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Snake'), 'return1.png'))
		self.return_btn = Button(self.master, image = self.return_img, text = ' Return ',
			command = self.return_root, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00', compound = LEFT)
		self.return_btn_render = self.canvas.create_window((100, 50), window = self.return_btn)
		self.create_game()

		self.snake_positions = [(100, 100), (80, 100), (60, 100)]
		self.food_position = self.set_new_food_position()
		self.direction = 'Right'
		self.score = 0

		self.load_assets()
		self.create_objects()
		self.frame.bind_all('<Key>', self.on_key_press)
		self.frame.after(GAME_SPEED, self.perform_actions)
	
	def load_assets(self):
		try:
			self.snake_body_img = Image.open(os.path.join(os.path.join('Assets', 'Snake'), 'snake.png'))
			self.snake_body = ImageTk.PhotoImage(self.snake_body_img)
			self.food_img = Image.open(os.path.join(os.path.join('Assets', 'Snake'), 'food.png'))
			self.food = ImageTk.PhotoImage(self.food_img)
		except IOError as error:
			self.frame.destroy()
			raise
	
	def create_objects(self):
		self.frame.create_text(35, 12, text = f'Score: {self.score}', tag = 'score', fill = '#fff', font = 10)

		for x_position, y_position in self.snake_positions:
			self.frame.create_image(x_position, y_position, image = self.snake_body, tag = 'snake')

		self.frame.create_image(*self.food_position, image = self.food, tag = 'food')
		self.frame.create_rectangle(7, 27, 593, 613, outline = '#525d69')

	def check_collisions(self):
		head_x_position, head_y_position = self.snake_positions[0]

		return (
			head_x_position in (0, 500)
			or head_y_position in (20, 520)
			or (head_x_position, head_y_position) in self.snake_positions[1:]
		)

	def check_food_collision(self):
		if self.snake_positions[0] == self.food_position:
			self.score += 1
			self.snake_positions.append(self.snake_positions[-1])

			self.frame.create_image(*self.snake_positions[-1], image = self.snake_body, tag = 'snake')
			self.food_position = self.set_new_food_position()
			self.frame.coords(self.frame.find_withtag('food'), *self.food_position)

			score = self.frame.find_withtag('score')
			self.frame.itemconfigure(score, text = f'Score: {self.score}', tag = 'score')

	def end_game(self):
		self.frame.delete(ALL)
		self.frame.create_text(self.frame.winfo_width() / 2, self.frame.winfo_height() / 2,
			text = f'Game over! You scored {self.score}!', fill = '#fff', font = 14)

	def move_snake(self):
		head_x_position, head_y_position = self.snake_positions[0]

		if self.direction == 'Left':
			new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position)
		elif self.direction == 'Right':
			new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)
		elif self.direction == 'Down':
			new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
		elif self.direction == 'Up':
			new_head_position = (head_x_position, head_y_position - MOVE_INCREMENT)

		self.snake_positions = [new_head_position] + self.snake_positions[:-1]

		for segment, position in zip(self.frame.find_withtag('snake'), self.snake_positions):
			self.frame.coords(segment, position)

	def on_key_press(self, e):
		new_direction = e.keysym

		all_directions = ('Up', 'Down', 'Left', 'Right')
		opposites = ({'Up', 'Down'}, {'Left', 'Right'})

		if (
			new_direction in all_directions
			and {new_direction, self.direction} not in opposites
		):
			self.direction = new_direction

	def perform_actions(self):
		if self.check_collisions():
			self.end_game()

		self.check_food_collision()
		self.move_snake()

		self.frame.after(GAME_SPEED, self.perform_actions)

	def set_new_food_position(self):
		while True:
			x_position = randint(1, 24) * MOVE_INCREMENT
			y_position = randint(3, 25) * MOVE_INCREMENT
			food_position = (x_position, y_position)

			if food_position not in self.snake_positions:
				return food_position

	def create_game(self):
		self.frame = Canvas(self.canvas, height = 500, width = 500, background = BLACK)
		self.frame_render = self.canvas.create_window((90, 90), window = self.frame, anchor = N + W)

		# self.a = Image.open(os.path.join(os.path.join('Assets', 'Snake'), 'snake_control.png'))
		# self.a = self.a.resize((int(self.a.size[0] / 6), int(self.a.size[1] / 6)), Image.ANTIALIAS)
		# self.a.save(os.path.join(os.path.join(os.path.join('Assets', 'Snake'), 'snake_control1.png')))
		self.up_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Snake'), 'up1.png'))
		self.up_btn = Button(self.master, image = self.up_img,
			command = self.up, background = '#CCCCFF', activebackground = '#FFBF00')
		self.up_btn_render = self.canvas.create_window((800, 230), window = self.up_btn)

		self.down_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Snake'), 'down1.png'))
		self.down_btn = Button(self.master, image = self.down_img,
			command = self.down, background = '#CCCCFF', activebackground = '#FFBF00')
		self.down_btn_render = self.canvas.create_window((800, 420), window = self.down_btn)

		self.right_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Snake'), 'right1.png'))
		self.right_btn = Button(self.master, image = self.right_img,
			command = self.right, background = '#CCCCFF', activebackground = '#FFBF00')
		self.right_btn_render = self.canvas.create_window((890, 325), window = self.right_btn)

		self.left_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Snake'), 'left1.png'))
		self.left_btn = Button(self.master, image = self.left_img,
			command = self.left, background = '#CCCCFF', activebackground = '#FFBF00')
		self.left_btn_render = self.canvas.create_window((710, 325), window = self.left_btn)

		self.snake_control_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Snake'), 'snake_control1.png'))
		self.snake_control_img_render = self.canvas.create_image((800, 325), image = self.snake_control_img)

	def up(self):
		self.direction = 'Up'
	def down(self):
		self.direction = 'Down'	
	def left(self):
		self.direction = 'Left'
	def right(self):
		self.direction = 'Right'
		

	def return_root(self):
		self.canvas.destroy()
		self.another = main.main_window(self.master)

