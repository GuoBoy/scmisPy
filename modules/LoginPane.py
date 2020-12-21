from PyQt5.Qt import QDialog, QErrorMessage, pyqtSignal
from PyQt5.QtCore import Qt

from resource.loginpane import Ui_Dialog
from modules.DBTool import CheckLogin


class LoginPane(QDialog, Ui_Dialog):
	login_signal = pyqtSignal()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.setWindowFlags(Qt.FramelessWindowHint)
		# self.setWindowOpacity()
		# self.lineEdit.setText("admin")
		# self.lineEdit_2.setText("admin")

	def login(self):
		"""登录函数"""
		acc = self.lineEdit.text()
		pas = self.lineEdit_2.text()
		if acc and pas:
			if CheckLogin(acc, pas).isHave():
				self.login_signal.emit()
				return
		# 登录失败提示
		error = QErrorMessage(self)
		error.setWindowTitle("提示")
		error.showMessage("登录失败，请正确输入后重试！")
		error.show()
