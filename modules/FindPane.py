from PyQt5.Qt import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QErrorMessage

from resource.findpane import Ui_Form
from modules.DBTool import CreditAbout


class FindPane(QWidget, Ui_Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.model = QStandardItemModel()
		self.title = ['合同id', '合同公司', '合同金额', '签定日期', '交货日期', '付款日期']
		self.data = list()
		self.comboBox.addItems(['合同id', '合同公司', '签定日期', '交货日期'])
		self.dic = ['cid', 'ccompany', 'signdate', 'givedate']
		c = CreditAbout()
		self.data = c.getAllContract()
		self.showTable()

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

	def findContract(self):
		print("查找")
		ty = self.dic[self.comboBox.currentIndex()]
		d = self.lineEdit.text()
		if d:
			c = CreditAbout()
			self.data = c.getList(ty, d)
			self.showTable()
			mes = QErrorMessage(self)
			mes.setWindowTitle("提示")
			mes.showMessage("共找到{}条数据".format(len(self.data)))
			mes.show()
			return
		mes = QErrorMessage(self)
		mes.setWindowTitle("提示")
		mes.showMessage("查找失败！请输入正确格式！")
		mes.show()
