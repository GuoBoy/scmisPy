from PyQt5.Qt import QDialog, pyqtSignal

from resource.kaipiaodialog import Ui_Dialog


class KaipaioDialog(QDialog, Ui_Dialog):
	finish_signal = pyqtSignal(list)

	def __init__(self, data, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.setWindowTitle("开票")
		self.data = data

	def finish(self):
		dat = self.lineEdit.text()
		if dat:
			self.data.insert(1, dat)
			self.finish_signal.emit(self.data)
			self.close()

	def exit(self):
		self.close()
