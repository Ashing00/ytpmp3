#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import youtube_dl

ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}

class Youtube_MP3(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):	   

		self.btn = QPushButton('下載', self)
		self.btn.move(380, 25)
		self.btn.resize(100,30)
		self.btn.clicked.connect(self.DownloadMP3)
		
		
		self.LB0_str='輸入Youtube影片位址:'
		self.LB0 = QLabel(self.LB0_str, self)
		self.LB0.move(20, 20)
		self.LB0.setFont(QFont('SimHei', 12))
		self.LB0.setStyleSheet("color: rgb(0, 0, 0);")
		self.LB0.resize(400,40)
		
		self.InputEdit = QLineEdit("https://www.youtube.com/watch?v=GCgvpwLNvtY",self)
		
		self.InputEdit.move(20, 60)
		self.InputEdit.resize(450,25)
		
		
		self.reviewEdit = QTextEdit('Loading...', self)
		self.reviewEdit.setFont(QFont('Arial', 12))
		self.reviewEdit.resize(450,180)
		self.reviewEdit.move(20, 100)
		self.reviewEdit.setReadOnly(True)
		self.reviewEdit.setStyleSheet("color: rgb(0, 200, 0);background-color: rgb(0, 0, 0)");
		

		self.setGeometry(100, 100, 500, 300)
		self.setWindowTitle('Download MP3 From Youtube Video')
		self.show()
			
	def DownloadMP3(self):		
		URL=self.InputEdit.text()
		str="Downloading from "+URL
		self.reviewEdit.append(str)
		self.repaint()	
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([URL])	
		self.reviewEdit.append("Finish!")	
			
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Youtube_MP3()
	sys.exit(app.exec_())
	
