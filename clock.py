from tkinter import *
from tkinter import messagebox
import os, time, datetime
from PIL import Image, ImageTk, ImageDraw
import threading
import main
from playsound import playsound

BLACK = '#000000'
WHITE = '#FFFFFF'

class CLOCK:
	def __init__(self, master):
		self.master = master
		self.canvas = Canvas(self.master, height = 600, width = 1024)
		self.canvas.pack()

		self.bg_img = ImageTk.PhotoImage(file = os.path.join('Assets', os.path.join('Clock', 'background.png')))
		self.bg_render = self.canvas.create_image((0, 0), image = self.bg_img, anchor = N + W)
		
		self.label_msg_render = self.canvas.create_text((520, 50), text = 'IVAST Bot - Clock', font = ('Transformers Movie', 40), fill = '#CCCCFF')

		self.return_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Clock'), 'return1.png'))
		self.return_btn = Button(self.master, image = self.return_img, text = ' Return ',
			command = self.return_root, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00', compound = LEFT)
		self.return_btn_render = self.canvas.create_window((100, 50), window = self.return_btn)

		self.border = Label(self.canvas, bg = '#DE3163', width = 83, height = 11)
		self.border_render = self.canvas.create_window((500, 180), window = self.border)
		self.create_clock()
		self.create_alarm()
	
	def create_clock(self):
		self.clock = Label(self.canvas, font = ('Courier', 30, 'bold'), bg = BLACK, fg = '#00FF00', bd = 30)
		self.clock_render = self.canvas.create_window((500, 180), window = self.clock)
		self.update()

	def update(self):
		clock_str = time.strftime('%H:%M:%S %p \n %A, %d %B')
		self.clock.config(text = clock_str)
		self.clock.after(200, self.update)

	def create_alarm(self):
		self.hour = StringVar(self.master)
		self.hours = ('00', '01', '02', '03', '04', '05', '06', '07',
				'08', '09', '10', '11', '12', '13', '14', '15',
				'16', '17', '18', '19', '20', '21', '22', '23', '24'
				)
		self.hour.set(self.hours[0])
		self.hrs = OptionMenu(self.master, self.hour, *self.hours)
		self.minute = StringVar(self.master)
		self.minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
				'08', '09', '10', '11', '12', '13', '14', '15',
				'16', '17', '18', '19', '20', '21', '22', '23',
				'24', '25', '26', '27', '28', '29', '30', '31',
				'32', '33', '34', '35', '36', '37', '38', '39',
				'40', '41', '42', '43', '44', '45', '46', '47',
				'48', '49', '50', '51', '52', '53', '54', '55',
				'56', '57', '58', '59', '60')
		self.minute.set(self.minutes[0])
		self.mins = OptionMenu(self.master, self.minute, *self.minutes)
		self.second = StringVar(self.master)
		self.seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
				'08', '09', '10', '11', '12', '13', '14', '15',
				'16', '17', '18', '19', '20', '21', '22', '23',
				'24', '25', '26', '27', '28', '29', '30', '31',
				'32', '33', '34', '35', '36', '37', '38', '39',
				'40', '41', '42', '43', '44', '45', '46', '47',
				'48', '49', '50', '51', '52', '53', '54', '55',
				'56', '57', '58', '59', '60')
		self.second.set(self.seconds[0])
		self.secs = OptionMenu(self.master, self.second, *self.seconds)

		self.alarm_frame = Canvas(self.canvas, height = 280, width = 600, background = '#808080')
		self.alarm_frame_render = self.canvas.create_window((500, 420), window = self.alarm_frame)

		self.hour_msg_render = self.alarm_frame.create_text((300, 20), text = 'Chọn giờ muốn báo thức', font = ('Arial', 15, 'bold'), fill = '#CCCCFF')

		self.hrs_render = self.alarm_frame.create_window((180, 70), window = self.hrs)
		self.mins_render = self.alarm_frame.create_window((300, 70), window = self.mins)
		self.secs_render = self.alarm_frame.create_window((420, 70), window = self.secs)

		self.hour_msg_render = self.alarm_frame.create_text((230, 70), text = 'giờ', font = ('Arial', 12, 'bold'), fill = '#CCCCFF')
		self.minute_msg_render = self.alarm_frame.create_text((350, 70), text = 'phút', font = ('Arial', 12, 'bold'), fill = '#CCCCFF')
		self.second_msg_render = self.alarm_frame.create_text((470, 70), text = 'giây', font = ('Arial', 12, 'bold'), fill = '#CCCCFF')

		self.set_alarm_btn = Button(self.master, text = 'Đặt báo thức', font = ('Helvetica', 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00', command = self.Threading)
		self.set_alarm_btn_render = self.alarm_frame.create_window((300, 130), window = self.set_alarm_btn)
	
	def alarm(self):
		set_alarm_time = f'{self.hour.get()}:{self.minute.get()}:{self.second.get()}'
		while self.state:
			time.sleep(1)
			current_time = datetime.datetime.now().strftime('%H:%M:%S')
			print(current_time, set_alarm_time)
			if current_time == set_alarm_time:
				playsound(os.path.join('Assets', os.path.join('Clock', 'alarm.mp3')))

	def on_closing(self):
		if messagebox.askokcancel('Quit', 'Tắt đồng nghĩa với việc xóa báo thức ?'):
			self.state = False
			self.top.destroy()

	def Threading(self):
		self.top = Toplevel()
		set_alarm_time = f'{self.hour.get()}:{self.minute.get()}:{self.second.get()}'
		self.alarm_label = Label(self.top, font = ('Courier', 15, 'bold'), bg = BLACK, fg = '#00FF00', bd = 5,
			text = f'Báo thức dậy lúc {set_alarm_time}')
		self.alarm_label.pack()
		self.del_alarm_btn = Button(self.top, text = 'Xóa báo thức', font = ('Helvetica', 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00', command = self.del_alarm)
		self.del_alarm_btn.pack()
		self.top.resizable(False, False)
		self.top.protocol('WM_DELETE_WINDOW', self.on_closing)
		self.state = True
		self.t1 = threading.Thread(target = self.alarm, args = (), daemon = True)
		self.t1.start()
		self.top.mainloop()
			
	def del_alarm(self):
		self.state = False
		# self.t1.join()
		self.top.destroy()

	def return_root(self):
		self.canvas.destroy()
		self.another = main.main_window(self.master)

