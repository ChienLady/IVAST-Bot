from tkinter import *
from tkinter import messagebox
import os, sys
from PIL import Image, ImageTk, ImageDraw
from threading import Thread
import main
from tkinterweb import HtmlFrame

BLACK = '#000000'
WHITE = '#FFFFFF'

class WEB:
	def __init__(self, master, url):
		self.master = master
		self.canvas = Canvas(self.master, height = 600, width = 1024)
		self.canvas.pack()

		self.bg_img = ImageTk.PhotoImage(file = os.path.join('Assets', os.path.join('Web', 'background.png')))
		self.bg_render = self.canvas.create_image((0, 0), image = self.bg_img, anchor = N + W)

		self.return_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Web'), 'return1.png'))
		self.return_btn = Button(self.master, image = self.return_img, text = ' Return ',
			command = self.return_root, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00', compound = LEFT)
		self.return_btn_render = self.canvas.create_window((100, 50), window = self.return_btn)

		self.www_founder_img = ImageTk.PhotoImage(file = os.path.join('Assets', os.path.join('Web', 'www-founder1.png')))
		self.www_founder_img_render = self.canvas.create_image((25, 300), image = self.www_founder_img, anchor = N + W)
		self.label_msg_render = self.canvas.create_text((100, 500), text = 'Tim Berners-Lee', font = ('Arial', 12, 'bold'), fill = '#CCCCFF')
		self.label_msg_render = self.canvas.create_text((100, 530), text = 'inventor of', font = ('Arial', 11, 'bold'), fill = '#CCCCFF')
		self.label_msg_render = self.canvas.create_text((100, 550), text = 'World Wide Web', font = ('Arial', 11, 'bold'), fill = '#CCCCFF')

		self.frame = HtmlFrame(self.master, horizontal_scrollbar = 'auto')
		self.frame.load_website(url)
		self.frame_render = self.canvas.create_window((200, 0), window = self.frame, anchor = N + W)

	def return_root(self):
		self.canvas.destroy()
		self.another = main.main_window(self.master)

