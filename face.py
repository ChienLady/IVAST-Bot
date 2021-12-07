from tkinter import *
from tkinter import messagebox
import os, sys
from PIL import Image, ImageTk, ImageDraw
from threading import Thread
import main

BLACK = '#000000'
WHITE = '#FFFFFF'

class FACE:
	def __init__(self, master):
		self.master = master
		self.canvas = Canvas(self.master, height = 600, width = 1024)
		self.canvas.pack()

		self.bg_img = ImageTk.PhotoImage(file = os.path.join('Assets', os.path.join('Face', 'background.png')))
		self.bg_render = self.canvas.create_image((0, 0), image = self.bg_img, anchor = N + W)
		
		self.label_msg_render = self.canvas.create_text((520, 50), text = 'IVAST Bot - Face Recognition', font = ('Transformers Movie', 40), fill = '#CCCCFF')

		self.a = Image.open(os.path.join(os.path.join('Assets', 'Walk'), 'return.png'))
		self.a = self.a.resize((int(self.a.size[0] / 12), int(self.a.size[1] / 12)), Image.ANTIALIAS)
		self.a.save(os.path.join(os.path.join(os.path.join('Assets', 'Walk'), 'return1.png')))
		self.return_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Walk'), 'return1.png'))
		self.return_btn = Button(self.master, image = self.return_img, text = ' Return ',
			command = self.return_root, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00', compound = LEFT)
		self.return_btn_render = self.canvas.create_window((100, 50), window = self.return_btn)

	def return_root(self):
		self.canvas.destroy()
		self.another = main.main_window(self.master)

