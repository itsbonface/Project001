from PyQt5.QtWidgets import *

class WindowOne(QWidget):

	def __init__(self):
		super().__init__()
		layout = QVBoxLayout()
		self.label = QLabel("Another")
		layout.addWidget(self.label)
		self.setLayout(layout)


class WindowMain(QMainWindow):

	def __init__(self):
		super().__init__()
		self.w = WindowOne()
		self.btn = QPushButton("Push")
		self.btn.clicked.connect(self.new_window)
		self.setCentralWidget(self.btn)

	def new_window(self, arg):
		self.w.show()


def run():
	import sys
	app = QApplication(sys.argv)
	w = WindowMain()
	w.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	run()
		
