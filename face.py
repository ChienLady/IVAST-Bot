from tkinter import *
from tkinter import messagebox
import os, sys, cv2
from PIL import Image, ImageTk, ImageDraw
from threading import Thread
import numpy as np
import face_recognition
import main

BLACK = '#000000'
WHITE = '#FFFFFF'

cam_port = 1
cap = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)

elliot_image = face_recognition.load_image_file(os.path.join('Assets', os.path.join('Face', os.path.join('Data', 'elliot.jpg'))))
elliot_face_encoding = face_recognition.face_encodings(elliot_image)[0]

mc_image = face_recognition.load_image_file(os.path.join('Assets', os.path.join('Face', os.path.join('Data', 'minh_chien.jpg'))))
mc_face_encoding = face_recognition.face_encodings(mc_image)[0]

known_face_encodings = [
	elliot_face_encoding,
	mc_face_encoding
]
known_face_names = [
	'Elliot',
	'Minh Chien'
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

class FACE:
	def __init__(self, master):
		self.master = master
		self.canvas = Canvas(self.master, height = 600, width = 1024)
		self.canvas.pack()

		self.bg_img = ImageTk.PhotoImage(file = os.path.join('Assets', os.path.join('Face', 'background.png')))
		self.bg_render = self.canvas.create_image((0, 0), image = self.bg_img, anchor = N + W)
		
		self.label_msg_render = self.canvas.create_text((520, 50), text = 'IVAST Bot - Face', font = ('Transformers Movie', 40), fill = '#CCCCFF')

		# self.a = Image.open(os.path.join(os.path.join('Assets', 'Walk'), 'return.png'))
		# self.a = self.a.resize((int(self.a.size[0] / 12), int(self.a.size[1] / 12)), Image.ANTIALIAS)
		# self.a.save(os.path.join(os.path.join(os.path.join('Assets', 'Walk'), 'return1.png')))
		self.return_img = ImageTk.PhotoImage(file = os.path.join(os.path.join('Assets', 'Face'), 'return1.png'))
		self.return_btn = Button(self.master, image = self.return_img, text = ' Return ',
			command = self.return_root, font = (('Arial'), 15, 'bold'),
			background = '#CCCCFF', activebackground = '#FFBF00', compound = LEFT)
		self.return_btn_render = self.canvas.create_window((100, 50), window = self.return_btn)
		self.frame_init = 0
		self.create_cam_frame()

	def process(self):
		if cap.isOpened():
			ret, self.frame = cap.read()
			if ret:
				scale = 0.8
				width = int(self.frame.shape[1] * scale)
				height = int(self.frame.shape[0] * scale)
				self.dim = (width, height)
				self.frame.flags.writeable = False
				self.frame = cv2.resize(self.frame, self.dim, interpolation = cv2.INTER_AREA)
				self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
				self.frame = cv2.flip(self.frame, flipCode = 1)

				small_frame = cv2.resize(self.frame, (0, 0), fx = 0.25, fy = 0.25)
				rgb_small_frame = small_frame[:, :, ::-1]
				if process_this_frame:
					face_locations = face_recognition.face_locations(rgb_small_frame)
					face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
					face_names = []
					for face_encoding in face_encodings:
						matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
						name = 'Unknown'
						face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
						best_match_index = np.argmin(face_distances)
						if matches[best_match_index]:
							name = known_face_names[best_match_index]
						face_names.append(name)
				for (top, right, bottom, left), name in zip(face_locations, face_names):
					top *= 4
					right *= 4
					bottom *= 4
					left *= 4
					cv2.rectangle(self.frame, (left, top), (right, bottom), (255, 0, 0), 2)
					cv2.rectangle(self.frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
					font = cv2.FONT_HERSHEY_DUPLEX
					cv2.putText(self.frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
				self.frame.flags.writeable = True
				
				self.frame = Image.fromarray(self.frame)
				self.imgtk = ImageTk.PhotoImage(image = self.frame)
				self.cam.configure(image = self.imgtk)
				self.cam.after(10, self.process)

	def create_cam_frame(self):
		self.frame = Canvas(self.canvas, height = 470, width = 836, background = '#808080')
		self.frame_render = self.canvas.create_window((90, 100), window = self.frame, anchor = N + W)
		self.cam = Label(self.master)
		self.cam_render = self.frame.create_window((50, 50), window = self.cam, anchor = N + W)
		self.process()

	def return_root(self):
		self.canvas.destroy()
		self.another = main.main_window(self.master)

