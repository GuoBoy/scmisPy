from PyQt5.Qt import QDialog, pyqtSignal

from resource.adduserpane import Ui_Dialog


class AddUserDialog(QDialog, Ui_Dialog):
	finish_signal = pyqtSignal(str, str)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)

	def add(self):
		acc = self.lineEdit.text()
		paw = self.lineEdit_2.text()
		if acc and paw:
			self.finish_signal.emit(acc, paw)
			self.close()

	def exit(self):
		self.close()
