from PyQt5.Qt import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QErrorMessage

from resource.clientmanage import Ui_Form
from modules.DBTool import ClientManager


class ClientManage(QWidget, Ui_Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.model = QStandardItemModel()
		self.title = ['公司名称', '联系人姓名', '电话', '公司地址', '客户开户行', '银行卡号']
		self.data = list()

	def showTable(self):
		self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.model.clear()
		self.model.setHorizontalHeaderLabels(self.title)
		self.tableView.setModel(self.model)
		if self.data:
			for b in self.data:
				for col in b:
					item = QStandardItem("{}".format(b[b.index(col)]))
					self.model.setItem(self.data.index(b), b.index(col), item)
			self.tableView.setModel(self.model)

	def showAllClient(self):
		try:
			u = ClientManager()
			self.data = u.getClients()
			if self.data:
				print(self.data)
				self.showTable()
		except Exception as ret:
			print(ret)

	def delClient(self):
		try:
			index = self.tableView.currentIndex().row()
			self.data.pop(index)
			self.showTable()
			mes = QErrorMessage(self)
			mes.setWindowTitle("提示")
			mes.showMessage("删除成功！")
			mes.show()
		except Exception as ret:
			print(ret)
			mes = QErrorMessage(self)
			mes.setWindowTitle("提示")
			mes.showMessage("删除失败！")
			mes.show()

