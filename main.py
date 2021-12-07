from tkinter import *
from tkinter import messagebox
import os, sys
from PIL import Image, ImageTk, ImageDraw
from threading import Thread
import walk, talk, bmath, aboutus, clock, snake, face, web

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

def add_corners(img, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', img.size, "white")
    w, h = img.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    img.putalpha(alpha)
    return img

alphabets = [
    ['`','1','2','3','4','5','6','7','8','9','0','-','=','Backspace'],
    ['Tab','q','w','e','r','t','y','u','i','o','p','[',']','\\'],
    ['Caps Lock','a','s','d','f','g','h','j','k','l',';',"'",'Enter'],
    ['Shift','z','x','c','v','b','n','m',',','.','/','Shift'],
    ['Space']
]

uppercase = False

def select(entry, value):
    global uppercase

    if value == 'Space':
        value = ' '
    elif value == 'Enter':
        value = '\n'
    elif value == 'Tab':
        value = '\t'

    if value == 'Backspace':
        if isinstance(entry, Entry):
            entry.delete(len(entry.get())-1, 'end')
        else:
            entry.delete('end - 2c', 'end')
    elif value in ('Caps Lock', 'Shift'):
        uppercase = not uppercase # change True to False, or False to True
    else:
        if uppercase:
            value = value.upper()
        entry.insert('end', value)

class main_window:
	def __init__(self, master):
		self.master = master
		self.canvas = Canvas(self.master, height = 600, width = 1024)
		self.canvas.pack()

		self.bg_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'background1.png'))
		self.bg_render = self.canvas.create_image((0, 0), image = self.bg_img, anchor = N + W)

		self.label_msg_render = self.canvas.create_text((520, 50), text = 'IVAST Bot Control Panel', font = ('Transformers Movie', 40), fill = '#CCCCFF')
		
		self.exit_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'exit1.png'))
		self.exit_btn = Button(self.master, image = self.exit_img,
			command = self.exit_root, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.exit_btn_render = self.canvas.create_window((900, 140), window = self.exit_btn)
		self.exit_btn_msg_render = self.canvas.create_text((900, 190), text = 'Thoát', font = ('Arial', 12, 'bold'), fill = WHITE)

		self.walk_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'walk1.png'))
		self.walk_btn = Button(self.master, image = self.walk_img,
			command = self.load_walk, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.walk_btn_render = self.canvas.create_window((124, 140), window = self.walk_btn)
		self.walk_btn_msg_render = self.canvas.create_text((124, 190), text = 'Di chuyển', font = ('Arial', 12, 'bold'), fill = WHITE)

		self.talk_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'talk1.png'))
		self.talk_btn = Button(self.master, image = self.talk_img,
			command = self.load_talk, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.talk_btn_render = self.canvas.create_window((235, 140), window = self.talk_btn)
		self.talk_btn_msg_render = self.canvas.create_text((235, 190), text = 'Nói chuyện', font = ('Arial', 12, 'bold'), fill = WHITE)

		self.math_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'math1.png'))
		self.math_btn = Button(self.master, image = self.math_img,
			command = self.load_math, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.math_btn_render = self.canvas.create_window((346, 140), window = self.math_btn)
		self.math_btn_msg_render = self.canvas.create_text((346, 190), text = 'Máy tính', font = ('Arial', 12, 'bold'), fill = WHITE)

		self.face_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'face1.png'))
		self.face_btn = Button(self.master, image = self.face_img,
			command = self.load_face, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.face_btn_render = self.canvas.create_window((457, 140), window = self.face_btn)
		self.vi_btn_msg_render1 = self.canvas.create_text((457, 190), text = 'Nhận diện', font = ('Arial', 12, 'bold'), fill = WHITE)
		self.vi_btn_msg_render2 = self.canvas.create_text((457, 210), text = 'khuôn mặt', font = ('Arial', 12, 'bold'), fill = WHITE)

		self.clock_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'clock1.png'))
		self.clock_btn = Button(self.master, image = self.clock_img,
			command = self.load_clock, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.clock_btn_rclockder = self.canvas.create_window((568, 140), window = self.clock_btn)
		self.clock_btn_msg_rclockder1 = self.canvas.create_text((568, 190), text = 'Đồng hồ', font = ('Arial', 12, 'bold'), fill = WHITE)

		# self.a = Image.open(os.path.join('Assets', 'snake.png'))
		# self.a = self.a.resize((int(self.a.size[0] / 10), int(self.a.size[1] / 10)), Image.ANTIALIAS)
		# self.a.save(os.path.join('Assets', 'snake1.png'))
		self.snake_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'snake1.png'))
		self.snake_btn = Button(self.master, image = self.snake_img,
			command = self.load_snake, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.snake_btn_render = self.canvas.create_window((679, 140), window = self.snake_btn)
		self.snake_btn_msg_render1 = self.canvas.create_text((679, 190), text = 'Rắn săn mồi', font = ('Arial', 12, 'bold'), fill = WHITE)

		self.aboutus_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'aboutus1.png'))
		self.aboutus_btn = Button(self.master, image = self.aboutus_img,
			command = self.load_aboutus, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.aboutus_btn_render = self.canvas.create_window((790, 140), window = self.aboutus_btn)
		self.aboutus_btn_msg_render1 = self.canvas.create_text((790, 190), text = 'Giới thiệu', font = ('Arial', 12, 'bold'), fill = WHITE)

		self.gg_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'web1.png'))
		self.gg_img_render = self.canvas.create_image((150, 280), image = self.gg_img)

		self.user_input_text = StringVar()
		self.user_input = Entry(self.canvas, textvariable = self.user_input_text, font = ('Times', 20, 'normal'), width = 40)
		self.user_input.focus()
		self.create_osk(self.user_input)
		self.user_input_render = self.canvas.create_window((480, 280), window = self.user_input)
		self.master.bind('<Return>', self.enter_key)

		self.find_img = ImageTk.PhotoImage(file = os.path.join('Assets', 'find1.png'))
		self.find_btn = Button(self.master, image = self.find_img,
			command = self.load_web, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00')
		self.find_btn_render = self.canvas.create_window((800, 280), window = self.find_btn)

	def create_osk(self, entry):
		self.kb = Canvas(self.canvas, height = 600, width = 1024, background = '#808080')
		self.kb_render = self.canvas.create_window((0, 350), window = self.kb, anchor = N + W)
		for y, row in enumerate(alphabets):
			x = 0
			for text in row:
				if text in ('Enter', 'Shift'):
					width = 15
					columnspan = 2
				elif text == 'Space':
					width = 120
					columnspan = 16
				elif text == 'Caps Lock':
					width = 5
					columnspan = 1
				else:                
					width = 5
					columnspan = 1
				Button(self.kb, text = text, width = width, command = lambda value = text: select(entry, value), font = ('Arial', 10, 'bold'),
					padx = 3, pady = 3, bd = 11, bg = '#808080', fg = WHITE).grid(row = y, column = x, columnspan = columnspan)
				x += columnspan

	def enter_key(self, event = None):
		self.load_web()

	def load_walk(self):
		self.canvas.destroy()
		self.another = walk.WALK(self.master)
	
	def load_talk(self):
		self.canvas.destroy()
		self.another = talk.TALK(self.master)

	def load_math(self):
		self.canvas.destroy()
		self.another = bmath.MATH(self.master)

	def load_clock(self):
		self.canvas.destroy()
		self.another = clock.CLOCK(self.master)
	
	def load_aboutus(self):
		self.canvas.destroy()
		self.another = aboutus.ABOUTUS(self.master)

	def load_snake(self):
		self.canvas.destroy()
		self.another = snake.SNAKE(self.master)
	
	def load_face(self):
		self.canvas.destroy()
		self.another = face.FACE(self.master)

	def load_web(self):
		self.user_input_text_content = self.user_input_text.get()
		self.canvas.destroy()
		self.another = web.WEB(self.master, self.user_input_text_content)
	
	def exit_root(self):
		self.master.destroy()
		sys.exit()

def on_closing():
	if messagebox.askokcancel('Quit', 'Bạn muốn thoát chứ ?'):
		root.destroy()
		sys.exit()

if __name__ == '__main__':
	root = Tk()
	root.geometry('1024x600')
	root.title('Main')
	root.iconbitmap(os.path.join('Assets', 'logo.ico'))
	run = main_window(root)
	root.protocol('WM_DELETE_WINDOW', on_closing)
	root.resizable(False, False)
	# root.attributes('-fullscreen', True)
	root.mainloop()



