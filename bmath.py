from tkinter import *
from tkinter import messagebox
import os, sys
from PIL import Image, ImageTk, ImageDraw
from threading import Thread
import main

BLACK = '#000000'
WHITE = '#FFFFFF'

def btn_click(item, input_text):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear(input_text): 
    global expression 
    expression = '' 
    input_text.set('')
 
def bt_equal(input_text):
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ''

expression = ''

class MATH:
	def __init__(self, master):
		self.master = master
		self.canvas = Canvas(self.master, height = 600, width = 1024)
		self.canvas.pack()

		self.bg_img = ImageTk.PhotoImage(file = os.path.join('Assets', os.path.join('Math', 'background.png')))
		self.bg_render = self.canvas.create_image((0, 0), image = self.bg_img, anchor = N + W)
		
		self.label_msg_render = self.canvas.create_text((520, 50), text = 'IVAST Bot - Calculator', font = ('Transformers Movie', 40), fill = '#CCCCFF')

		self.return_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Math'), 'return1.png'))
		self.return_btn = Button(self.master, image = self.return_img, text = ' Return ',
			command = self.return_root, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00', compound = LEFT)
		self.return_btn_render = self.canvas.create_window((100, 50), window = self.return_btn)
		self.create_calculator()

	def create_calculator(self):
		self.cal = Canvas(self.canvas, height = 460, width = 836, background = '#808080')
		self.cal_render = self.canvas.create_window((90, 100), window = self.cal, anchor = N + W)
		self.input_text = StringVar()
		self.input_field = Entry(self.cal, font = ('Arial', 49, 'bold'), textvariable = self.input_text, width = 23, bg = '#eee', bd = 0, justify = RIGHT)
		self.input_field_render = self.cal.create_window((5, 5), window = self.input_field, anchor = N + W)

		self.clear = Button(self.canvas, text = 'CLEAR', fg = 'black', width = 76, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#eee', cursor = 'hand2', command = lambda: bt_clear(self.input_text))
		self.clear_render = self.cal.create_window((5, 87), window = self.clear, anchor = N + W)
		self.divide = Button(self.canvas, text = '/', fg = 'black', width = 25, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#eee', cursor = 'hand2', command = lambda: btn_click('/', self.input_text))
		self.divide_render = self.cal.create_window((628, 87), window = self.divide, anchor = N + W)
		self.seven = Button(self.cal, text = '7', fg = 'black', width = 24, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(7, self.input_text))
		self.senven_render = self.cal.create_window((5, 162), window = self.seven, anchor = N + W)
		self.eight = Button(self.cal, text = '8', fg = 'black', width = 25, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(8, self.input_text))
		self.eight_render = self.cal.create_window((209, 162), window = self.eight, anchor = N + W)
		self.nine = Button(self.cal, text = '9', fg = 'black', width = 24, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(9, self.input_text))
		self.nine_render = self.cal.create_window((421, 162), window = self.nine, anchor = N + W)
		self.multiply = Button(self.cal, text = 'x', fg = 'black', width = 25, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#eee', cursor = 'hand2', command = lambda: btn_click('*', self.input_text))
		self.multiply_render = self.cal.create_window((628, 162), window = self.multiply, anchor = N + W)

		self.four = Button(self.cal, text = '4', fg = 'black', width = 24, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(4, self.input_text))
		self.four_render = self.cal.create_window((5, 237), window = self.four, anchor = N + W)
		self.five = Button(self.cal, text = '5', fg = 'black', width = 25, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(5, self.input_text))
		self.five_render = self.cal.create_window((209, 237), window = self.five, anchor = N + W)
		self.six = Button(self.cal, text = '6', fg = 'black', width = 24, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(6, self.input_text))
		self.six_render = self.cal.create_window((421, 237), window = self.six, anchor = N + W)
		self.minus = Button(self.cal, text = '_', fg = 'black', width = 25, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#eee', cursor = 'hand2', command = lambda: btn_click('-', self.input_text))
		self.minus_render = self.cal.create_window((628, 237), window = self.minus, anchor = N + W)

		self.one = Button(self.cal, text = '1', fg = 'black', width = 24, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(1, self.input_text))
		self.one_render = self.cal.create_window((5, 312), window = self.one, anchor = N + W)
		self.two = Button(self.cal, text = '2', fg = 'black', width = 25, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(2, self.input_text))
		self.two_render = self.cal.create_window((209, 312), window = self.two, anchor = N + W)
		self.three = Button(self.cal, text = '3', fg = 'black', width = 24, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(3, self.input_text))
		self.three_render = self.cal.create_window((421, 312), window = self.three, anchor = N + W)
		self.plus = Button(self.cal, text = '+', fg = 'black', width = 25, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#eee', cursor = 'hand2', command = lambda: btn_click('+', self.input_text))
		self.plus_render = self.cal.create_window((628, 312), window = self.plus, anchor = N + W)

		self.zero = Button(self.cal, text = '0', fg = 'black', width = 50, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#fff', cursor = 'hand2', command = lambda: btn_click(0, self.input_text))
		self.zero_render = self.cal.create_window((7, 387), window = self.zero, anchor = N + W)
		self.point = Button(self.cal, text = ',', fg = 'black', width = 24, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#eee', cursor = 'hand2', command = lambda: btn_click('.', self.input_text))
		self.point_render = self.cal.create_window((421, 387), window = self.point, anchor = N + W)
		self.equals = Button(self.cal, text = '=', fg = 'black', width = 25, height = 4, bd = 0, font = ('Arial', 10, 'bold'),
			bg = '#eee', cursor = 'hand2', command = lambda: bt_equal(self.input_text))
		self.equals_render = self.cal.create_window((628, 387), window = self.equals, anchor = N + W)

	def return_root(self):
		self.canvas.destroy()
		self.another = main.main_window(self.master)

