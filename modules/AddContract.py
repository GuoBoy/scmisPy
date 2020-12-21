from PyQt5.Qt import QWidget, QHeaderView, QStandardItemModel, QStandardItem, QErrorMessage, QFileDialog
from time import time, strftime

from resource.addcontract import Ui_Form

from modules.AddMaterialDialog import AddMaterialDialog
from modules.PreviewPane import PreviewPane
from modules.DBTool import SaveContract, getToday


class AddContract(QWidget, Ui_Form):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)

		self.materiallist = list()
		self.title = ['印刷材料', '印刷单价', '印刷数量']
		self.totalprice = 0
		self.model = QStandardItemModel()
		self.comboBox.addItems(['银行转账'])
		self.showTable()

	def showTable(self):
		self.totalprice = 0
		# 设置表格表头
		self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.model.clear()
		self.model.setHorizontalHeaderLabels(self.title)
		self.tableView.setModel(self.model)
		# 设置内容
		if self.materiallist:
			for b in self.materiallist:
				for col in range(3):
					item = QStandardItem("{}".format(b[col]))
					self.model.setItem(self.materiallist.index(b), col, item)
			self.tableView.setModel(self.model)
			for m in self.materiallist:
				self.totalprice += m[1] * m[2]
		self.lineEdit_5.setText("{}".format(self.totalprice))

	def showAddPane(self):
		"""显示添加面板"""
		self.selectdialog = AddMaterialDialog(self)
		self.selectdialog.show()
		self.selectdialog.finish_signal.connect(self.appendMaterial)

	def appendMaterial(self, item):
		for i in self.materiallist:
			if item[0] == i[0]:
				error = QErrorMessage(self)
				error.setWindowTitle("提示")
				error.showMessage("{}已存在，请删除原来的再添加".format(item[0]))
				error.show()
				return
		try:
			self.materiallist.append(item)
			self.showTable()
		except Exception as ret:
			print(ret)

	def delProduct(self):
		"""删除产品"""
		try:
			index = self.tableView.currentIndex().row()
			self.materiallist.pop(index)
			self.showTable()
		except Exception as ret:
			print(ret)

	def onSave(self):
		"""导出保存"""
		ccompany = self.lineEdit.text().strip()
		cman = self.lineEdit_2.text().strip()
		cphone = self.lineEdit_3.text().replace('-', '').strip()
		caddress = self.lineEdit_4.text().strip()
		csigndate = self.lineEdit_6.text()
		cgive = self.lineEdit_7.text()
		cpaydate = self.lineEdit_11.text()
		myname = self.lineEdit_8.text().strip()
		myphone = self.lineEdit_9.text().replace('-', '')
		myaddres = self.lineEdit_10.text().strip()
		cpaymethod = self.comboBox.currentText()
		ctotalprice = self.lineEdit_5.text()
		cmaterials = ""
		for i in self.materiallist:
			cmaterials += "{}x{}x{};".format(i[0], i[1], i[2])
		cmaterials = cmaterials[:-1]
		print(cmaterials)

		if ccompany and cman and cphone and caddress and csigndate and cgive and cpaydate and myname and myphone and myaddres and cpaymethod and ctotalprice and cmaterials:
			cid = "H{}{}".format(csigndate.replace('-', ''), getToday(csigndate))
			print(cid)
			dd = [cid, cmaterials, ctotalprice, cpaymethod, ccompany, cman, cphone, caddress, csigndate, cgive, myname, myphone, myaddres, cpaydate]
			try:
				sc = SaveContract(dd)
				sc.saveContract()
				# 制作合同
				f = open("resource/static/contractmodel.html", 'r', encoding="utf-8")
				m = f.read()
				f.close()
				temp = ""
				cmaterials = cmaterials.split("x")[0]
				l = [cid, cmaterials, ctotalprice, cpaymethod, ccompany, cman, cphone, caddress, csigndate, cgive, cpaydate]
				n = 0
				for i in m:
					if i == "{":
						temp += "{}".format(l[n])
						n += 1
					else:
						temp += i
				with open('resource/static/contractres.html', 'w', encoding='utf-8') as f:
					f.write(temp)
					print("制作完成")
				# 初始化
				self.materiallist = list()
				self.showTable()
				self.lineEdit.clear()
				self.lineEdit_2.clear()
				self.lineEdit_3.clear()
				self.lineEdit_4.clear()
				self.lineEdit_5.clear()
				self.lineEdit_6.clear()
				self.lineEdit_7.clear()
				self.lineEdit_8.clear()
				self.lineEdit_9.clear()
				self.lineEdit_10.clear()
				self.lineEdit_11.clear()
				self.previewpane = PreviewPane("resource/static/contractres.html")
				self.previewpane.show()
			except Exception as ret:
				print(ret)
		else:
			mes = QErrorMessage(self)
			mes.setWindowTitle("提示")
			mes.showMessage("请填写完整信息！")
			mes.show()
