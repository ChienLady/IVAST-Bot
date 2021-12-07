from tkinter import *
from tkinter import messagebox
import os, sys
from PIL import Image, ImageTk, ImageDraw
from threading import Thread
import main

BLACK = '#000000'
WHITE = '#FFFFFF'

def crop_to_circle(img):
	bigsize = (img.size[0] * 3, img.size[1] * 3)
	mask = Image.new('L', bigsize, 0)
	draw = ImageDraw.Draw(mask) 
	draw.ellipse((0, 0) + bigsize, fill = 255)
	mask = mask.resize(img.size, Image.ANTIALIAS)
	img.putalpha(mask)
	return img

class ABOUTUS:
	def __init__(self, master):
		self.master = master
		self.canvas = Canvas(self.master, height = 600, width = 1024)
		self.canvas.pack()

		self.bg_img = ImageTk.PhotoImage(file = os.path.join('Assets', os.path.join('Aboutus', 'background.png')))
		self.bg_render = self.canvas.create_image((0, 0), image = self.bg_img, anchor = N + W)
		
		self.label_msg_render = self.canvas.create_text((520, 50), text = 'IVAST Bot - About us', font = ('Transformers Movie', 40), fill = '#CCCCFF')

		self.return_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Aboutus'), 'return1.png'))
		self.return_btn = Button(self.master, image = self.return_img, text = ' Return ',
			command = self.return_root, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00', compound = LEFT)
		self.return_btn_render = self.canvas.create_window((100, 50), window = self.return_btn)

		self.frame = Canvas(self.canvas, height = 470, width = 836, background = '#808080')
		self.frame_render = self.canvas.create_window((90, 100), window = self.frame, anchor = N + W)
		self.frame_render_render1 = self.frame.create_text((10, 10), text = 'IVAST Bot là một dự án xây dựng robot hình người của viện Hàn lâm Khoa học và Công nghệ Việt Nam',
			font = ('Arial', 12, 'bold'), fill = WHITE, anchor = N + W)
		self.frame_render_render1 = self.frame.create_text((10, 40), text = 'Dự án được phát triển bởi TS. Ngô Mạnh Tiến - Trưởng phòng Tự động hóa của Viện Vật lý và các ',
			font = ('Arial', 12, 'bold'), fill = WHITE, anchor = N + W)
		self.frame_render_render1 = self.frame.create_text((10, 60), text = 'nghiên cứu sinh thuộc nhóm nghiên cứu của tiến sĩ',
			font = ('Arial', 12, 'bold'), fill = WHITE, anchor = N + W)
		
		self.frame_render_render1 = self.frame.create_text((180, 420), text = 'Hình ảnh TS. Ngô Mạnh Tiến cùng những nghiên cứu sinh',
			font = ('Arial', 12, 'bold'), fill = WHITE, anchor = N + W)
		
		self.tt_img_dir = os.path.join(os.path.join('Assets', 'Aboutus'), 'Images')
		self.tt_imgs = os.listdir(self.tt_img_dir)
		self.left_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Aboutus'), 'left1.png'))
		self.left_btn = Button(self.master, image = self.left_img, command = self.previous,
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.left_btn_render = self.frame.create_window((100, 250), window = self.left_btn)

		self.right_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Aboutus'), 'right1.png'))
		self.right_btn = Button(self.master, image = self.right_img, command = self.next,
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.right_btn_render = self.frame.create_window((720, 250), window = self.right_btn)
		self.create_image()

	def create_image(self):
		self.i = 0
		fn = os.path.join(self.tt_img_dir, self.tt_imgs[self.i])
		# IMAGE SIZE = 451x280
		self.tt_img = ImageTk.PhotoImage(file = fn)
		self.panel = Label(self.master, image = self.tt_img)
		self.tt_img_render = self.frame.create_window((180, 110), window = self.panel, anchor = N + W)
		if self.i == 0:
			self.left_btn.configure(state = 'disable')
			self.right_btn.configure(state = 'normal')
		elif self.i == len(self.tt_imgs) - 1:
			self.left_btn.configure(state = 'normal')
			self.right_btn.configure(state = 'disable')
		else:
			self.left_btn.configure(state = 'normal')
			self.right_btn.configure(state = 'normal')
	
	def next(self):
		self.i += 1
		fn = os.path.join(self.tt_img_dir, self.tt_imgs[self.i])
		self.tt_img = ImageTk.PhotoImage(file = fn)
		self.panel.configure(image = self.tt_img)
		if self.i == 0:
			self.left_btn.configure(state = 'disable')
			self.right_btn.configure(state = 'normal')
		elif self.i == len(self.tt_imgs) - 1:
			self.left_btn.configure(state = 'normal')
			self.right_btn.configure(state = 'disable')
		else:
			self.left_btn.configure(state = 'normal')
			self.right_btn.configure(state = 'normal')

	def previous(self):
		self.i -= 1
		fn = os.path.join(self.tt_img_dir, self.tt_imgs[self.i])
		self.tt_img = ImageTk.PhotoImage(file = fn)
		self.panel.configure(image = self.tt_img)
		if self.i == 0:
			self.left_btn.configure(state = 'disable')
			self.right_btn.configure(state = 'normal')
		elif self.i == len(self.tt_imgs) - 1:
			self.left_btn.configure(state = 'normal')
			self.right_btn.configure(state = 'disable')
		else:
			self.left_btn.configure(state = 'normal')
			self.right_btn.configure(state = 'normal')

	def return_root(self):
		self.canvas.destroy()
		self.frame.destroy()
		self.another = main.main_window(self.master)

