from PyQt5.Qt import QDialog, pyqtSignal, QRegExpValidator, QRegExp
from PyQt5.QtWidgets import QErrorMessage
import re

from resource.addmaterialdialog import Ui_Dialog


class AddMaterialDialog(QDialog, Ui_Dialog):
	finish_signal = pyqtSignal(list)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		# validator = QRegExpValidator(QRegExp('[\d.]+'))
		# self.lineEdit_3.setValidator(validator)

	def exit(self):
		self.close()

	def finish(self):
		name = self.lineEdit.text()
		num = self.spinBox.value()
		price = re.findall("[\d.]+", self.lineEdit_3.text())[0]
		if name and num and price:
			self.finish_signal.emit([name, int(num), float(price)])
			self.close()
		else:
			mes = QErrorMessage(self)
			mes.setWindowTitle("提示")
			mes.showMessage("请输入完整内容！")
			mes.show()
