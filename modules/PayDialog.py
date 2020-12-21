from PyQt5.Qt import QDialog, pyqtSignal

from resource.paydialog import Ui_Dialog


class PayDialog(QDialog, Ui_Dialog):
	finish_signal = pyqtSignal(list)

	def __init__(self, cost, zid, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.cost = cost
		self.lineEdit_6.setText("{}".format(self.cost))
		self.zid = zid
		self.setWindowTitle("收款")

	def finish(self):
		khh = self.lineEdit.text()
		kid = self.lineEdit_2.text()
		mhh = self.lineEdit_4.text()
		mid = self.lineEdit_5.text()
		ty = self.lineEdit_3.text()
		dat = self.lineEdit_7.text()
		if khh and kid and mhh and mid and ty and dat:
			self.finish_signal.emit([self.zid, khh, kid, mhh, mid, ty, self.cost, dat])
			self.close()

	def exit(self):
		self.close()
