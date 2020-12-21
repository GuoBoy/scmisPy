from PyQt5.Qt import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QErrorMessage

from resource.systemmanage import Ui_Form
from modules.DBTool import UserManage
from modules.AddUserDialog import AddUserDialog


class SystemManage(QWidget, Ui_Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.model = QStandardItemModel()
		self.title = ['用户id', '用户名', '权限']
		self.data = list()
		self.showAll()

	def setTableHeader(self):
		# 设置表格表头
		self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.model.clear()
		self.model.setHorizontalHeaderLabels(self.title)
		self.tableView.setModel(self.model)

	def showTables(self):
		# 设置内容
		for b in self.data:
			for col in range(3):
				item = QStandardItem("{}".format(b[col]))
				self.model.setItem(self.data.index(b), col, item)
		self.tableView.setModel(self.model)

	def showAll(self):
		self.model.clear()
		self.setTableHeader()
		u = UserManage()
		self.data = u.getUsers()
		if self.data:
			self.showTables()

	def addUser(self):
		self.ad = AddUserDialog()
		self.ad.show()
		self.ad.finish_signal.connect(self.au)

	def au(self, acc, paw):
		u = UserManage()
		u.addUser(acc, paw)
		er = QErrorMessage(self)
		er.setWindowTitle("提示")
		er.showMessage("添加成功！")
		er.show()
		self.showAll()

	def delUser(self):
		try:
			index = self.tableView.currentIndex().row()
			u = UserManage()
			u.delUser(self.data[index][0])
			self.showAll()
		except Exception as ret:
			print(ret)

