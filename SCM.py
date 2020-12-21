from PyQt5.Qt import QApplication
import sys

from modules.LoginPane import LoginPane
from modules.FunctionPane import FP


def logined():
	"""功能界面"""
	functionpane.show()
	loginpane.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)

	loginpane = LoginPane()
	functionpane = FP()

	loginpane.login_signal.connect(logined)

	loginpane.show()
	sys.exit(app.exec())
