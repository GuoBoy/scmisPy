from PyQt5.Qt import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QErrorMessage

from resource.paymanagepane import Ui_Form
from modules.DBTool import ZhuanzhangNote, CreditAbout
from modules.PayDialog import PayDialog


class PayManagePane(QWidget, Ui_Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.model = QStandardItemModel()
		self.title = ['合同id', '合同公司', '合同金额', '签定日期', '交货日期', '付款日期']
		self.data = list()
		self.showAll()

	def showTable(self):
		# 设置表格表头
		self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.model.clear()
		self.model.setHorizontalHeaderLabels(self.title)
		self.tableView.setModel(self.model)
		if self.data:
			for b in self.data:
				for col in range(6):
					item = QStandardItem("{}".format(b[col]))
					self.model.setItem(self.data.index(b), col, item)
			self.tableView.setModel(self.model)

	def showAll(self):
		"""显示所有合同"""
		self.model.clear()
		c = CreditAbout()
		self.data = c.getFilter()
		if self.data:
			self.showTable()

	def onPay(self):
		print("支付")
		try:
			index = self.tableView.currentIndex().row()
			self.cid = self.data[index][0]
			zid = self.cid.replace('H', 'Z')
			self.paydialog = PayDialog(self.data[index][2], zid)
			self.paydialog.show()
			self.paydialog.finish_signal.connect(self.pay)
		except Exception as ret:
			print(ret)
			mes = QErrorMessage(self)
			mes.setWindowTitle("提示")
			mes.showMessage("支付失败")
			mes.show()

	def pay(self, data):
		c = ZhuanzhangNote()
		c.addNote(data)
		d = CreditAbout()
		d.setPayed(self.cid)
		self.showAll()
		mes = QErrorMessage(self)
		mes.setWindowTitle("提示")
		mes.showMessage("支付成功！")
		mes.show()
